# Statistical Hypothesis Tests

## Statistical Hypothesis Tests using Python

### Shapiro-Wilk Test

The Shapiro–Wilk test is a test of normality. It was published in 1965 by Samuel Sanford Shapiro and Martin Wilk. The test evaluates the null hypothesis that a given sample \( x_1, x_2, ..., x_n \) originates from a normally distributed population.

### Shapiro-Wilk Test Statistic Calculation

To calculate the Shapiro-Wilk test statistic \( W \), follow the procedure below:

#### Procedure

1. **Sort the Sample:**
   - Given a sample of size \( n \): \( x_1, x_2, \dots, x_n \).
   - Sort the sample in increasing order to obtain \( y_1, y_2, \dots, y_n \), where \( y_1 < y_2 < \dots < y_n \).

2. **Calculate the Sum \( b \):**
   - **If \( n \) is even:**
     - Compute \( b \) using \( k = \frac{n}{2} \):
       
       \[
       b = \sum_{i=1}^{k} a_{n-i+1} (y_{n-i+1} - y_i)
       \]
   - **If \( n \) is odd:**
     - Compute \( b \) using \( k = \frac{n-1}{2} \).
     - **Note:** The median must not be included in the calculation.
   
   The coefficients \( a_{n-i+1} \) depend on the sample size \( n \) and can be obtained from the table published by Shapiro and Wilk.

3. **Calculate the Test Statistic \( W \):**
   
   \[
   W = \frac{b^2}{S^2}
   \]
   
   where \( S^2 \) is the sample variance.

4. **Interpret the Result:**
   - Compare the calculated \( W \) with the critical threshold from the Shapiro-Wilk table.
   - If \( W \) is smaller than the critical threshold, the assumption of a normal distribution is rejected.

### Notes
- Ensure you refer to the Shapiro-Wilk table for the correct coefficients \( a_{n-i+1} \) and critical thresholds.
- This test is commonly used to assess the normality of a dataset.
