from scipy.stats import pearsonr
import numpy as np


class PearsonsCorrelationCoefficient:
    def __init__(self,x,y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.nx = len(self.x)
        self.ny = len(self.y)
    def calculate_covariance(self):
        """
        Calculate the covariance of the data.
        """
        return np.mean((self.x - np.mean(self.x)) * (self.y - np.mean(self.y)))
    def calculate_correlation(self):
        """
        Calculate the correlation of the data.
        """
        return self.calculate_covariance() / (np.std(self.x) * np.std(self.y))
    

def main():
    x = np.random.normal(0, 1, 100)
    y = np.random.normal(0, 1, 100)
    pcc = PearsonsCorrelationCoefficient(x,y)
    print(pcc.calculate_correlation())
    print(pearsonr(x,y)[0])

if __name__ == "__main__":
    main()