""" Data Model Columns"""


from enum import Enum

""" Source columns"""


class SourceColumns(Enum):
    ID="id"
    TYPE="type"
    ACTOR="actor"
    REPO="repo"
    PAYLOAD="payload"
    PUBLIC="public"
    CREATED_AT="created_at"
    ORG="org"


""" Calculated columns"""


class CalcColumns(Enum):
    COUNT="count"
    HOUR="hour"
    RESOLUTION="resolution"






