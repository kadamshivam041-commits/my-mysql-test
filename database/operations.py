from database.connection import create_connection


def get_all_ships():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ship_id,
            ship_name,
            imo_number,
            flag,
            ship_type,
            capacity,
            status
        FROM ships
        ORDER BY ship_id
    """)

    ships = cursor.fetchall()

    cursor.close()
    connection.close()

    return ships


def get_all_crew():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            crew.crew_id,
            crew.crew_name,
            crew.crew_rank,
            crew.nationality,
            crew.ship_id,
            ships.ship_name,
            crew.joining_date,
            crew.status
        FROM crew
        LEFT JOIN ships
            ON crew.ship_id = ships.ship_id
        ORDER BY crew.crew_id
    """)

    crew = cursor.fetchall()

    cursor.close()
    connection.close()

    return crew


def get_all_voyages():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            voyages.voyage_id,
            voyages.ship_id,
            ships.ship_name,
            voyages.departure_port,
            voyages.destination_port,
            voyages.departure_date,
            voyages.arrival_date,
            voyages.voyage_status
        FROM voyages
        LEFT JOIN ships
            ON voyages.ship_id = ships.ship_id
        ORDER BY voyages.voyage_id
    """)

    voyages = cursor.fetchall()

    cursor.close()
    connection.close()

    return voyages


def get_all_cargo():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            cargo.cargo_id,
            cargo.voyage_id,
            ships.ship_name,
            cargo.cargo_type,
            cargo.quantity,
            cargo.unit,
            cargo.destination,
            cargo.cargo_status
        FROM cargo
        LEFT JOIN voyages
            ON cargo.voyage_id = voyages.voyage_id
        LEFT JOIN ships
            ON voyages.ship_id = ships.ship_id
        ORDER BY cargo.cargo_id
    """)

    cargo = cursor.fetchall()

    cursor.close()
    connection.close()

    return cargo


def get_all_fuel_records():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            fuel_records.fuel_id,
            fuel_records.ship_id,
            ships.ship_name,
            fuel_records.fuel_type,
            fuel_records.quantity,
            fuel_records.cost,
            fuel_records.fuel_date,
            fuel_records.port
        FROM fuel_records
        LEFT JOIN ships
            ON fuel_records.ship_id = ships.ship_id
        ORDER BY fuel_records.fuel_id
    """)

    fuel_records = cursor.fetchall()

    cursor.close()
    connection.close()

    return fuel_records


def get_all_maintenance():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            maintenance.maintenance_id,
            maintenance.ship_id,
            ships.ship_name,
            maintenance.maintenance_type,
            maintenance.maintenance_date,
            maintenance.cost,
            maintenance.maintenance_status,
            maintenance.description
        FROM maintenance
        LEFT JOIN ships
            ON maintenance.ship_id = ships.ship_id
        ORDER BY maintenance.maintenance_id
    """)

    maintenance = cursor.fetchall()

    cursor.close()
    connection.close()

    return maintenance


def insert_ship(
    ship_name,
    imo_number,
    flag,
    ship_type,
    capacity,
    status
):
    connection = create_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO ships
            (ship_name, imo_number, flag, ship_type, capacity, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            ship_name,
            imo_number,
            flag,
            ship_type,
            capacity,
            status
        ))

        connection.commit()
        return True

    except Exception:
        connection.rollback()
        return False

    finally:
        cursor.close()
        connection.close()


def delete_ship(ship_id):
    connection = create_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            DELETE FROM ships
            WHERE ship_id = %s
        """, (ship_id,))

        connection.commit()
        return cursor.rowcount > 0

    except Exception:
        connection.rollback()
        return False

    finally:
        cursor.close()
        connection.close()


def update_ship(
    ship_id,
    ship_name,
    flag,
    ship_type,
    capacity,
    status
):
    connection = create_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            UPDATE ships
            SET
                ship_name = %s,
                flag = %s,
                ship_type = %s,
                capacity = %s,
                status = %s
            WHERE ship_id = %s
        """, (
            ship_name,
            flag,
            ship_type,
            capacity,
            status,
            ship_id
        ))

        connection.commit()
        return cursor.rowcount > 0

    except Exception:
        connection.rollback()
        return False

    finally:
        cursor.close()
        connection.close()