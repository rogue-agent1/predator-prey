#!/usr/bin/env python3
"""Lotka-Volterra predator-prey population dynamics simulator."""
import sys

def lotka_volterra(prey0, pred0, alpha, beta, gamma, delta, dt=0.01, steps=1000):
    prey, pred = [prey0], [pred0]
    x, y = float(prey0), float(pred0)
    for _ in range(steps):
        dx = (alpha * x - beta * x * y) * dt
        dy = (delta * x * y - gamma * y) * dt
        x = max(0, x + dx); y = max(0, y + dy)
        prey.append(x); pred.append(y)
    return prey, pred

def stats(series):
    return {"min": min(series), "max": max(series), "mean": sum(series)/len(series), "final": series[-1]}

def main():
    if len(sys.argv) < 2: print("Usage: predator_prey.py <demo|test>"); return
    if sys.argv[1] == "test":
        prey, pred = lotka_volterra(40, 9, alpha=0.1, beta=0.02, gamma=0.3, delta=0.01, steps=5000)
        assert len(prey) == 5001
        # Both populations should survive (oscillate)
        assert min(prey) > 0 and min(pred) > 0
        # Should oscillate - check that prey goes up and down
        ps = stats(prey)
        assert ps["max"] > ps["min"] * 1.5  # significant oscillation
        # Zero predators -> prey grows
        prey2, pred2 = lotka_volterra(10, 0, 0.1, 0.02, 0.3, 0.01, steps=100)
        assert prey2[-1] > prey2[0]; assert all(p == 0 for p in pred2)
        print("All tests passed!")
    else:
        prey, pred = lotka_volterra(40, 9, 0.1, 0.02, 0.3, 0.01, steps=3000)
        print(f"Prey:     {stats(prey)}"); print(f"Predator: {stats(pred)}")

if __name__ == "__main__": main()
