import abc


class IGraphs(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        pass