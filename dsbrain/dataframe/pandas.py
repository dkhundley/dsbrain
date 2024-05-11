from base_dataframe import DSBrainDataFrame

import pandas as pd



class DSBrainPandasDataFrame(DSBrainDataFrame):

    def __init__(self, llm, df: pd.DataFrame):
        super().__init__(llm)
        self.df = df

    def summary(self):
        pass