import unittest
import sys,os
import numpy as np
import pandas as pd
import math
import os,sys
import json

from pandas.errors import MergeError, EmptyDataError, ParserError, \
    InvalidIndexError, DtypeWarning, DuplicateLabelError

sys.path.append('../') 

## This unit testing framework is mostly just acting as a placeholder giv en the time limitation here.
# In reality this would be up and working with capability to continuosly add unit tests as more functionality arrives

from pipelineAccidentAnalyser import CrudePipeLineAnalysis

class Testing(unittest.TestCase):

    CrudePipeLineAnalysis test_pipelineAnalist();

    df_test = pd.DataFrame()

    def test_do_checks_on_dataframe(self):

        retVal_test = test_pipelineAnalist.do_checks_on_dataframe (self, df_test )

        exected_return_bool = True

        self.assertEqual(retVal_test, exected_return_bool)

    def test_plot_correlation_map(self, df_test ):

        teamA_win_odds = 1.5
        teamB_win_odds = 6.0
        draw_odds      = 8.1

        retVal_test = test_pipelineAnalist.plot_correlation_map(self,df_test)

        exected_return_float = 0.9567

        self.assertAlmostEquals(retVal_test, exected_return_float,places=3)


    def test_density_mix(self, df_test ):

        teamA_win_odds = 1.5
        teamB_win_odds = 6.0
        draw_odds      = 8.1

        retVal_test = test_pipelineAnalist.density_mix(self,dense_test1 = 1.25, dense_test2 = 0.75, percent1_test = 0.5 )

        exected_return_float = 0.9567

        self.assertAlmostEquals(retVal_test, exected_return_float,places=3)


