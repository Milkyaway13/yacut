from http import HTTPStatus

from flask import jsonify, request

from yacut import app, db

from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import validate_create_id


@app.route("/api/id/<string:short_id>/", methods=["GET"])
def get_original(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage("Указанный id не найден", HTTPStatus.NOT_FOUND)
    return jsonify({"url": url_map.original}), HTTPStatus.OK


@app.route("/api/id/", methods=["POST"])
def create_id():
    data = request.get_json()
    validate_create_id(data)
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED
