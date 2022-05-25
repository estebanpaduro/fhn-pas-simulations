# %% importar librerias
import seaborn as sns
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

# %%
fig, ax = plt.subplots()
x= pd.read_csv("data_fig5.csv", sep=",",names=["amplitude","freq","spikerate"],header=0)
df = x[["amplitude","freq","spikerate"]]
df = df.groupby(['amplitude','freq']).sum()
df = df.reset_index()
df.columns =["amplitude","freq","spikerate"]
df_pivot=df.pivot('amplitude', 'freq')

X=df_pivot.columns.levels[1].values
Y=df_pivot.index.values
Z=df_pivot.values
Xi,Yi = np.meshgrid(X, Y)

vmin = 0
vmax = 30
levels = vmax - vmin+1
level_boundaries = np.linspace(vmin, vmax, levels+ 1)

from matplotlib.cm import ScalarMappable
graf1 = ax.contourf(Yi, Xi, Z, 
    level_boundaries,  # change this to `levels` to get the result that you want
    vmin=vmin, vmax=vmax, cmap=plt.cm.jet)

ax.set_xlabel('Stimulation amplitude $A = B$')
ax.set_ylabel('Envelope frequency $\eta/(2\pi)$ [Hz]')

cbar = fig.colorbar(
    ScalarMappable(norm=graf1.norm, cmap=graf1.cmap),
    ticks=range(vmin, vmax+1, 5),
    boundaries=level_boundaries,
    values=(level_boundaries[:-1] + level_boundaries[1:]) / 2,
)
cbar.set_label('Spike rate [spikes/s]', rotation=270, labelpad=15)
plt.savefig('Fig5.png')