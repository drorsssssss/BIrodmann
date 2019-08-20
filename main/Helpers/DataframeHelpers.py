import pandas as pd
import os
import logging

def add_columns_pandas_df(df, new_col, func):
    """ Add new column based on func logic"""
    dict_col_spec = {new_col:func}
    return df.assign(**dict_col_spec)


def filter_pandas_df(df, filters):
    """Filter DataFrame using dictionary of filters."""
    return df[(df[list(filters)] == pd.Series(filters)).all(axis=1)]


def create_pandas_df(path, projected_columns=None, filter_columns=None, chunksize=100000):
    """ Create a pandas dataframe from multiple files"""

    df_chunks=[]
    for file in os.listdir(path):
        try:
            df_iterator = pd.read_json(path+file,lines=True,chunksize=chunksize)
            for chunk in df_iterator:
                if filter_columns is not None and filter_columns != {}:
                    chunk = filter_pandas_df(chunk,filter_columns)
                if projected_columns is not None:
                    chunk = chunk[projected_columns.split(',')]

                df_chunks.append(chunk)
                logging.info(f"File {file} is loaded successfully!")

        except Exception as e:
            logging.error(f"Error in file: {file}",exc_info=True)

    df_chunks=pd.concat(df_chunks).reset_index(drop=True)
    return df_chunks

