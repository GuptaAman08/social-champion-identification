import pandas as pd
import pickle
import numpy as np

class Ranking:
    def __init__(self, ranks):
        self.dataframe = pd.DataFrame(ranks)
        filters = ['influence', 'moiScore', 'topic_relevance']
        for filter in filters:
            self.dataframe = self.normalize(self.dataframe, filter)

    @staticmethod
    def normalize(df, column):
        df = pd.DataFrame(df)
        max = df[column].max()
        min = 0
        df[column] = (df[column] - min) / (max - min)
        return df

    def rank(self, filters=['influence', 'moiScore', 'topic_relevance']):
        weightages = {}
        rank = []
        self.dataframe['rank'] = 0
        for filter in filters:
            weightages[filter] = 1 / 3
            self.dataframe['rank'] += self.dataframe[filter] * weightages[filter]
        self.dataframe = self.dataframe.sort_values(['rank'], ascending=0)