# population-dispersion.py
"""Population Variance and Standard Deviation for 10 six-sided dice rolls"""

# Initilization
import statistics as stats

rolls =[1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

# Processing / Display
print('10 rolls on a six sided dice:', rolls)
print('Population Variance:', stats.pvariance(rolls))
print('Population Standard Deviation:', stats.pstdev(rolls))