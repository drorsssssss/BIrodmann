""" Aggregate functions based on pandas dataframe """

from enum import Enum


class AggBaseFunc(Enum):
    COUNT="count"
    MIN="min"
    MAX="max"


def aggregate(df, groupby_cols, func):
    """ Return a dataframe based on group by columns and aggregate function """
    return getattr(df.groupby(groupby_cols,as_index=False),func)()


def groupby_sort(df,groupby_cols,sort_cols,ascending=True):
    """ Return a dataframe, each group is sorted by input columns """
    df=df.groupby(groupby_cols).apply(lambda x: x.sort_values(sort_cols, ascending = ascending)).reset_index(drop=True)
    return df


def groupby_limit(df,groupby_cols,limit):
    """ Return a dataframe, each group of rows will be limit by the limit variable """
    return df.groupby(groupby_cols).head(limit).reset_index(drop=True)
