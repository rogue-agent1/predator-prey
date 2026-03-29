from predator_prey import lotka_volterra, sir_model
prey, pred = lotka_volterra(40, 9, steps=1000)
assert len(prey) == 1001
assert all(v >= 0 for v in prey)
assert all(v >= 0 for v in pred)
S, I, R = sir_model(990, 10, 0)
assert abs(S[-1] + I[-1] + R[-1] - 1000) < 1, "Population should be conserved"
print("Predator-prey tests passed")