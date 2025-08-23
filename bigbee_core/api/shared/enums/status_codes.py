# api/shared/enums/status_codes.py

from enum import IntEnum

class StatusCode(IntEnum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409
    UNPROCESSABLE = 422
    INTERNAL_ERROR = 500