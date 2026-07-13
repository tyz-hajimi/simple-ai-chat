#!/usr/bin/env python3
"""Numerical verification of lemmas for Conway-Guy dissociated sets."""

from math import isqrt, comb, log2
import numpy as np


def conway_guy(n_max: int):
    u = [0] * (n_max + 1)
    if n_max >= 1:
        u[1] = 1
    for n in range(1, n_max):
        r = (isqrt(8 * n) + 1) // 2
        u[n + 1] = 2 * u[n] - u[n - r]
    return u


def subset_sums(A):
    s = np.array([0], dtype=np.int64)
    for a in A:
        s = np.concatenate((s, s + a))
    return np.sort(s)


def mod_energy(A, q):
    c = np.zeros(q, dtype=np.int64)
    c[0] = 1
    for a in A:
        c = c + np.roll(c, int(a) % q)
    M = 1 << len(A)
    return int(c @ c) / M, int(c.max())


def verify(n_max: int = 16):
    u = conway_guy(n_max)
    print("n N N/2^n H/C W/C R_2N gap1 Qbound missing_ltN")
    for n in range(4, n_max + 1):
        N = u[n]
        # ascending so newly added element is always the subset max
        A = sorted(N - u[j] for j in range(n))
        s = subset_sums(A)
        M = 1 << n
        T = int(sum(A))
        sums = np.array([0], dtype=np.int64)
        mx = np.array([0], dtype=np.int64)
        for a in A:
            sums = np.concatenate((sums, sums + a))
            mx = np.concatenate((mx, np.full(mx.shape, a, dtype=np.int64)))
        H = int(np.count_nonzero((2 * sums > T) & (2 * (sums - mx) < T)))
        C = comb(n, n // 2)
        ends = np.searchsorted(s, s + N, side="left")
        W = int((ends - np.arange(M)).max())
        R2N, _ = mod_energy(A, 2 * N)
        gaps = np.diff(s)
        gap1 = int(np.count_nonzero(gaps == 1))
        missing = -1
        if n <= 12:
            bits = 1
            total = 0
            for a in A[:-1]:
                ai = int(a)
                bits |= (bits << ai) | (bits << (2 * ai))
                total += ai
            missing = sum(
                1 for v in range(1, N) if ((bits >> (v + total)) & 1) == 0
            )
        print(
            f"{n:2d} {N:6d} {N/M:.6f} {H/C:.4f} {W/C:.4f} "
            f"{R2N:.4f} {gap1/M:.4f} {43/64:.4f} {missing}"
        )


if __name__ == "__main__":
    verify(18)
