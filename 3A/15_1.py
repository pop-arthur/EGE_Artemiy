#  P = [5, 30] и Q = [14, 23]
# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)

def f(Amin, Amax, x):
    return ((5 <= x <= 30) == (14 <= x <= 23)) <= (not (Amin <= x <= Amax))


mx = 0
for Amin in range(-100, 100):
    for Amax in range(Amin + 1, 100):

        if all(f(Amin, Amax, x) for x in range(-100, 100)):
            mx = max(Amax - Amin + 1, mx)

print(mx)