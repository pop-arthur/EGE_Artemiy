# P = [8; 47] и Q = [5; 18]
# ((x ∉ A) → (x ∉ P)) ∨ (x ∈ Q)

def f(x, Amin, Amax):
    return ((not (Amin <= x <= Amax)) <= (not (8 <= x <= 47))) or (5 <= x <= 18)


min_length = 10 ** 4
for Amin in range(-100, 100):
    for Amax in range(Amin + 1, 100):

        if all(f(x, Amin, Amax) for x in range(-100, 100)):
            min_length = min(Amax - Amin + 1, min_length)

print(min_length)
