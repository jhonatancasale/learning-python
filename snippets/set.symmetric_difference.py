"""
Semmetric difference between two sets, such as A and B is defined by
(A | B) - (A & B)
Therefore, all the elements belonging to either A or B but not the elements
belonging to both.
"""

A = set(range(10))
B = set([_ for _ in range(16) if _ % 2 == 0])
C = set([_ for _ in range(16) if _ % 2])

print()
print(f"Set A: {A}")
print(f"Set B: {B}")
print(f"Set C: {C}")

print()

print(f"A^B: {A.symmetric_difference(B)}")
print(f"A^C: {A.symmetric_difference(C)}")

print(f"A^A: {A ^ A}")
