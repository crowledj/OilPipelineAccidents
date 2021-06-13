import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import os,sys

import json
from scipy.stats import zscore

from pandas.errors import MergeError, EmptyDataError, ParserError, \
    InvalidIndexError, DtypeWarning, DuplicateLabelError

# dEFINE some fixed constants:
HALF_ROTATION = 180
FULL_ROTATION = 360
QUARTER_ROTATION = 90

MIN_PAR_PIN = 3
MEDIAN_PAR_PIN = 4
MAX_PAR_PIN = 5

SHORT_NON_PUTT_DIST = 30
NUMBER_PUTTS_NORMALIZE_CONSTANT = 3


class CrudePipeLineAnalysis():
    """
    Object : is a entity called 'CrudePipeLineAnalysis' - it refers to a single developer's analysis of this phenomenon -
    uniquely by his/her userID (which is a class member)
    It will have data sources, several dataframes - raw, cleaned, feature sets and models. 

    """
    def __init__(self):

        self.userID = '2ffl247vefbv5ue7qh1v6o045q9eirverv'

        self.rounds_data = []
        self.terrain_data = []
        self.course_info = []

        self.raw_data_kaggle = pd.DataFrame()
        self.raw_data_USGOV = pd.DataFrame()

        self.cleaned_data_kaggle = pd.DataFrame()
        self.cleaned_data__USGOV = pd.DataFrame()

        self.relevant_data_kaggle = pd.DataFrame()
        self.relevant_data__USGOV = pd.DataFrame()

        self.built_temporal_model = []  # ?? (weights to a regresion model o algo)

  


    def do_checks_on_dataframe(self, df):

        if not isinstance( df, pd.DataFrame ):
            print('inputted data structure here is NOT a pandas dataframe , please re-check or create thius and try again')
            return False

        # Check dimensions of DF


        # check are there naNs in the DF :

        # display the Summary statistics of the DF...

        # display the first few rows of the df

        # possibly drop the NaNs if they exis (and return in a copied df )  - or ask user if he/she wishes to do this in a custom way themselves


        return True


    # function to create a heatmap of the correlations between columns in a dataframe:
    # #compute correlations of all columns in dataframe and display correlation heatmap !:
    def plot_correlation_map(self, df ):


        corr = df.corr()
        _ , ax = plt.subplots( figsize =( 12 , 10 ) )
        cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
        _ = sns.heatmap(
            corr, 
            cmap = cmap,
            square=True, 
            cbar_kws={ 'shrink' : .9 }, 
            ax=ax, 
            annot = True, 
            annot_kws = { 'fontsize' : 12 }
        ); 







        




