from enum import Enum


class TimeoutVariables(Enum):
    """
    Class contains time values
    """

    IMPLICIT_WAIT = 50
    EXPLICIT_WAIT = 100


class Urls(Enum):
    """
    Class contains base urls
    """

    HOME_PAGE = "http://localhost:3000/home"
