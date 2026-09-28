from database.connection import create_connection


def get_all_ships():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM ships"
    cursor.execute(query)

    ships = cursor.fetchall()

    cursor.close()
    connection.close()

    return ships


def get_all_crew():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            crew.crew_id,
            crew.crew_name,
            crew.crew_rank,
            crew.nationality,
            ships.ship_name,
            crew.joining_date,
            crew.status
        FROM crew
        JOIN ships
        ON crew.ship_id = ships.ship_id
    """

    cursor.execute(query)

    crew = cursor.fetchall()

    cursor.close()
    connection.close()

    return crew


def get_all_voyages():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            voyages.voyage_id,
            ships.ship_name,
            voyages.departure_port,
            voyages.destination_port,
            voyages.departure_date,
            voyages.arrival_date,
            voyages.voyage_status
        FROM voyages
        JOIN ships
        ON voyages.ship_id = ships.ship_id
    """

    cursor.execute(query)

    voyages = cursor.fetchall()

    cursor.close()
    connection.close()

    return voyages
def get_all_cargo():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            cargo.cargo_id,
            ships.ship_name,
            cargo.cargo_type,
            cargo.quantity,
            cargo.unit,
            cargo.destination,
            cargo.cargo_status
        FROM cargo
        JOIN voyages
        ON cargo.voyage_id = voyages.voyage_id
        JOIN ships
        ON voyages.ship_id = ships.ship_id
    """

    cursor.execute(query)

    cargo = cursor.fetchall()

    cursor.close()
    connection.close()

    return cargo
def get_all_fuel_records():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            fuel_records.fuel_id,
            ships.ship_name,
            fuel_records.fuel_type,
            fuel_records.quantity,
            fuel_records.cost,
            fuel_records.fuel_date,
            fuel_records.port
        FROM fuel_records
        JOIN ships
        ON fuel_records.ship_id = ships.ship_id
    """

    cursor.execute(query)

    fuel_records = cursor.fetchall()

    cursor.close()
    connection.close()

    return fuel_records
def get_all_maintenance():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            maintenance.maintenance_id,
            ships.ship_name,
            maintenance.maintenance_type,
            maintenance.maintenance_date,
            maintenance.cost,
            maintenance.maintenance_status,
            maintenance.description
        FROM maintenance
        JOIN ships
        ON maintenance.ship_id = ships.ship_id
    """

    cursor.execute(query)

    maintenance = cursor.fetchall()

    cursor.close()
    connection.close()

    return maintenance
def get_dashboard_stats():
    connection = create_connection()
    cursor = connection.cursor()

    stats = {}

    cursor.execute("SELECT COUNT(*) FROM ships")
    stats["ships"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM crew")
    stats["crew"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM voyages")
    stats["voyages"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM cargo")
    stats["cargo"] = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return stats
def get_fleet_status_report():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT status, COUNT(*)
        FROM ships
        GROUP BY status
    """

    cursor.execute(query)
    report = cursor.fetchall()

    cursor.close()
    connection.close()

    return report
