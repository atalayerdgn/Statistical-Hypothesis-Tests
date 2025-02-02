import numpy as np
from scipy import stats
from scipy.stats import t
from scipy.stats import ttest_1samp as t1s


class T_test:
    def __init__(self,x):
        self.x = x
        self.mean = np.mean(x)
        self.std = np.std(x)
        self.n = len(x)
        self.df = self.n - 1
    def test(self, mu, alpha):
        t_stat = (self.mean - mu) / (self.std / np.sqrt(self.n))
        p_value = 2 * (1 - t.cdf(np.abs(t_stat), df=self.df))
        if p_value < alpha:
            return True
        else:
            return False
    
def test_t_test():
    x = [1,2,3,4,5]
    mu = 3
    alpha = 0.05
    t_test_obj = T_test(x)
    scipy_t_stat, scipy_p_value = t1s(x, mu)
    assert t_test_obj.test(mu, alpha) == (scipy_p_value < alpha)
    
if __name__ == '__main__':
    test_t_test()
    print('t_test passed')
