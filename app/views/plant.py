from flask import Blueprint, request, flash, redirect, url_for, render_template
from app.forms.plant import CreateForm, ProfileForm
from app.models.plant import Plant

plant_blueprint = Blueprint("plant", __name__)


@plant_blueprint.route("/plant/create_plant", methods=["GET", "POST"])
def create_plant():
    form = CreateForm(request.form)
    if form.validate_on_submit():
        plant = Plant(
            plant_name=form.plant_name.data,
            location=form.location.data,
        )
        plant.save()
        flash("Registration plant is successful.", "success")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("plant/create_plant.html", form=form)


@plant_blueprint.route("/plant/all_plants", methods=["GET", "POST"])
def all_plants():
    plants: Plant = Plant.query.all()
    form = ProfileForm()
    return render_template("plant/all_plants.html", form=form, plants=plants)
