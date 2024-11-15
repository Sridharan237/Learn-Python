# python program to use the statistics module

import statistics as s

print(s.mean([1, 2, 3, 4, 5]))
# Output : 3

print(s.harmonic_mean([1, 2, 3, 4, 5]))
# Output : 2.18978102189781



print(s.median([1, 2, 3, 4, 5]))
# Output : 3

print(s.median([1, 2, 3, 4, 5]))
# Output : 3

print(s.median([1, 2, 3, 4, 5, 6]))
# Output : 3.5

print(s.median_low([1, 2, 3, 4, 5, 6]))
# Output : 3

print(s.median_high([1, 2, 3, 4, 5, 6]))
# Output : 4

print(s.median([1, 2, 30, 50, 51, 52]))
# Output : 40.0

print(s.median_low([1, 2, 30, 50, 51, 52]))
# Output : 30

print(s.median_high([1, 2, 30, 50, 51, 52]))
# Output : 50



print(s.mode([1, 2, 1, 3, 3, 1, 5, 1]))
# Output : 1

print(s.mode([2, 2, 1, 1, 3, 3]))
# Output : 2

print(s.mode([4, 4, 4, 3, 2, 3, 2, 3, 2]))
# Output : 4



print(s.pvariance([1, 2, 3, 4, 5]))
# Output : 2

print(s.pstdev([1, 2, 3, 4, 5]))
# Output : 1.4142135623730951

print(s.variance([1, 2, 3, 4, 5]))
# Output : 2.5

print(s.stdev([1, 2, 3, 4, 5]))
# Output : 1.5811388300841898
