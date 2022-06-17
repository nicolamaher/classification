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

import os
import random
from shutil import copyfile, copy2 , move, rmtree
from natsort import natsorted
import glob
from tqdm import tqdm


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
        
    for key, value in dict_.items():
        
        filename  = value['filename']
        x = prepare_data(path, filename )
        crop = value['crop']
        firstmon = value['firstmon']
        reshaped = reshape_feature(x, crop=crop, firstmon=firstmon, verbose=verbose)
        
        result[key]=reshaped
    
    return result


def reshape_feature2(x, crop=26, firstmon =6, no_months=2, verbose=False):
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

def preprocess_from_dict2(dict_, path, verbose = True):
    '''
    input:
        - dict_:
    '''
    result ={}
        
    for key, value in dict_.items():
        
        filename  = value['filename']
        x = prepare_data(path, filename )
        crop = value['crop']
        firstmon = value['firstmon']
        reshaped = reshape_feature2(x, crop=crop, firstmon=firstmon, verbose=verbose)
        
        result[key]=reshaped
    
    return result



# Concatenate 
def concat_features(result, keys, axis=0):
    '''
    this concatanates the model data
    '''
    list_= [result[key] for key in keys]
    return np.concatenate(list_,axis=axis)


def prepare_data2c(path, filename):
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
    sst = f('sst')
    #lon=sst('lon')
    #lat=sst('lat')
    #lon=np.array(lon)
    #lat=np.array(lat)
    sst=np.squeeze(np.array(sst))
    #sst=sst[0:155,:,:]
    #x = np.array(x[:,0,0])
    return sst#, lon, lat

def prepare_data2(path, filename):
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
    sst = f('sst')
    #lon=sst('lon')
    #lat=sst('lat')
    #lon=np.array(lon)
    #lat=np.array(lat)
    sst=np.squeeze(np.array(sst))
    sst=sst[0:155,:,:]
    #x = np.array(x[:,0,0])
    return sst#, lon, lat

def prepare_data2b(path, filename):
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
    sst = f('tos')
    #lon=sst('lon')
    #lat=sst('lat')
    #lon=np.array(lon)
    #lat=np.array(lat)
    sst=np.squeeze(np.array(sst))
    sst=sst[0:155,:,:]
    #x = np.array(x[:,0,0])
    return sst#, lon, lat


def prepare_data2d(path, filename):
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
    sst = f('tos')
    #lon=sst('lon')
    #lat=sst('lat')
    #lon=np.array(lon)
    #lat=np.array(lat)
    sst=np.squeeze(np.array(sst))
    #sst=sst[0:155,:,:]
    #x = np.array(x[:,0,0])
    return sst#, lon, lat

def prepare_data3(path, filename):
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
    sst = f('sst')
    #lon=sst('lon')
    #lat=sst('lat')
    #lon=np.array(lon)
    #lat=np.array(lat)
    sst=np.squeeze(np.array(sst))
    #sst=sst[0:155,:,:]
    #x = np.array(x[:,0,0])
    return sst#, lon, lat


def find_events(event_name,pred,data): 
    '''
    this function finds events of event name (e.g. CP) 
    and then creates a map of the average of that event type from the full data
    input: 
        event name e.g. CP, EP
        pred = prediction from classifier e.g. CP EP NE
        data = full data map for DJF average
        
    output:
        mean map for that event class
    '''
    
    index=np.where(pred ==event_name)
    maps=np.squeeze(data[index,:,:])
    maps_mean=np.mean(maps,axis=0)
    return maps_mean


def number_events(event_name,pred,data): 
    '''
    this function finds events of event name (e.g. CP) 
    and then creates a map of the average of that event type from the full data
    input: 
        event name e.g. CP, EP
        pred = prediction from classifier e.g. CP EP NE
        data = full data map for DJF average
        
    output:
        mean map for that event class
    '''
    
    index=np.where(pred ==event_name)
    maps=np.squeeze(data[index,:,:])
    no_events=len(maps[:,1,1])
    return no_events


def create_data_struct(path,features,firstmon = 6,crop =0, file_id='1950'):
    '''
    Create a dictionary of file name for the large ensemble so we can dont have to do it manually, this gives me the directory with first feature first second second and so on
    input :
        path - folder with files
        feature - name features, currently using nino 3W 3E 4W 4E and 12
        firstmon is first month used here 10 for october
        crop - no crop for what is being classified this is for the observational data
    output:
        dictionary of files and features to read in
        
    '''
    
    cwd = os.getcwd()
    os.chdir(path)
    
    list_file= []
    dict_data_struc ={}
    
    for current_feature in features:
    
        base_name = "*" + file_id + "*" + current_feature
        list_file.extend(natsorted(glob.glob(base_name)))
    
    for i, file in enumerate(list_file):
        dict_data_struc[i]={"filename": file, "crop":crop, "firstmon":firstmon}
        
    os.chdir(cwd)    
    return dict_data_struc
  
    
