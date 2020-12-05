#################################
########## UTILITIES ############
#################################

import pandas as pd
import numpy as np

def str_to_float(s):
    """ e.g. '0.78 (2)' -> 0.78
        TODO: more robust
    """
    if isinstance(s, str):
        if s[-1]==')':
            s = float(s.split(' ')[0])
    return s

def read_codalab_csv(csv_file):
    """ Read a leaderboard generated by Codalab as a CSV file.
    
        :param csv_file: The leaderboard downloaded from Codalab.
    """
    m = pd.read_csv('data/chems.csv', usecols=np.arange(0,5), index_col=1)
    m = m.drop('submission_pk', axis=1)
    m = m.applymap(str_to_float)
    return m
