# built-in-min-max.py
"""Call functions to find Max of (12,27,36) and Min of (15,9,27,14)"""

# Initilization/Processing
def maximum_manual_3(max_val1, max_val2, max_val3):
    """Find max value of 3 numbers"""
    max_val = max_val1
    if max_val2 > max_val:
        max_val = max_val2
    if max_val3 > max_val:
        max_val = max_val3
    return max_val

def minimum_manual_4(min_val1, min_val2, min_val3, min_val4):
    """Find min value of 4 numbers"""
    min_val = min_val1
    if min_val2 < min_val:
        min_val = min_val2
    if min_val3 < min_val:
        min_val = min_val3
    if min_val4 < min_val:
        min_val = min_val4
    return min_val

max_val1 = 12
max_val2 = 27
max_val3 = 36

min_val1 = 15
min_val2 = 9
min_val3 = 27
min_val4 = 14

# Termination / Display

print('The Manual Maximum Value of (12,27,36) =', maximum_manual_3(max_val1, max_val2, max_val3))
print('The Built in Maximum Value of (12,27,36) =', max(max_val1, max_val2, max_val3))
print('The Manual Minimum Value of (15,9,27,14) =', minimum_manual_4(min_val1, min_val2, min_val3, min_val4))
print('The Built in Maximum Value of (15,9,27,14) =', min(min_val1, min_val2, min_val3, min_val4))
