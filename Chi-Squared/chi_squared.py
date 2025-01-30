from scipy.stats import chisquare
import numpy as np


class ChiSquared:
    def __init__(self, observed, expected):
        self.observed = observed
        self.expected = expected
        if np.shape(self.observed) != np.shape(self.expected):
            raise ValueError("Observed and expected arrays must have the same shape.")

    def calculate_o_e(self):
        """
        Calculate the (O-E)^2 / E values.
        """
        return (self.observed - self.expected)**2 / self.expected

    def calculate_df(self):
        """
        Calculate the degrees of freedom.
        """
        return len(self.observed) - 1

    def calculate_chi_squared(self):
        """
        Calculate the chi-squared statistic and degrees of freedom.
        """
        df = self.calculate_df()
        chi2 = np.sum(self.calculate_o_e())
        return df, chi2


def main():
    observed = np.array([10, 5, 2, 8, 9])
    expected = np.array([10, 10, 10, 10, 10])

    scale_factor = np.sum(observed) / np.sum(expected)
    expected_scaled = expected * scale_factor

    chi_squared = ChiSquared(observed, expected_scaled)
    df, chi2 = chi_squared.calculate_chi_squared()
    print(f"Chi-squared: {chi2}")

    chi2_stat, p_value = chisquare(observed, expected_scaled)
    print(f"Scipy Chi-squared: {chi2_stat}")

if __name__ == "__main__":
    main()