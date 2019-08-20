from main.Factories.Reports.ReportAggUser.ReportAggUser import ReportAggUser
from main.Factories.Reports.ReportEnums import ReportNames

class FactoryReport:
    """ Factory specific report class """

    def __init__(self,report,conf,logger):
        self.report=report
        self.conf=conf
        self.logger=logger

    def build(self):
        if self.report == ReportNames.AGGUSER.value : return ReportAggUser(self.conf,self.logger)