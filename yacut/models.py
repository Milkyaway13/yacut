from datetime import datetime

from flask import url_for

from yacut import db

from .constants import MAX_LENGHT_SHORT_LINK


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(MAX_LENGHT_SHORT_LINK), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for("follow_short_link", short=self.short, _external=True),
        )

    def from_dict(self, data):
        api_column_mapping = {"url": "original", "custom_id": "short"}
        for field in ["url", "custom_id"]:
            setattr(self, api_column_mapping[field], data[field])
