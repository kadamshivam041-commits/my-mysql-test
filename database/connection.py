import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="ocean_admin",
        password="Ocean@1234",
        database="ocean_command"
    )

    return connection
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