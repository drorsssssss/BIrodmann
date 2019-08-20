from main.Factories.Graphs.IGraphs import IGraphs
from main.DataModel.Columns import SourceColumns,CalcColumns
import matplotlib.pyplot as plt
import pandas as pd


class UserCountEvents(IGraphs):
    def __init__(self,conf,logger):
        self.conf=conf
        self.logger=logger

    def execute(self):
        self.logger.info("Start sketching user_count_events graph")
        result_report_path=self.conf.get_string("App.Graphs.input_path")
        output_graph_path=self.conf.get_string("App.Graphs.output_path")

        df = pd.read_csv(result_report_path)
        columns=f"{CalcColumns.RESOLUTION.value},{SourceColumns.ID.value}"
        df=df.groupby(columns.split(",")).sum()
        res=df.plot.bar()
        fig=res.get_figure()
        fig.savefig(output_graph_path)
        plt.show()
        self.logger.info("End sketching user_count_events graph")