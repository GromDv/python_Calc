from abc import ABCMeta, abstractmethod


class Operation():
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, view):
        """Выполнить операцию"""
