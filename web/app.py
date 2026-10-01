from flask import Flask, render_template

from database.operations import (
    get_all_ships,
    get_all_crew,
    get_all_voyages,
    get_all_cargo,
    get_all_fuel_records,
    get_all_maintenance
)


app = Flask(__name__)


@app.route("/")
def home():

    ships = get_all_ships()
    crew = get_all_crew()
    voyages = get_all_voyages()
    cargo = get_all_cargo()
    fuel_records = get_all_fuel_records()
    maintenance = get_all_maintenance()


    active_ships = sum(
        1 for ship in ships
        if ship["status"] == "Active"
    )


    at_port_ships = sum(
        1 for ship in ships
        if ship["status"] == "At Port"
    )


    maintenance_ships = sum(
        1 for ship in ships
        if ship["status"] == "Maintenance"
    )


    current_voyages = [
        voyage
        for voyage in voyages
        if voyage["voyage_status"] == "In Progress"
    ]


    return render_template(
        "dashboard.html",
        ships=ships,
        crew=crew,
        voyages=voyages,
        cargo=cargo,
        fuel_records=fuel_records,
        maintenance=maintenance,
        active_ships=active_ships,
        at_port_ships=at_port_ships,
        maintenance_ships=maintenance_ships,
        current_voyages=current_voyages
    )


@app.route("/ships")
def ships_page():

    ships = get_all_ships()


    active_ships = sum(
        1 for ship in ships
        if ship["status"] == "Active"
    )


    at_port_ships = sum(
        1 for ship in ships
        if ship["status"] == "At Port"
    )


    maintenance_ships = sum(
        1 for ship in ships
        if ship["status"] == "Maintenance"
    )


    return render_template(
        "ships.html",
        ships=ships,
        active_ships=active_ships,
        at_port_ships=at_port_ships,
        maintenance_ships=maintenance_ships
    )


@app.route("/crew")
def crew_page():

    crew = get_all_crew()


    on_board_crew = sum(
        1 for member in crew
        if member["status"] == "On Board"
    )


    on_leave_crew = sum(
        1 for member in crew
        if member["status"] == "On Leave"
    )


    return render_template(
        "crew.html",
        crew=crew,
        on_board_crew=on_board_crew,
        on_leave_crew=on_leave_crew
    )

@app.route("/voyages")
def voyages_page():

    voyages = get_all_voyages()


    in_progress_voyages = sum(
        1 for voyage in voyages
        if voyage["voyage_status"] == "In Progress"
    )


    completed_voyages = sum(
        1 for voyage in voyages
        if voyage["voyage_status"] == "Completed"
    )


    scheduled_voyages = sum(
        1 for voyage in voyages
        if voyage["voyage_status"] == "Scheduled"
    )


    return render_template(
        "voyages.html",
        voyages=voyages,
        in_progress_voyages=in_progress_voyages,
        completed_voyages=completed_voyages,
        scheduled_voyages=scheduled_voyages
    )

@app.route("/cargo")
def cargo_page():

    cargo = get_all_cargo()


    delivered_cargo = sum(
        1 for item in cargo
        if item["cargo_status"] == "Delivered"
    )


    in_transit_cargo = sum(
        1 for item in cargo
        if item["cargo_status"] == "In Transit"
    )


    loaded_cargo = sum(
        1 for item in cargo
        if item["cargo_status"] == "Loaded"
    )


    return render_template(
        "cargo.html",
        cargo=cargo,
        delivered_cargo=delivered_cargo,
        in_transit_cargo=in_transit_cargo,
        loaded_cargo=loaded_cargo
    )
@app.route("/fuel")
@app.route("/fuel")
def fuel_page():

    fuel_records = get_all_fuel_records()


    total_fuel_quantity = sum(
        fuel["quantity"] for fuel in fuel_records
    )


    total_fuel_cost = sum(
        fuel["cost"] for fuel in fuel_records
    )


    marine_diesel_records = sum(
        1 for fuel in fuel_records
        if fuel["fuel_type"] == "Marine Diesel Oil"
    )


    heavy_fuel_records = sum(
        1 for fuel in fuel_records
        if fuel["fuel_type"] == "Heavy Fuel Oil"
    )


    return render_template(
        "fuel.html",
        fuel_records=fuel_records,
        total_fuel_quantity=total_fuel_quantity,
        total_fuel_cost=total_fuel_cost,
        marine_diesel_records=marine_diesel_records,
        heavy_fuel_records=heavy_fuel_records
    )


@app.route("/maintenance")
def maintenance_page():

    maintenance = get_all_maintenance()


    completed_maintenance = sum(
        1 for item in maintenance
        if item["maintenance_status"] == "Completed"
    )


    in_progress_maintenance = sum(
        1 for item in maintenance
        if item["maintenance_status"] == "In Progress"
    )


    scheduled_maintenance = sum(
        1 for item in maintenance
        if item["maintenance_status"] == "Scheduled"
    )


    total_maintenance_cost = sum(
        item["cost"] for item in maintenance
    )


    return render_template(
        "maintenance.html",
        maintenance=maintenance,
        completed_maintenance=completed_maintenance,
        in_progress_maintenance=in_progress_maintenance,
        scheduled_maintenance=scheduled_maintenance,
        total_maintenance_cost=total_maintenance_cost
    )