import matplotlib.pyplot as plt
import numpy as np

methods = [None, 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36']

# Fixing random state for reproducibility
np.random.seed(133422219)

grid = np.random.rand(2, 2)

fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(9, 6), subplot_kw={'xticks': [], 'yticks': []})

for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))

plt.tight_layout()
plt.show()
