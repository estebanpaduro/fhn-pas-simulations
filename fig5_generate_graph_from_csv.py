# %% import libraries
import seaborn as sns
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

# %%
for frequency in ["10","50","80","120"]:
    fig, ax = plt.subplots()
    x= pd.read_csv("data_fig5_"+frequency+"hz.csv", sep=",",header=0,names=["A","B","freq","spikerate"])
    df = x[["A","B","spikerate"]]
    df = df.groupby(['A','B']).sum()
    df = df.reset_index()
    df.columns =["A","B","spikerate"]
    df_pivot=df.pivot('A', 'B')
    
    X=df_pivot.columns.levels[1].values
    Y=df_pivot.index.values
    Z=df_pivot.values
    Xi,Yi = np.meshgrid(X, Y)
    
    vmin = 0
    vmax = 31
    levels = vmax - vmin+1
    level_boundaries = np.linspace(vmin, vmax, levels)-0.5
    
    from matplotlib.cm import ScalarMappable
    graf1 = ax.contourf(Yi, Xi, Z, 
        level_boundaries,
        vmin=vmin, vmax=vmax, cmap=plt.cm.jet)
    
    ax.set_xlabel('Amplitude parameter $A$')
    ax.set_ylabel('Amplitude parameter $B$')
    
    cbar = fig.colorbar(
        ScalarMappable(norm=graf1.norm, cmap=graf1.cmap),
        ticks=range(vmin, vmax+1, 5),
        boundaries=level_boundaries,
        values=(level_boundaries[:-1] + level_boundaries[1:]) / 2,
    )
    cbar.set_label('Spike rate [spikes/s]', rotation=270, labelpad=15)
    
    plt.savefig('Fig5_'+frequency+'hz.png')
