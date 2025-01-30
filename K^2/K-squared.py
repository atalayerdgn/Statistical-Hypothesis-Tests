import numpy as np
from scipy.stats import norm, jarque_bera
import math

class K_Squared:
    def __init__(self,x):
        self.x = x
        self.n = len(self.x)
    def calculate_moment(self, k):
        """
        Calculate the k-th moment of the data.
        """
        if k == 1:
            return 0
        elif k == 2:
            return np.var(self.x)
        elif k == 3:
            return np.mean((self.x - np.mean(self.x))**3)
        elif k == 4:
            return np.mean((self.x - np.mean(self.x))**4) 
    def calculate_skewness(self):
        """
        Calculate the skewness of the data.
        """
        return (self.calculate_moment(3)) / (self.calculate_moment(2)**1.5)
    def calculate_kurtosis(self):
        """
        Calculate the kurtosis of the data.
        """
        return (self.calculate_moment(4)) / (self.calculate_moment(2)**2)
    def calculate_excess_kurtosis(self):
        """
        Calculate the excess kurtosis of the data.
        """
        return self.calculate_kurtosis() - 3
    def calculate_transformed_skewness(self):
        """
        Calculate the transformed skewness of the data.
        """
        skewness = self.calculate_skewness()
        correction_factor = (math.sqrt(self.n * (self.n - 1))) / (self.n - 2)
        return skewness * correction_factor
    def calculate_k_squared(self):
        """
        Calculate the K^2 statistic.
        """
        return  (self.n / 6) * (self.calculate_transformed_skewness()**2 + (self.calculate_excess_kurtosis()**2 / 4))
    
def main():
    x = np.random.normal(0, 1, 100)
    k_squared = K_Squared(x)
    print(k_squared.calculate_k_squared())
    print(jarque_bera(x).statistic)

if __name__ == "__main__":
    main()