import abc


class IReporting(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        pass