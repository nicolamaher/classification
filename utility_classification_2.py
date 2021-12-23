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
    x = np.array(x)
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
        x2=np.zeros((full_size,30,121))
        x2[0:len(x),:,:]=x
    elif residual_month != 0:
        x2=x[:-residual_month,:,:]
    elif residual_month == 0 :
        x2=x
    
    x2_move_month=x2[firstmon-1:firstmon-13,:,:]    
    x_reshaped = x2_move_month.reshape((-1,12,3630))
    x_crop_b = x_reshaped[crop:,:-no_months,:]
    x_crop = x_crop_b.reshape((-1,21780))
    
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

# Concatenate 
def concat_features(result, keys, axis=0):
    '''
    this concatanates the model data
    '''
    list_= [result[key] for key in keys]
    return np.concatenate(list_,axis=axis)


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



    
