import os
from pathlib import Path

import mysql.connector
import psycopg2
from dotenv import load_dotenv


load_dotenv()


# --------------------------------------------------
# DATABASE CONNECTIONS
# --------------------------------------------------

def get_mysql_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


def get_postgres_connection():
    database_url = Path("/tmp/render_url").read_text().strip()
    return psycopg2.connect(database_url)


# --------------------------------------------------
# POSTGRESQL SCHEMA
# --------------------------------------------------

SCHEMA = """

DROP TABLE IF EXISTS maintenance;
DROP TABLE IF EXISTS fuel_records;
DROP TABLE IF EXISTS cargo;
DROP TABLE IF EXISTS voyages;
DROP TABLE IF EXISTS crew;
DROP TABLE IF EXISTS ships;


CREATE TABLE ships (
    ship_id INTEGER PRIMARY KEY,
    ship_name VARCHAR(100) NOT NULL,
    imo_number VARCHAR(20) UNIQUE NOT NULL,
    flag VARCHAR(50),
    ship_type VARCHAR(50),
    capacity DECIMAL(10,2),
    status VARCHAR(30)
);


CREATE TABLE crew (
    crew_id INTEGER PRIMARY KEY,
    crew_name VARCHAR(100) NOT NULL,
    crew_rank VARCHAR(50) NOT NULL,
    nationality VARCHAR(50),
    ship_id INTEGER,
    joining_date DATE,
    status VARCHAR(30),
    FOREIGN KEY (ship_id) REFERENCES ships(ship_id)
);


CREATE TABLE voyages (
    voyage_id INTEGER PRIMARY KEY,
    ship_id INTEGER NOT NULL,
    departure_port VARCHAR(100) NOT NULL,
    destination_port VARCHAR(100) NOT NULL,
    departure_date DATE,
    arrival_date DATE,
    voyage_status VARCHAR(30),
    FOREIGN KEY (ship_id) REFERENCES ships(ship_id)
);


CREATE TABLE cargo (
    cargo_id INTEGER PRIMARY KEY,
    voyage_id INTEGER NOT NULL,
    cargo_type VARCHAR(100) NOT NULL,
    quantity DECIMAL(10,2),
    unit VARCHAR(30),
    destination VARCHAR(100),
    cargo_status VARCHAR(30),
    FOREIGN KEY (voyage_id) REFERENCES voyages(voyage_id)
);


CREATE TABLE fuel_records (
    fuel_id INTEGER PRIMARY KEY,
    ship_id INTEGER NOT NULL,
    fuel_type VARCHAR(50),
    quantity DECIMAL(10,2),
    cost DECIMAL(12,2),
    fuel_date DATE,
    port VARCHAR(100),
    FOREIGN KEY (ship_id) REFERENCES ships(ship_id)
);


CREATE TABLE maintenance (
    maintenance_id INTEGER PRIMARY KEY,
    ship_id INTEGER NOT NULL,
    maintenance_type VARCHAR(100),
    maintenance_date DATE,
    cost DECIMAL(12,2),
    maintenance_status VARCHAR(30),
    description VARCHAR(255),
    FOREIGN KEY (ship_id) REFERENCES ships(ship_id)
);

"""


# --------------------------------------------------
# TABLE DEFINITIONS
# --------------------------------------------------

TABLES = {
    "ships": [
        "ship_id",
        "ship_name",
        "imo_number",
        "flag",
        "ship_type",
        "capacity",
        "status"
    ],

    "crew": [
        "crew_id",
        "crew_name",
        "crew_rank",
        "nationality",
        "ship_id",
        "joining_date",
        "status"
    ],

    "voyages": [
        "voyage_id",
        "ship_id",
        "departure_port",
        "destination_port",
        "departure_date",
        "arrival_date",
        "voyage_status"
    ],

    "cargo": [
        "cargo_id",
        "voyage_id",
        "cargo_type",
        "quantity",
        "unit",
        "destination",
        "cargo_status"
    ],

    "fuel_records": [
        "fuel_id",
        "ship_id",
        "fuel_type",
        "quantity",
        "cost",
        "fuel_date",
        "port"
    ],

    "maintenance": [
        "maintenance_id",
        "ship_id",
        "maintenance_type",
        "maintenance_date",
        "cost",
        "maintenance_status",
        "description"
    ]
}


# --------------------------------------------------
# MIGRATION
# --------------------------------------------------

def migrate():
    mysql_connection = None
    mysql_cursor = None
    postgres_connection = None
    postgres_cursor = None

    try:
        print("Connecting to local MySQL...")
        mysql_connection = get_mysql_connection()
        mysql_cursor = mysql_connection.cursor()

        print("Connecting to Render PostgreSQL...")
        postgres_connection = get_postgres_connection()
        postgres_cursor = postgres_connection.cursor()

        print("Creating PostgreSQL tables...")
        postgres_cursor.execute(SCHEMA)
        postgres_connection.commit()

        print("PostgreSQL schema created successfully.")
        print()

        for table_name, columns in TABLES.items():

            column_list = ", ".join(columns)

            mysql_cursor.execute(
                f"SELECT {column_list} FROM {table_name}"
            )

            rows = mysql_cursor.fetchall()

            placeholders = ", ".join(["%s"] * len(columns))

            insert_query = f"""
                INSERT INTO {table_name}
                ({column_list})
                VALUES ({placeholders})
            """

            if rows:
                postgres_cursor.executemany(
                    insert_query,
                    rows
                )

            postgres_connection.commit()

            print(
                f"{table_name}: {len(rows)} records migrated"
            )

        print()
        print("========================================")
        print("MIGRATION COMPLETED SUCCESSFULLY")
        print("========================================")

    except Exception as error:
        if postgres_connection:
            postgres_connection.rollback()

        print()
        print("MIGRATION FAILED")
        print("ERROR:", error)

    finally:
        if mysql_cursor:
            mysql_cursor.close()

        if mysql_connection:
            mysql_connection.close()

        if postgres_cursor:
            postgres_cursor.close()

        if postgres_connection:
            postgres_connection.close()


if __name__ == "__main__":
    migrate()
