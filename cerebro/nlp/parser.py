import pandas as pd


class DataSetParser(object):
    def __init__(self, path):
        self.df = None
        self.path = path

    def parse(self):
        self.df = pd.read_csv(self.path)

    def get_column_data(self, name):
        # Retried features and Labels column
        return list(self.df[name])
