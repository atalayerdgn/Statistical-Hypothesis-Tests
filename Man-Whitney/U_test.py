import numpy as np
from scipy.stats import rankdata

class WhitneyU:
    """
    A class to compute the Mann-Whitney U statistic and multi-class AUC M measure.
    """

    def __init__(self):
        pass

    def mann_whitney_auc(self, X, Y):
        """
        Computes the Mann-Whitney U statistic and AUC value for two groups.

        Parameters:
        X (array-like): Samples from group 1.
        Y (array-like): Samples from group 2.

        Returns:
        float: AUC value.
        """
        n1 = len(X)
        n2 = len(Y)
        if n1 == 0 or n2 == 0:
            return 0.0

        combined = np.concatenate([X, Y])
        ranks = rankdata(combined)
        R1 = np.sum(ranks[:n1])
        R2 = np.sum(ranks[n1:])

        U1 = n1 * n2 + (n1 * (n1 + 1)) / 2 - R1
        auc = U1 / (n1 * n2)

        return auc

    def multi_class_auc_m_measure(self, y_true, y_probs):
        """
        Computes the multi-class AUC M measure for a classifier.

        Parameters:
        y_true (array-like): True class labels.
        y_probs (array-like): Predicted probabilities for each class (n_samples, n_classes).

        Returns:
        float: M measure.
        """
        classes = np.unique(y_true)
        c = len(classes)
        if c < 2:
            raise ValueError("At least 2 classes are required.")

        total = 0.0
        for k in classes:
            for l in classes:
                if k == l:
                    continue
                mask = np.logical_or(y_true == k, y_true == l)
                y_true_subset = y_true[mask]
                y_probs_subset = y_probs[mask, k]

                X = y_probs_subset[y_true_subset == k]
                Y = y_probs_subset[y_true_subset == l]

                if len(X) == 0 or len(Y) == 0:
                    continue 

                auc = self.mann_whitney_auc(X, Y)
                total += auc

        m = total / (c * (c - 1))
        return m


if __name__ == "__main__":
    # Two-group example
    X = np.array([1, 2, 3])
    Y = np.array([4, 5, 6])
    whitney_u = WhitneyU()
    print("Two-group AUC:", whitney_u.mann_whitney_auc(X, Y))

    # Multi-class example
    y_true = np.array([0, 0, 1, 1, 2, 2])
    y_probs = np.array([
        [0.7, 0.2, 0.1],
        [0.6, 0.3, 0.1],
        [0.1, 0.8, 0.1],
        [0.2, 0.7, 0.1],
        [0.1, 0.2, 0.7],
        [0.2, 0.3, 0.5]
    ])
    print("Multi-class M measure:", whitney_u.multi_class_auc_m_measure(y_true, y_probs))
