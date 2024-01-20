#%%
import polars as pl
import pyarrow as pw
import plotly as ply
import statsmodels as st
#%%
places = pl.read_parquet()
patterns = pl.read_parquet("https://github.com/byuibigdata/challenge_church_wi24/blob/main/data/parquet/patterns.parquet")
#%%

#%%

#%%