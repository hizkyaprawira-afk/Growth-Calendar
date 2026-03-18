from .classification import *
from .regression import *
from .clustering import *

__all__ = [
    #classification
    "SVM",
    "KNN",
    "XGBoostClassifier",
    "LogisticRegression",
     
    #regression
    "LinearRegression",
    "SVR",
    "XGBoostRegressor",
    
    #clustering
    "KMeans",
    "HierarchicalClustering",
    "Cmeans",
]
    