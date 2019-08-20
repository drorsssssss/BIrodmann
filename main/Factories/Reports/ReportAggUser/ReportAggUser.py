import json
import main.DataModel.ColumnFunctions as cf
import main.DataModel.AggFunctions as af
from main.DataModel.Columns import SourceColumns,CalcColumns
import main.Helpers.DataframeHelpers as dfh
from main.Factories.Reports.IReporting import IReporting
from main.Factories.Persistence.FactoryPersistDF import FactoryPersistDF
from main.Helpers.RequestsHelper import download_multiple_files_from_url
from main.Helpers.FilesHelpers import clear_folder


class ReportAggUser(IReporting):
    def __init__(self,conf,logger):
        self.conf=conf
        self.logger=logger

    def execute(self):

        input_path = self.conf.get_string("App.Reports.input_path")
        filter_columns_json = json.loads(self.conf.get_string("App.Reports.filter_columns_json"))
        agg_time_resolution=self.conf.get_string("App.Reports.agg_time_resolution")
        topn=self.conf.get_int("App.Reports.topn")
        persist_target=self.conf.get_string("App.Reports.persist.target")
        should_download = self.conf.get_bool("App.Reports.download_files.is_active")
        urls = self.conf.get_list("App.Reports.download_files.urls")
        concurrency_level = self.conf.get_int("App.Reports.download_files.concurrency_level")
        clear_input_path = self.conf.get_bool("App.Reports.download_files.clear_input_path")

        self.logger.info("Start executing report Agg User")
        self.logger.info(f"Clear input path: {clear_input_path}")
        clear_folder(input_path) if clear_input_path else None
        self.logger.info(f"Download files: {should_download}")
        download_multiple_files_from_url(urls,input_path,concurrency_level) if should_download else None
        projected_columns=f"{SourceColumns.ID.value},{SourceColumns.CREATED_AT.value}"
        df = dfh.create_pandas_df(input_path,projected_columns=projected_columns,filter_columns=filter_columns_json)
        if df.empty:
            self.logger.info(f"There is no data to calculate. Please check your filter or files.")
            return
        func = cf.col_created_at_to_resolution(agg_time_resolution)
        df = dfh.add_columns_pandas_df(df,CalcColumns.RESOLUTION.value,func)
        df = af.aggregate(df,[CalcColumns.RESOLUTION.value,SourceColumns.ID.value],af.AggBaseFunc.COUNT.value)
        df = cf.rename_pandas_cols(df,[CalcColumns.RESOLUTION.value,SourceColumns.ID.value,CalcColumns.COUNT.value])
        df = af.groupby_sort(df,CalcColumns.RESOLUTION.value,[CalcColumns.COUNT.value],ascending=False)
        df = af.groupby_limit(df,CalcColumns.RESOLUTION.value,topn)
        FactoryPersistDF(df,persist_target, self.conf, self.logger).build().persist()
        self.logger.info(f"Persist report: {persist_target}")
        self.logger.info("End executing report Agg User")



