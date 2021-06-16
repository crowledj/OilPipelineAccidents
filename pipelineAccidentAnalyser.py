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


class CrudePipeLineAnalysis():
    """
    Object : is a entity called 'CrudePipeLineAnalysis' - it refers to a single developer's analysis of this phenomenon -
    uniquely by his/her userID (which is a class member)
    It will have data sources, several dataframes - raw, cleaned, feature sets and models. 

    """
    def __init__(self):

        self.raw_data = pd.DataFrame()
        self.raw_data_USGOV = pd.DataFrame()

        self.cleaned_data = pd.DataFrame()
        self.cleaned_data__USGOV = pd.DataFrame()

        self.relevant_data_kaggle = pd.DataFrame()
        self.relevant_data__USGOV = pd.DataFrame()

        self.built_temporal_model = []  # ?? (weights to a regresion model o algo)


    def do_checks_on_dataframe(self, df):
        """
        PARAMETERS:

        df - dataframe of input data (must be and so auumes its in tabular SQl like format - eg .csv, excel file originally)

        Purpose :

        This function reads in the data spits out high level lstructure and information - like high level descriptive stats on the data as weell as giving the user an option for returning a 'cleaned'
        version of the data as well as the original back. Such cleaning will include checking for NaN values and removing the columns which contain them
        
        and loads the files with info on each round and course, plus the course's terrain data.
        It stores them in their respective Golfer() member functions


        output/return value :

        option for returning a 'cleaned'
        version of the data as well as the original back.
        Boolean indicating success or not.

        """


        if not isinstance( df, pd.DataFrame ):
            print('inputted data structure here is NOT a pandas dataframe , please re-check or create this correcty and try again')
            return False

        # Check dimensions of DF
        print('\n \n ***********************************************************')
        print('The dimansions of the tabular data are :' + str(df.shape))
        print('\n \n ***********************************************************')
        
        # display the Summary statistics of the DF...
        print('\n \n ***********************************************************')
        print(' *********** THE DATAFRAME"S SUMMARY STATISTICS ARE :   **********')
        print('\n \n ***********************************************************')     
        print(df.describe())

        # check are there naNs in the DF :

        try:
            if df.isna:
                print('\n \n ***********************************************************')
                print('\n \n **********  THE DATAFRAME CONTAINS NAN VALUES  *************')
                print('\n \n ***********************************************************')

            else:    
                print('\n \n ***********************************************************')
                print('********** THE DATAFRAME DOES NOT CONTAIN NAN VALUES **********')
                print('\n \n ***********************************************************')

        except EmptyDataError:
            print("The dataframe is actually empty - please check the data source or how its read in .., exiting function..")
            return False

        #print('Do you wish to remove rows with any Nans present')

        # display the first few rows of the df
        print('\n \n ***********************************************************')
        print('**********the first few rows of the df **********')
        print('\n \n ***********************************************************')
        #print('Do you wish to remove rows with any Nans present')
        df.head(100)

        # possibly drop the NaNs if they exis (and return in a copied df )  - or ask user if he/she wishes to do this in a custom way themselves
        return True



    def remove_replace_nans(self, df):
        """
        PARAMETERS:

        df - dataframe of input data (must be and so auumes its in tabular SQl like format - eg .csv, excel file originally)

        Purpose :

        This function reads in the data spits out high level lstructure and information - like high level descriptive stats on the data as weell as giving the user an option for returning a 'cleaned'
        version of the data as well as the original back. Such cleaning will include checking for NaN values and removing the columns which contain them
        
        and loads the files with info on each round and course, plus the course's terrain data.
        It stores them in their respective Golfer() member functions


        output/return value :

        option for returning a 'cleaned'
        version of the data as well as the original back.
        Boolean indicating success or not.

        """
        
        new_df = df

        print('Do you wish to remove rows with any Nans present - Y/N:')

        answer = input()
      
        if answer == 'N' or answer == 'n':
            print('Do you wish to remove rows with any Nans present - Y/N:')

            second_ans =  input() 
            if second_ans == 'N' or answer == 'n':
                print("OK, dataframe left as is...")
                pass
            elif second_ans ==  'Y' or answer == 'y':
                self.cleaned_dat = df.dropna(how = 'all')
            else:
                print("please input Y or N...")  

        elif answer ==  'Y' or answer == 'y':
             self.cleaned_data = df.dropna(how = 'any')

        else:
                print("please input Y or N...")      

        # display the first few rows of the df
        # possibly drop the NaNs if they exis (and return in a copied df )  - or ask user if he/she wishes to do this in a custom way themselves


        return self.cleaned_dat

    # function to create a heatmap of the correlations between columns in a dataframe:
    # #compute correlations of all columns in dataframe and display correlation heatmap !:
    def plot_correlation_map(self, df ):

        """
        PARAMETERS:

        df

        Purpose :

        This function read in and loads the files with info on each round and course, plus the course's terrain data.
        It stores them in their respective Golfer() member functions


        outpur/return value :

        Boolean indicating success or not.

        """

        corr = df.corr()
        _ , ax = plt.subplots( figsize =( 120 , 80 ) )
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


    def density_mix(self, dense_1,dense_2, percent_1 ):
        """
        PARAMETERS:

         round_file,
         terrain_file,
         course_info_file

        Purpose :

        This function read in and loads the files with info on each round and course, plus the course's terrain data.
        It stores them in their respective Golfer() member functions


        outpur/return value :

        Boolean indicating success or not.

        """

        density_mix = 1.0
        simple_dense_mix = (dense_1 + dense_2) / 2.0

        if percent_1 == 1.0 and dense_1 == 0.0:
            return simple_dense_mix

        elif dense_1 == dense_2 == 0.0:
            return simple_dense_mix    
        else:
            density_mix = 2*(dense_1*dense_2)/ ( (percent_1 * dense_1) + ((1- percent_1) * dense_2) )


        return density_mix


    def time_cost_model_n_plot(self, df_1, remove_year=['2017'], group_by_column = 'Accident Year' ,headers = ['Accident Year','All Costs','Property Damage Costs',
            'Other Costs'] ):

        #headers = ['Accident Year','All Costs','Property Damage Costs',
        #    'Lost Commodity Costs','Public/Private Property Damage Costs',
        #    'Emergency Response Costs','Environmental Remediation Costs', 'Other Costs']
        df_reduced = df_1[headers]
        for i in range(len(remove_year  )):
            df_reduced = df_reduced[df_reduced['Accident Year'] != remove_year[i]] # and 'Accident Year'] != 2010 ]
        per_year = df_reduced.groupby(group_by_column)

        indices = per_year.sum()['All Costs'].index.values
        yAll_sum = per_year.sum()['All Costs'].values


        f, a = plt.subplots(nrows=1, ncols=2, figsize=(13,5))

        a[0].fill_between(indices, yAll_sum, 10E0, facecolor='black', alpha=0.1)

        a[0].get_xaxis().get_major_formatter().set_useOffset(False)
        a[0].set_xlabel('Year', fontsize=16)
        a[0].set_ylabel('Sum Cost ($Million)', fontsize=16)
        a[0].legend()


        return True



        

if __name__  == '__main__':
    
    import os

    Oilpipeline_1 = CrudePipeLineAnalysis()


    os.chdir('C:/Users/MaaD/coding_projects/kaggle/oil_pipeline_accidents')
    cwd = os.getcwd()
    data_file = gwd + '/' + 'database.csv'

    try:
        data = pd.read_csv(data_file)
    except FileNotFoundError as e:
        print("Excel file not found " + str(e) + ' -- please ensure The file is in your current working directory, now exiting program...')
        #return False

    except IOError as e:
        print("invalid data format encountered in file " + str(e) + ' -- please ensure The file content is in the corre3ct format, now exiting program...')
        #return False

    except Exception as err:
        print('Specific error is : ' + str(err))
        #return False


    pd.set_option("display.max_columns", None)

    Oilpipeline_1.time_cost_model_n_plot(data)

    chech = -1
