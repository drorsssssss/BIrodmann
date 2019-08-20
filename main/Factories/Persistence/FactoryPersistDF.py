from main.Factories.Persistence.LocalFS import PersistLocalFS
from main.Factories.Persistence.PersistEnums import PersistTargets


class FactoryPersistDF:
    """ Factory specific persist class """

    def __init__(self,df,target,conf,logger):
        self.df=df
        self.target=target
        self.conf=conf
        self.logger=logger

    def build(self):
        if self.target == PersistTargets.LOCAL.value : return PersistLocalFS(self.df,self.conf,self.logger)