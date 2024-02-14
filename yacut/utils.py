from random import choice
from re import match
from string import ascii_letters, digits

from .constants import CUSTOM_LINK_REGEX_PATTERN, SHORT_LINK_LENGTH, URL_REGEX_PATTERN
from .error_handlers import InvalidAPIUsage
from .models import URLMap


def get_unique_short_id(length=SHORT_LINK_LENGTH):
    letters_digits = ascii_letters + digits
    random_string = "".join(choice(letters_digits) for _ in range(length))
    return random_string


def validate_create_id(data):
    if data is None:
        raise InvalidAPIUsage("Отсутствует тело запроса")
    if "url" not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if not match(URL_REGEX_PATTERN, data["url"]):
        raise InvalidAPIUsage("Указан недопустимый URL")
    if not data.get("custom_id"):
        data["custom_id"] = get_unique_short_id()
    # Всё таки эта проверка нужна, без нее тесты падают
    if not match(CUSTOM_LINK_REGEX_PATTERN, data["custom_id"]):
        raise InvalidAPIUsage("Указано недопустимое имя для короткой ссылки")
    if URLMap.query.filter_by(short=data["custom_id"]).first():
        raise InvalidAPIUsage("Предложенный вариант короткой ссылки уже существует.")
