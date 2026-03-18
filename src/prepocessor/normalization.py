import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from typing import Tuple
import logging
import warnings


class Normalizer:
    @staticmethod
    def standard(data, col):
        df = data.copy()
        scaler = StandardScaler()
        df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))
        return df
    
    @staticmethod
    def minmax(data, col):
        df = data.copy()
        scaler = MinMaxScaler()
        df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))
        return df