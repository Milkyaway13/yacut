from flask import flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route("/", methods=["GET", "POST"])
def add_custom_id():
    form = URLForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if not short:
            short = get_unique_short_id()
        elif URLMap.query.filter_by(short=short).first():
            flash("предложенный вариант короткой ссылки уже существует.")
            return render_template("index.html", form=form)
        url_map = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template("index.html", form=form, short=short)
    return render_template("index.html", form=form)


@app.route("/<string:short>")
def follow_short_link(short):
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
