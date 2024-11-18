import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from autoviz.AutoViz_Class import AutoViz_Class

AV = AutoViz_Class()



dfte = AV.AutoViz(
    filename="data/Superstore2.csv",  # or pass a pandas DataFrame instead
    sep=',',
    depVar='',  # target variable (if any)
    dfte=None,  # use this if passing a DataFrame instead of filename
    header=1,
    verbose=2,
    
    lowess=False,
    chart_format='svg',
    max_rows_analyzed=150000,
    max_cols_analyzed=30,
    save_plot_dir=None
)





# AV = AutoViz_Class()
# df_visualized = AV.AutoViz(
#     filename="data/Superstore.csv",  # Filename is not used since we are passing a DataFrame
#     sep =",",
#     dfte="",      # DataFrame loaded from the uploaded file
#     verbose=2,
#     depVar="",    # No dependent variable specified
#      # Enable verbose output
# )




# If using a DataFrame
# dfte = AV.AutoViz("", sep=',', depVar='', dfte=df, header=0, verbose=1, lowess=False,
#            chart_format='svg', max_rows_analyzed=150000, max_cols_analyzed=30, save_plot_dir=None)