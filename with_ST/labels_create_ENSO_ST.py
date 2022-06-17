#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:36:11 2019

@author: nicola
"""

## Nicolas horrible labels - needs cleaning
#create my list of classified parts
## start 1896v= - 2017
def create_labels():
    
    aa=[None]*124
    
    for i in range(124):
        aa[i]='NE';
    
    
    aa[1896-1896]='EL';
    aa[1899-1896]='EL';
    aa[1902-1896]='EL';
    aa[1905-1896]='EL';
    aa[1918-1896]='EL';
    aa[1925-1896]='EL';
    aa[1930-1896]='EL';
    aa[1941-1896]='EL';
    aa[1957-1896]='EL';
    aa[1965-1896]='EL';
    aa[1972-1896]='EL';
    aa[1979-1896]='EL';
    aa[1982-1896]='EL';
    aa[1987-1896]='EL';
    aa[1997-1896]='EL';
    aa[2006-1896]='EL';
    aa[2009-1896]='EL';
    aa[2014-1896]='EL';
    aa[2015-1896]='EL';
    aa[2018-1896]='EL';
    
    aa[1903-1896]='LN';
    aa[1908-1896]='LN';
    aa[1909-1896]='LN';
    aa[1910-1896]='LN';
    aa[1916-1896]='LN';
    aa[1917-1896]='LN';
    aa[1924-1896]='LN';
    aa[1933-1896]='LN';
    aa[1938-1896]='LN';
    aa[1942-1896]='LN';
    aa[1949-1896]='LN';
    aa[1950-1896]='LN';
    aa[1954-1896]='LN';
    aa[1955-1896]='LN';
    aa[1961-1896]='LN';
    aa[1970-1896]='LN';
    aa[1973-1896]='LN';
    aa[1975-1896]='LN';
    aa[1988-1896]='LN';
    aa[1998-1896]='LN';
    aa[1999-1896]='LN';
    aa[2007-1896]='LN';
    aa[2010-1896]='LN';
    aa[2011-1896]='LN';
    aa[2016-1896]='LN';
    aa[2017-1896]='LN';

    aa[1914-1896]='CP';
    aa[1940-1896]='CP';
    aa[1958-1896]='CP';
    aa[1963-1896]='CP';
    aa[1968-1896]='CP';
    aa[1977-1896]='CP';
    aa[1986-1896]='CP';
    aa[1990-1896]='CP';
    aa[1991-1896]='CP';
    aa[1994-1896]='CP';
    aa[2002-1896]='CP';
    aa[2003-1896]='CP';
    aa[2004-1896]='CP';
    aa[2019-1896]='CP';
    
    aa[1957-1896]='ST';
    aa[1965-1896]='ST';
    aa[1972-1896]='ST';
    aa[1987-1896]='ST';
    aa[1982-1896]='ST';
    aa[1997-1896]='ST';
    aa[2015-1896]='ST';
  
    1896
    ##
    #labels for each set are as follows
    #ERA 1854   start 0 : length ERA   - cute 42
    ERA=aa[0:123]
    ERA5=aa[0:124]
    #COBESST2 1850  start 0 : - cut 46
    COBE2=aa[0:123]
    #COBEv1 1891 start 0 - cute 5
    COBE1=aa[0:124]
    #GODAS 1980 start 84 
    GOD=aa[84:84+40]
    #Kaplan 1856 start 0 - cut 40
    KAP=aa[0:124]
    #GECCO2 1948 start 52
    GEC=aa[52:52+68]
    #OISST 09/1981 start 85
    OI=aa[86:86+38]
    #ORAs4 1958 start 62
    OR4=aa[62:62+59]
    #ORAs5 1979 start 83
    OR5=aa[83:83+39]
    #soda 1980 start 84
    SO1=aa[84:84+35]
    SO2=aa[84:84+37]
    SO3=aa[84:84+34]
    SO4=aa[84:84+38]
    SO5=aa[84:84+29]
    SO6=aa[84:84+36]
    #AMSRE 06/2002 106
    AM=aa[106:106+9]
    #HadISST 1870 start 0 cut 26
    HA=aa[0:123]
    
    
   

    
    
    labels_train=ERA+ERA+ERA5+COBE2+COBE1+GOD+KAP+GEC+OI+OR4+OR5+OR5+OR5+OR5+OR5+SO1+SO2+SO4+SO5+SO6+AM
    labels_test=HA
    
    #info for which year is which
    #t=[i+1896 for i in range(122)]
    
    #labels_train,labels_test=labels.create_labels()
    #idx = [i for i, x in enumerate(labels_test) if x=='LN']
    #a=[t[i] for i in idx]
    #a

    return labels_train, labels_test
