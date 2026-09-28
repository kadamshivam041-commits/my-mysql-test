import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, render_template

from database.operations import (
    get_dashboard_stats,
    get_fleet_status_report,
    get_all_ships,
    get_all_crew,
    get_all_voyages,
    get_all_cargo,
    get_all_fuel_records,
    get_all_maintenance
)


app = Flask(__name__)

@app.route("/fleet")
def fleet():

    ships = get_all_ships()

    return render_template(
        "fleet.html",
        ships=ships
    )
@app.route("/crew")
def crew():

    crew_members = get_all_crew()

    return render_template(
        "crew.html",
        crew=crew_members
    )

@app.route("/voyages")
def voyages():

    voyage_list = get_all_voyages()

    return render_template(
        "voyages.html",
        voyages=voyage_list
    )

@app.route("/cargo")
def cargo():

    cargo_list = get_all_cargo()

    return render_template(
        "cargo.html",
        cargo=cargo_list
    )
@app.route("/fuel")
def fuel():

    fuel_records = get_all_fuel_records()

    return render_template(
        "fuel.html",
        fuel_records=fuel_records
    )


@app.route("/maintenance")
def maintenance():

    maintenance_records = get_all_maintenance()

    return render_template(
        "maintenance.html",
        maintenance_records=maintenance_records
    )


@app.route("/")
def home():

    stats = get_dashboard_stats()

    fleet_status = get_fleet_status_report()

    return render_template(
        "dashboard.html",
        stats=stats,
        fleet_status=fleet_status
    )

@app.route("/reports")
def reports():

    stats = get_dashboard_stats()

    fleet_status = get_fleet_status_report()

    return render_template(
        "reports.html",
        stats=stats,
        fleet_status=fleet_status
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )