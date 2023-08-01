import math
import numpy as np


layer_outputs = [4.8, 1.21, 2.385]

E = math.e

exp_values = []

for output in layer_outputs:
    exp_values.append(E ** output)

norm_base = sum(exp_values)
norm_val = []

for val in exp_values:
    norm_val.append(val / norm_base)