# %%

import matplotlib.pyplot as plt
import numpy as np

import pydanski as pdk

# %%

A = np.random.uniform(0, 1, size=20).reshape((-1, 2))
fig, ax = plt.subplots()
for i in range(A.shape[0]):
    ax.scatter(A[i, 0], A[i, 1], label="Random Point")
ax.legend()
pdk.plots.remove_duplicate_legends(fig, ax)
fig.show()

# %%

A = np.array([1, 2, 3, 4])

fig, ax = plt.subplots()
ax.bar(np.arange(4), A)
pdk.plots.add_text_to_bars(fig, ax, ["A", "B", "C", "D"])
fig.show()
