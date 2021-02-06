
## Python For Finance 

The code is based on [randerson112358's](https://randerson112358.medium.com/) work described [here](https://randerson112358.medium.com/python-for-finance-25d2ed1ed35d) with a video [here](https://www.youtube.com/watch?v=O-O1WclwXck)

Initially coded in jupyter notebook on Google's colaboratory following the video referenced above. Python generated from jupyter notebook with: 
```console
jupyter nbconvert --to script *.ipynb
```

A portfolio simple returns program.
* gets historical stock values for 5 tickers from yahoo
* store in Pandas DataFrame (df) (two-dimensional data structure like a spreadsheet)
* use df functions to get daily % change and statistics (variances, correlations, mean, std dev, etc.)
* model a weighted portfolio
* calculate and plot cumulative returns

Here is a sample output:

![Portfolio Value Over Time](doc/images/daily_cumulative.png?raw=true "Daily Cumulative Simple Returns")