import scipy.stats as stats

class ANOVA:
    def __init__(self):
        pass
    def anova_test(self, groups, alpha=0.05):
        """
        Perform one-way ANOVA test on the given groups.
        groups: List of lists of numbers. Each list represents a group.
        alpha: Significance level.
        Returns a dictionary containing the ANOVA table.
        """
        k = len(groups)
        if k < 2:
            raise ValueError("ANOVA requires at least two groups.")
        group_sums = [sum(group) for group in groups]
        group_means = [sum_ / len(group) for sum_, group in zip(group_sums, groups)]
        group_counts = [len(group) for group in groups]
        total_N = sum(group_counts)
        overall_mean = sum(group_sums) / total_N
        ssb = sum(nj * (mj - overall_mean)**2 for nj, mj in zip(group_counts, group_means))
        sse = 0.0
        for i in range(k):
            mean_j = group_means[i]
            sse += sum((x - mean_j)**2 for x in groups[i])
        sst = ssb + sse
        df_between = k - 1
        df_error = total_N - k
        df_total = total_N - 1
        msb = ssb / df_between if df_between != 0 else 0
        mse = sse / df_error if df_error != 0 else 0
        f_value = msb / mse if mse != 0 else 0
        critical_value = stats.f.ppf(1 - alpha, df_between, df_error)
        print("ANOVA Table:")
        print(f"{'Source of Variation':<20} {'Sum of Squares':<15} {'Degrees of Freedom':<18} {'Mean Squares':<12} {'F Value':<10}")
        print(f"{'Between Groups':<20} {ssb:<15.4f} {df_between:<18} {msb:<12.4f} {f_value:<10.4f}")
        print(f"{'Error':<20} {sse:<15.4f} {df_error:<18} {mse:<12.4f} {'':<10}")
        print(f"{'Total':<20} {sst:<15.4f} {df_total:<18} {'':<12} {'':<10}")
        print(f"\nCritical Value at α={alpha:.2f}: {critical_value:.4f}")
        return {
            'SSB': ssb,
            'SSE': sse,
            'SST': sst,
            'df_between': df_between,
            'df_error': df_error,
            'df_total': df_total,
            'MSB': msb,
            'MSE': mse,
            'F_value': f_value,
            'critical_value': critical_value
        }


def main():
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    anova = ANOVA()
    print(anova.anova_test(arr))

if __name__ == '__main__':
    main()
