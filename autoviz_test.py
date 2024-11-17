import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from autoviz.AutoViz_Class import AutoViz_Class


AV = AutoViz_Class()
df_visualized = AV.AutoViz(
    filename="data/Superstore.csv",  # Filename is not used since we are passing a DataFrame
    sep =",",
    dfte="",      # DataFrame loaded from the uploaded file
    verbose=2,
    depVar="",    # No dependent variable specified
     # Enable verbose output
)