from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (
    URL,
    DataRequired,
    Length,
    Optional,
    Regexp,
    ValidationError,
)

from .constants import (
    CUSTOM_LINK_EXISTS_MESSAGE,
    CUSTOM_LINK_VALIDATION_MESSAGE,
    MAX_LENGHT_SHORT_LINK,
    MIN_LENGHT_SHORT_LINK,
    REQUIRED_FIELD_MESSAGE,
    SUBMIT_BUTTOM_TEXT,
    URL_VALIDATION_MESSAGE,
)
from .models import URLMap


class URLForm(FlaskForm):
    original_link = URLField(
        "Укажите свою ссылку",
        validators=(
            DataRequired(message=REQUIRED_FIELD_MESSAGE),
            URL(require_tld=True, message=URL_VALIDATION_MESSAGE),
        ),
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=(
            Length(MIN_LENGHT_SHORT_LINK, MAX_LENGHT_SHORT_LINK),
            Optional(),
            Regexp(r"^[A-Za-z0-9]+$", message=CUSTOM_LINK_VALIDATION_MESSAGE),
        ),
    )
    submit = SubmitField(SUBMIT_BUTTOM_TEXT)

    def validate_custom_id(self, field):
        """Метод проверки уникальности поля."""
        if field.data and URLMap.query.filter_by(short=field.data).first():
            raise ValidationError(CUSTOM_LINK_EXISTS_MESSAGE)
