#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:34:17 2019
f
Utility for classifaction and data preparation
"""

# import build-in
import numpy as np

# import third party
import cdutil
import netCDF4 as nc
import cdms2


# import local
# import utility as ut



def prepare_data(path, filename):
    '''
    read the data 
    input:
        path : file location
        filename : 
            
    output: SST
    example: 
        filename =['AMSRE_processed.nc_nino3.nc',
           'HadISST_processed.nc_nino4.nc',
           'HadISST_processed.nc_nino12.nc']
        x3, x4, x12 = [prepare_data(path,i) for i in filename]
    '''
    f = cdms2.open(path+filename)
    x = f('sst')
    x = np.array(x[:,0,0])
    return x

def reshape_feature(x, crop=26, firstmon =10, no_months=6, verbose=False):
    '''
    reshape the feature to start and finish at specify month
    and crop for years with labels
    input:
        - x = input data
        - crop = number of years removed to make start point equal to where labelling begins
        - first_mon = month want to start in e.g. 10 = October
        - no_months - how many months to include in analysis
    output:
        - cropped data
        - it is in year x months for each input dataset
    example
        data_reshape, _=reshape_feature(data,crop= 46,verbose=True)
        data_reshape = [reshape_feature(x) for x in data]
    
    '''
    residual_month = np.mod(x.shape[0],12)
    if residual_month >=3:
        full_size=int(np.ceil(float(x.shape[0])/12)*12)
        x2=np.zeros(full_size)
        x2[0:len(x)]=x
    elif residual_month != 0:
        x2=x[:-residual_month]
    elif residual_month == 0 :
        x2=x
    
    x2_move_month=x2[firstmon-1:firstmon-13]    
    x_reshaped = x2_move_month.reshape((-1,12))
    x_crop = x_reshaped[crop:,:-no_months]
    
    if verbose: 
        print ("cropped data size:", x_crop.shape)
        print ("residual month:", residual_month)
        
    return x_crop

def preprocess_from_dict(dict_, path, verbose = True):
    '''
    input:
        - dict_:
    '''
    result ={}
        
    for key, value in dict_.iteritems():
        
        filename  = value['filename']
        x = prepare_data(path, filename )
        crop = value['crop']
        firstmon = value['firstmon']
        reshaped = reshape_feature(x, crop=crop, firstmon=firstmon, verbose=verbose)
        
        result[key]=reshaped
    
    return result
