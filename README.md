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


### Pearsons Chi-Squared Test

Pearson's chi-squared test or Pearson's χ2 test is a statistical test applied to sets of categorical data to evaluate how likely it is that any observed difference between the sets arose by chance. It is the most widely used of many chi-squared tests (e.g., Yates, likelihood ratio, portmanteau test in time series, etc.) – statistical procedures whose results are evaluated by reference to the chi-squared distribution. Its properties were first investigated by Karl Pearson in 1900. In contexts where it is important to improve a distinction between the test statistic and its distribution, names similar to Pearson χ-squared test or statistic are used.

## Steps

**Prepare the Data**:
You start with two sets of frequencies: the observed frequencies and the expected frequencies. The observed frequencies are the actual counts you collected from your data. The expected frequencies are the counts you would expect to see if the null hypothesis were true. For example, if you're testing whether a die is fair, the expected frequency for each face of the die would be the same.

**Check the Totals**:
Before proceeding, you need to make sure that the total of the observed frequencies matches the total of the expected frequencies. If they don't match, you must adjust the expected frequencies so that their total equals the total of the observed frequencies. This is done by scaling the expected frequencies proportionally.

**Calculate the Differences**:
For each category, subtract the expected frequency from the observed frequency. This gives you the difference between what you observed and what you expected. Square this difference to make sure it's positive, and then divide it by the expected frequency. This step measures how much each category deviates from what was expected, relative to the expected frequency.

**Sum the Values**:
Add up all the values you calculated in the previous step. This sum is the Pearson Chi-Squared statistic. It represents the overall difference between the observed and expected frequencies across all categories.

**Determine Degrees of Freedom**:
The degrees of freedom depend on the number of categories in your data. For a goodness-of-fit test, the degrees of freedom are calculated as the number of categories minus one. This value is important because it helps determine the critical value or p-value for the test.