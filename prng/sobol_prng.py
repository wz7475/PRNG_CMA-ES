from scipy.stats import qmc, norm
from .prng import PRNG


class SOBOL_PRNG(PRNG):
    def __init__(self, seed) -> None:
        self._prng = qmc.Sobol(d=1, seed=seed)

    def __str__(self) -> str:
        return f"sobol_prng_{super().__str__()}"

    def std_normal(self, dim: int):
        samples = self._prng.random(n=dim)
        return norm.ppf(samples).reshape((1, dim))[0]