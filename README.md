# Generate figures used in the paper: A partially averaged system to model neuron responses to interferential current stimulation
Mathematica and python files used to generate the graphs in the article.: A partially averaged system to model neuron responses to interferential current stimulation
Authors: Cerpa E., Courdurier M., Hernandez E., Medina L., Paduro E.

## Download 
From a command line:
```
git clone https://github.com/estebanpaduro/fhn-pas-simulations
```
## Contents
The scripts are organized in the following folders:

* `fig1_interference_pattern.nb`: Generate a plot of a interferential current with beat frequency.
* `fig2_separatrix.nb`: Generate a plot of the separatrix of the FHN system and the null lines.
* `fig3_averaging.nb`: Generate 3 plots that illustrate the Partial Averaging method used in the paper.
* `fig4_amplitude_vs_amplitude_heatmap.nb`: Generate csv files for a graph of amplitude vs amplitude in the Partially averaged system and measure the spike rate for each pair using 4 different frequencies eta.
* `fig4_generate_graph_from_csv.py`: Generate image files from the csv files generated by `fig4_amplitude_vs_amplitude_heatmap.nb`.
* `fig5_eta_vs_amplitude_heatmap.nb`: Generate csv file for a graph of amplitude vs beat frequency in the Partially averaged system and measure the spike rate for each pair.
* `fig5_generate_graph_from_csv.py`: Generate image file from the csv file generated by `fig5_eta_vs_amplitude_heatmap.nb`.

## References

[1] Cerpa E., Courdurier M., Hernandez E., Medina L., Paduro E. (2022) A partially averaged system to model neuron responses to interferential current stimulation

## License

[MIT](LICENSE)