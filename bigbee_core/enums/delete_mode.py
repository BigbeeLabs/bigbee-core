from enum import Enum


class DeleteMode(str, Enum):
    HARD = "hard"
    SOFT = "soft"