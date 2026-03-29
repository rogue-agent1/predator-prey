#!/usr/bin/env python3
"""Predator-prey (Lotka-Volterra) simulation. Zero dependencies."""
import sys

def lotka_volterra(prey0, pred0, alpha=1.1, beta=0.4, delta=0.1, gamma=0.4, dt=0.01, steps=10000):
    prey, pred = [prey0], [pred0]
    x, y = float(prey0), float(pred0)
    for _ in range(steps):
        dx = (alpha*x - beta*x*y) * dt
        dy = (delta*x*y - gamma*y) * dt
        x += dx; y += dy
        x = max(0, x); y = max(0, y)
        prey.append(x); pred.append(y)
    return prey, pred

def sir_model(S0, I0, R0, beta=0.3, gamma=0.1, dt=0.1, steps=1000):
    S, I, R = [S0], [I0], [R0]
    s, i, r = float(S0), float(I0), float(R0)
    N = s + i + r
    for _ in range(steps):
        ds = -beta * s * i / N * dt
        di = (beta * s * i / N - gamma * i) * dt
        dr = gamma * i * dt
        s += ds; i += di; r += dr
        S.append(s); I.append(i); R.append(r)
    return S, I, R

def ascii_plot(series, width=60, height=15, labels=None):
    all_vals = [v for s in series for v in s]
    mn, mx = min(all_vals), max(all_vals)
    if mx == mn: mx = mn + 1
    n = len(series[0])
    step = max(1, n // width)
    chars = "·ox#@"
    grid = [[" "]*width for _ in range(height)]
    for si, s in enumerate(series):
        ch = chars[si % len(chars)]
        for xi in range(width):
            idx = min(xi * step, len(s)-1)
            yi = int((s[idx] - mn) / (mx - mn) * (height-1))
            yi = height - 1 - yi
            grid[yi][xi] = ch
    lines = ["".join(row) for row in grid]
    if labels:
        lines.append(" ".join(f"{chars[i%len(chars)]}={l}" for i, l in enumerate(labels)))
    return "\n".join(lines)

if __name__ == "__main__":
    prey, pred = lotka_volterra(40, 9)
    print(ascii_plot([prey, pred], labels=["Prey", "Predator"]))
