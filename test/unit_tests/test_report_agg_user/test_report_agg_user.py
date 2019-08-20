import pytest
from pandas.util.testing import assert_frame_equal
import main.Helpers.DataframeHelpers as dfh
import main.DataModel.AggFunctions as af
import main.DataModel.ColumnFunctions as cf
from main.DataModel.Columns import SourceColumns,CalcColumns
from main.Factories.Persistence.FactoryPersistDF import FactoryPersistDF
from main.Helpers.FilesHelpers import clear_folder
from main.Helpers.RequestsHelper import download_multiple_files_from_url
from pyhocon import ConfigFactory
import pandas as pd
import json
import logging
import os
from httmock import urlmatch, HTTMock

BASE_PATH="/Users/dsivan"


def test_create_pandas_df():
    source_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/create_pandas_df/source/"
    target_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/create_pandas_df/target/create_df.csv"
    projected_columns=f"{SourceColumns.ID.value},{SourceColumns.CREATED_AT.value}"
    filter_columns_json = json.loads("""{"type":"CommitCommentEvent"}""")

    target_df = pd.read_csv(target_path,parse_dates = ['created_at'])
    source_df = dfh.create_pandas_df(source_path,projected_columns=projected_columns,filter_columns=filter_columns_json)
    assert_frame_equal(target_df,source_df)


def test_add_columns_pandas_df():
    source_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/add_columns_pandas_df/source/create_df.csv"
    target_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/add_columns_pandas_df/target/add_column.csv"
    df_source_raw=pd.read_csv(source_path,parse_dates = ['created_at'])
    source_df=dfh.add_columns_pandas_df(df_source_raw,"hour",lambda x: getattr(x[SourceColumns.CREATED_AT.value].dt,"hour"))
    target_df=pd.read_csv(target_path,parse_dates = ['created_at'])
    assert_frame_equal(target_df,source_df)


def test_aggregate():
    source_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/aggregate/source/add_column.csv"
    target_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/aggregate/target/aggregate.csv"
    df_source_raw=pd.read_csv(source_path,parse_dates = ['created_at'])
    groupby_cols=["hour",SourceColumns.ID.value]
    source_df=af.aggregate(df_source_raw,groupby_cols,"count")
    target_df=pd.read_csv(target_path)
    assert_frame_equal(target_df,source_df)


def test_rename_pandas_cols():
    source_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/rename_pandas_cols/source/aggregate.csv"
    target_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/rename_pandas_cols/target/rename.csv"
    df_source_raw=pd.read_csv(source_path)
    columns=["hour",SourceColumns.ID.value,CalcColumns.COUNT.value]
    source_df=cf.rename_pandas_cols(df_source_raw,columns)
    target_df=pd.read_csv(target_path)
    assert_frame_equal(target_df,source_df)


def test_groupby_sort():
    source_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/groupby_sort/source/rename.csv"
    target_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/groupby_sort/target/groupby_sort.csv"
    df_source_raw=pd.read_csv(source_path)
    source_df=af.groupby_sort(df_source_raw,"hour","count",ascending=False)
    target_df=pd.read_csv(target_path)
    assert_frame_equal(target_df,source_df)


def test_groupby_limit():
    source_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/groupby_limit/source/groupby_sort.csv"
    target_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/groupby_limit/target/groupby_limit.csv"
    df_source_raw=pd.read_csv(source_path)
    source_df=af.groupby_limit(df_source_raw,"hour",2)
    target_df=pd.read_csv(target_path)
    assert_frame_equal(target_df,source_df)


def test_factory_persist_local():
    source_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/factory_persist_local/source/groupby_limit.csv"
    conf_file=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/factory_persist_local/conf/conf.conf"
    conf=ConfigFactory.parse_file(conf_file)
    source_df=pd.read_csv(source_path)
    FactoryPersistDF(source_df,"local",conf,logging.getLogger(__name__)).build().persist()
    target_df=pd.read_csv(conf.get_string("App.Reports.persist.path"))
    assert_frame_equal(target_df,source_df)


def test_clear_folder():
    source_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/clear_folder/source/"
    file_name="clear_folder.csv"
    with open(source_path+file_name,"w") as file:
        file.write("test")
    clear_folder(source_path)
    assert len(os.listdir(source_path)) == 0


def test_download_multiple_files_from_url():

    @urlmatch(netloc=r'(.*\.)?brodmann\.com$')
    def url_mock(url, request):
        return '{"company":"brodmann"}'
    urls=['http://brodmann.com/']
    target_path=f"{BASE_PATH}/Brodmann/BIrodmann/test/unit_test_files/download_multiple_files_from_url/target/target.json"
    with HTTMock(url_mock):
        download_multiple_files_from_url(urls,target_path,concurrency_level=1)

    with open(target_path) as file:
        result = file.readlines()
    source_file=json.loads("""{"company":"brodmann"}""")
    target_file=json.loads(result[0])
    assert str(source_file) == str(target_file)


pytest.main(['-rA'])
