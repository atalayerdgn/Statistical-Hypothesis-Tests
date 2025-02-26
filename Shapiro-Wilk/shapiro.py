
import numpy as np
from scipy.stats import norm, shapiro

class Shapiro_Wilk:
    def __init__(self, x):
        self.x = x
        self.n = len(self.x)
        self.mean = np.mean(self.x)
        self.sorted = np.sort(self.x)

    def shapiro_wilk_coefficients(self):
        """
        Calculate the coefficients for the Shapiro-Wilk test.
        n = number of samples
        a = coefficients
        n 3 to 20 if u want to calculate for more than 20 samples to 50 samples https://real-statistics.com/statistics-tables/shapiro-wilk-table/
        """
        a = {
            3: [0.7071],
            4: [0.6872, 0.1677],
            5: [0.6646, 0.2413],
            6: [0.6431, 0.2806, 0.0875],
            7: [0.6233, 0.3031, 0.1401],
            8: [0.6052, 0.3244, 0.1976, 0.0947],
            9: [0.5888, 0.3244, 0.1976, 0.0947],
            10: [0.5739, 0.3291, 0.2141, 0.1224, 0.0399],
            11: [0.5601, 0.3315, 0.2260, 0.1429, 0.0695],
            12: [0.5475, 0.3325, 0.2347, 0.1586, 0.0922, 0.0303],
            13: [0.5359, 0.3325, 0.2412, 0.1707, 0.1099, 0.0539],
            14: [0.5251, 0.3318, 0.2460, 0.1802, 0.1240, 0.0727, 0.0240],
            15: [0.5150, 0.3306, 0.2495, 0.1878, 0.1353, 0.0880, 0.0433],
            16: [0.5056, 0.3290, 0.2521, 0.1939, 0.1447, 0.1005, 0.0593, 0.0196],
            17: [0.4968, 0.3273, 0.2540, 0.1988, 0.1524, 0.1109, 0.0725, 0.0359],
            18: [0.4886, 0.3253, 0.2553, 0.2027, 0.1587, 0.1197, 0.0837, 0.0496, 0.0163],
            19: [0.4808, 0.3232, 0.2561, 0.2059, 0.1641, 0.1271, 0.0932, 0.0612, 0.0303],
            20: [0.4734, 0.3211, 0.2565, 0.2085, 0.1686, 0.1334, 0.1013, 0.0711, 0.0422, 0.0140],
        }
        if self.n < 3 or self.n > 20:
            raise ValueError("Sample size must be between 3 and 20.")
        return a[self.n]

    def calculate_b(self):
        """
        Calculate the b coefficient for the Shapiro-Wilk test.
        """
        a = self.shapiro_wilk_coefficients()
        b = 0
        for i in range(len(a)):
            b += a[i] * (self.sorted[self.n - i - 1] - self.sorted[i])
        return b

    def calculate_variance(self):
        """
        Calculate the variance
        """
        return np.var(self.x, ddof=1)

    def calculate_w(self):
        """
        Calculate the W statistic
        """
        b = self.calculate_b()
        s_squared = self.calculate_variance()
        w = (b ** 2) / ((self.n - 1) * s_squared)
        return w


    def shapiro_test(self):
        """
        Perform the Shapiro-Wilk test
        """
        w = self.calculate_w()
        return w


def main():
    x = [78, 85, 92, 88, 76, 95, 89, 81, 84, 90]
    shapiro_ = Shapiro_Wilk(x)
    w = shapiro_.shapiro_test()
    print(f"Calculated W statistic: {w:.4f}")

    # Compare with scipy's shapiro
    w_scipy, p_scipy = shapiro(x)
    print(f"Scipy W statistic: {w_scipy:.4f}")


if __name__ == "__main__":
    main()
