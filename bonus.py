# bonus.py
"""Bonus: Find Variance and Standard Deviation of data set >= 100 numbers"""

# Initilization
import statistics as stats

# Processing / Display
print('Display Population/Standard Deviation for numbers 1-1000')
print('Population Variance:', stats.pvariance(range(1,1001)))
print('Population Standard Deviation:', stats.pstdev(range(1,1001)))