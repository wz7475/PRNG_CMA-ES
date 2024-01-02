import numpy as np
from scipy.stats import qmc
from .mocking_prng import MOCKING_PRNG


class HALTON_PRNG(MOCKING_PRNG):
    name='halton'
    def __init__(self, seed, chunk_size=2**12) -> None:
        super().__init__(seed, chunk_size)
        #self._prng = qmc.Halton(d=1, scramble=False, seed=self._seed)
        #_ = self._prng.fast_forward(5) # First value in sequence is 0 so mapping to std_dist yields -inf. Skipping first few values prevents that

    def __str__(self) -> str:
        return f"halton_{super().__str__()}"

    def _gen_uniform(self, dim: int):
        return self._prng.random(dim).astype(np.float32)