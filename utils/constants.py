from enum import Enum


class TimeoutVariables(Enum):
    IMPLICIT_WAIT = 50
    EXPLICIT_WAIT = 100


class Urls(Enum):
    HOME_PAGE = "http://localhost:3000/home"
