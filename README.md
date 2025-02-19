# Marine Heatwaves and Heat/Humidity in Houston/Galveston Bay

## Description
This project uses the outputs of [Weather Research and Forecasting (WRF) Model](https://www.mmm.ucar.edu/models/wrf) simulations to examine the connection between marine heatwaves in the Gulf and coastal temperatures and humidity in the Houston/Galveston Bay region.

## Contact + Timeline
This is part of an initiative with GCOOS, started in the fall of 2024 and still under active development. Please contact Ren Poulton Kamakura (renata.kamakura@gcoos.org) if you have any questions.

## Folders
* 01Data: contains the wrfout files from the WRF model runs (often too large to be on GitHub but can be requested)
* 02Code: contains the data analysis and management codes. The Python codes are primarily for reformatting wrfout files and for some basic vualizations. The R codes are for exploratory data analysis and spatial mixed-effects regressions
* 03ProcessedData: Outputs from data cleaning codes in the previous folder, used in data analysis. Again, many are too large to currently appear in the GitHub repository
* 04Visuals: Figures and other visuals from exploratory data analysis or more in-depth analysis

## Contributing
Since the project is in its early stages and the outputs are primarily data analysis and not applications, please contact renata.kamakura@gcoos.org if you would like to contribute.

##Acknowledgements
WRF runs were possible due to support from Dr. Dan Fu at Texas A&M University, [Texas A&M High Performance Research Computing](https://hprc.tamu.edu/) and technical support from Xiao Qi at GCOOS.
