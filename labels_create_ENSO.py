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
    
    aa9=[None]*122
    
    for i in range(122):
        aa9[i]=i+1896;
    
    aa=[None]*122
    
    for i in range(122):
        aa[i]='NE';
    
    aa[1897-1896-1]='EL';
    aa[1900-1896-1]='EL';
    aa[1903-1896-1]='EL';
    aa[1906-1896-1]='EL';
    aa[1915-1896-1]='EL';
    aa[1919-1896-1]='EL';
    aa[1926-1896-1]='EL';
    aa[1931-1896-1]='EL';
    aa[1941-1896-1]='EL';
    aa[1942-1896-1]='EL';
    aa[1958-1896-1]='EL';
    aa[1966-1896-1]='EL';
    aa[1973-1896-1]='EL';
    aa[1978-1896-1]='EL';
    aa[1980-1896-1]='EL';
    aa[1983-1896-1]='EL';
    aa[1987-1896-1]='EL';
    aa[1988-1896-1]='EL';
    aa[1992-1896-1]='EL';
    aa[1995-1896-1]='EL';
    aa[1998-1896-1]='EL';
    aa[2003-1896-1]='EL';
    aa[2007-1896-1]='EL';
    aa[2010-1896-1]='EL';
    
    aa[1904-1896-1]='LN';
    aa[1909-1896-1]='LN';
    aa[1910-1896-1]='LN';
    aa[1911-1896-1]='LN';
    aa[1917-1896-1]='LN';
    aa[1918-1896-1]='LN';
    aa[1925-1896-1]='LN';
    aa[1934-1896-1]='LN';
    aa[1939-1896-1]='LN';
    aa[1943-1896-1]='LN';
    aa[1950-1896-1]='LN';
    aa[1951-1896-1]='LN';
    aa[1955-1896-1]='LN';
    aa[1956-1896-1]='LN';
    aa[1962-1896-1]='LN';
    aa[1971-1896-1]='LN';
    aa[1974-1896-1]='LN';
    aa[1976-1896-1]='LN';
    aa[1989-1896-1]='LN';
    aa[1999-1896-1]='LN';
    aa[2000-1896-1]='LN';
    aa[2008-1896-1]='LN';
    aa[2011-1896-1]='LN';
    aa[2012-1896-1]='LN';
    
    
    aa[24-5-1]='CP';
    aa[50-5-1]='CP';
    aa[60-5-1]='CP';
    aa[73-5-1]='CP';
    aa[78-5-1]='CP';
    aa[87-5-1]='CP';
    aa[96-5-1]='CP';
    aa[100-5-1]='CP';
    aa[101-5-1]='CP';
    aa[104-5-1]='CP';
    aa[112-5-1]='CP';
    aa[113-5-1]='CP';
    aa[114-5-1]='CP';
    
    aa[92-5-1]='EL';
    aa[107-5-1]='EL';
    
    aa[118]='EL';
    aa[119]='EL';
    aa[120]='LN';
    aa[121]='LN';
    
    
    ##
    #labels for each set are as follows
    ##
    #AMSRE
    aa2=aa[106:115]
    # guess should be 
    aa2=aa[106:114]
    
    
    #COBE
    aa3=aa[0:121]
    #gues should be 
    aa3=aa[0:121]
    
    
    #ERSST
    aa4=aa
    
    #GODAS
    aa5=aa[84:122]
    
    #OISST
    aa6=aa[86:123]
    
    
    labels_train=aa+aa2+aa3+aa5+aa6
    labels_test=aa4

    return labels_train, labels_test
