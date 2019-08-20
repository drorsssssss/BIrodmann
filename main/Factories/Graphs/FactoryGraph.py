from main.Factories.Graphs.UserCountsEvents.UserCountEvents import UserCountEvents
from main.Factories.Graphs.GraphEnums import GraphNames


class FactoryGraph:
    """ Factory specific graph class """

    def __init__(self,graph,conf,logger):
        self.report=graph
        self.conf=conf
        self.logger=logger

    def build(self):
        if self.report == GraphNames.USER_COUNT_EVENTS.value : return UserCountEvents(self.conf,self.logger)