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

