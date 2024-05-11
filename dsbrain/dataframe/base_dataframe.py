from abc import ABC, abstractmethod
from ..llm.base_llm import DSBrainLLM



class DSBrainDataFrame(ABC):

    def __init__(self, llm: DSBrainLLM):
        self.llm = llm

    @property
    @abstractmethod
    def df(self):
        pass

    @property
    @abstractmethod
    def column_names(self):
        pass

    @abstractmethod
    def summary(self):
        '''
        Produces a general summary about the dataframe
        '''
        pass