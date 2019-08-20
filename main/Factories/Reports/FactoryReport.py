from main.Factories.Reports.ReportAggUser.ReportAggUser import ReportAggUser


class FactoryReport:
    """ Factory specific report class """

    def __init__(self,report,conf,logger):
        self.report=report
        self.conf=conf
        self.logger=logger

    def build(self):
        if self.report == "report_agg_user" : return ReportAggUser(self.conf,self.logger)