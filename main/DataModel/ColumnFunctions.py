""" Pandas column functions"""
from main.DataModel.Columns import SourceColumns


def rename_pandas_cols(df,columns):
    """ Rename pandas dataframe columns"""
    df.columns = columns
    return df


"""  Custom Funcs """


def col_created_at_to_resolution(time_resolution):
    """ Convert created_at column to new time_resolution (hour,month,year) """
    return lambda x: getattr(x[SourceColumns.CREATED_AT.value].dt,time_resolution)

