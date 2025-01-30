# Statistical Hypothesis Tests

## Statistical Hypothesis Tests using Python

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
