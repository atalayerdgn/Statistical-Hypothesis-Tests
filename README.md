# Statistical Hypothesis Tests

# NORMALİTY TESTS

### Shapiro-Wilk Test

The Shapiro–Wilk test is a statistical test used to determine whether a given dataset follows a normal distribution. It was introduced in 1965 by Samuel Sanford Shapiro and Martin Wilk. The test evaluates the null hypothesis that a sample comes from a normally distributed population.

### Steps to Perform the Shapiro-Wilk Test

1. **Sort the Sample:**
   - Arrange the data in ascending order.

2. **Compute the Test Statistic:**
   - Use specific coefficients based on the sample size to calculate the test statistic.
   - The calculation involves the ordered data values and their expected values if they were normally distributed.

3. **Determine the Sample Variance:**
   - Compute how much the data deviates from its mean.

4. **Compare with Critical Values:**
   - The test statistic is compared with critical values from the Shapiro-Wilk table.
   - If the statistic is below the threshold, the normality assumption is rejected.

### Interpretation
- If the test statistic is high, the data is likely to be normally distributed.
- If the test statistic is low, the data deviates significantly from a normal distribution, and the normality assumption is rejected.

### Notes
- The test is widely used to assess whether a dataset follows a normal distribution before applying parametric statistical methods.
- The coefficients used in the calculation are predetermined based on the sample size and are referenced from statistical tables.

# K-Squared Statistic Calculation
## Description

K2 test, named for Ralph D'Agostino, is a goodness-of-fit measure of departure from normality, that is the test aims to gauge the compatibility of given data with the null hypothesis that the data is a realization of independent, identically distributed Gaussian random variables. The test is based on transformations of the sample kurtosis and skewness, and has power only against the alternatives that the distribution is skewed and/or kurtic.

## Steps

**Compute Moments**:

* Calculate the second, third, and fourth central moments of the dataset.

**Calculate Skewness and Kurtosis**:

* Compute the skewness using the third moment and standard deviation.

* Compute the kurtosis using the fourth moment and variance.

**Determine Excess Kurtosis**:

* Subtract 3 from the computed kurtosis to get excess kurtosis.

**Transform Skewness**:

* Apply a correction factor based on the sample size to the skewness.

**Compute the K² Statistic**

**Interpret Results**:

* Compare the K² statistic with a critical value or p-value to determine normality.

# Correlation Tests


### Pearson Correlation Coefficient


In statistics, the Pearson correlation coefficient (PCC)[a] is a correlation coefficient that measures linear correlation between two sets of data. It is the ratio between the covariance of two variables and the product of their standard deviations; thus, it is essentially a normalized measurement of the covariance, such that the result always has a value between −1 and 1. As with covariance itself, the measure can only reflect a linear correlation of variables, and ignores many other types of relationships or correlations. As a simple example, one would expect the age and height of a sample of children from a primary school to have a Pearson correlation coefficient significantly greater than 0, but less than 1 (as 1 would represent an unrealistically perfect correlation).

## Steps

**Find covariance**

   - Calculate the covariance between X and Y

**Calculate Standart deviation of X**

**Calculate Standart deviation of Y**

**Calculate the Pearson's Correlation Coeff**

