from statsmodels.tsa.stattools import adfuller
import numpy as np


class ADF:
    def __init__(self,x):
        self.x = x
        self.length = len(self.x)
    