from os import path
import pandas as pd
import numpy as np

class VarianceDecompose:

    d_natoms = {'arna+arna': 676, 'bdna+bdna': 650}

    def __init__(self, rootfolder, type_na):
        self.type_na = type_na
        self.na_folder = path.join(rootfolder, type_na)

    def read_c2_doperator_dc_df(self, v1_id, v2_id):
        f_in = path.join(self.na_folder, 'c2_doperator_dc_df_v1_{0}_v2_{1}.csv'.format(v1_id, v2_id))
        df = pd.read_csv(f_in)
        return df

def get_data_by_df_bend_angle(df, start_mode, end_mode):
    parameter = 'dtheta_dc'
    c2square = df['<c2>'].values[start_mode-1:end_mode]
    parameter_prime_sqaure = np.square(df[parameter].values[start_mode-1:end_mode])
    product = np.multiply(parameter_prime_sqaure, c2square)
    return product

def get_data_by_df_contour_length(df, start_mode, end_mode):
    parameter = 'dL_dc'
    c2square = df['<c2>'].values[start_mode-1:end_mode]
    parameter_prime_sqaure = np.square(df[parameter].values[start_mode-1:end_mode])
    product = np.multiply(parameter_prime_sqaure, c2square)
    return product

def get_data_by_df_twiststretch_coupling(df, start_mode, end_mode):          
    c2square = df['<c2>'].values[start_mode-1:end_mode]
    parameter_prime_sqaure = np.multiply(df['dL_dc'].values[start_mode-1:end_mode], df['domega_dc'].values[start_mode-1:end_mode])
    product = np.multiply(parameter_prime_sqaure, c2square)
    return product     