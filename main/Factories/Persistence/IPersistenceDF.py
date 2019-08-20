import abc


class IPersistence(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def persist(self):
        pass

