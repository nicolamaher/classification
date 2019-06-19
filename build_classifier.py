#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  10 2019

@author: nicola
this code uses observations to build a ENSO classifier
"""

# import modules
##
# import build-in
import numpy as np

# import local
import utility_classification as ut_cla
import labels_create_ENSO as labels
##
#set up path and files for observations and take the DJF mean values
##
path = '/home/nicola/Data2/obs/raw/Reanalysis/'


#create dictionary with all input data
dict_data_struc ={
        1:{'filename' : 'HadISST_processed.nc_nino3.nc',
           'crop' : 26,
           'firstmon' :10},
        2:{'filename' : 'HadISST_processed.nc_nino4.nc',
           'crop' : 26,
           'firstmon' :10},
        3:{'filename' : 'HadISST_processed.nc_nino12.nc',
           'crop' : 26,
           'firstmon' :10},
        4:{'filename' : 'AMSRE_processed.nc_nino3.nc',
           'crop' : 0,
           'firstmon' :4},
        5:{'filename' : 'AMSRE_processed.nc_nino4.nc',
           'crop' : 0,
           'firstmon' :4},
        6:{'filename' : 'AMSRE_processed.nc_nino12.nc',
           'crop' : 0,
           'firstmon' :4}, 
        7:{'filename' : 'COBE_processed.nc_nino3.nc',
           'crop' : 46,
           'firstmon' :10},
        8:{'filename' : 'COBE_processed.nc_nino4.nc',
           'crop' : 46,
           'firstmon' :10},
        9:{'filename' : 'COBE_processed.nc_nino12.nc',
           'crop' : 46,
           'firstmon' :10}, 
        10:{'filename' : 'GODAS_processed.nc_nino3.nc',
           'crop' : 0,
           'firstmon' :10},
        11:{'filename' : 'GODAS_processed.nc_nino4.nc',
           'crop' : 0,
           'firstmon' :10},
        12:{'filename' : 'GODAS_processed.nc_nino12.nc',
           'crop' : 0,
           'firstmon' :10}, 
        13:{'filename' : 'OISST_processed.nc_nino3.nc',
           'crop' : 0,
           'firstmon' :10},
        14:{'filename' : 'OISST_processed.nc_nino4.nc',
           'crop' : 0,
           'firstmon' :10},
        15:{'filename' : 'OISST_processed.nc_nino12.nc',
           'crop' : 0,
           'firstmon' :10},       
        16:{'filename' : 'ERSST_processed.nc_nino3.nc',
           'crop' : 42,
           'firstmon' :10},
        17:{'filename' : 'ERSST_processed.nc_nino4.nc',
           'crop' : 42,
           'firstmon' :10},
        18:{'filename' : 'ERSST_processed.nc_nino12.nc',
           'crop' : 42,
           'firstmon' :10}
                 }

#process all data
result = ut_cla.preprocess_from_dict(dict_data_struc, path, verbose=True)

# Concatenate 
def concat_features(result, keys, axis=0):
    list_= [result[key] for key in keys]
    return np.concatenate(list_,axis=axis)
    
keys=[1,4,7,10,13] # key to concatenate
concat_N3= concat_features(result, keys)

keys=[2,5,8,11,14] # key to concatenate
concat_N4= concat_features(result, keys)

keys=[3,6,9,12,15] # key to concatenate
concat_N12= concat_features(result, keys)
##

input_train=np.concatenate([concat_N3,concat_N4,concat_N12],axis=1)

keys=[16,17,18] # key to concatenate
input_test= concat_features(result, keys, axis=1)


#create labels
labels_train,labels_test=labels.create_labels()


#import the machine learning tools

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib

#h = .02  # step size in the mesh


names = ["NearestNeighbors", "LinearSVM", "RBFSVM","DecisionTree", "RandomForest", "NeuralNet", "AdaBoost",
         "NaiveBayes", "QDA"]

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    #GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1, max_iter=400),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]


#classify!
    
for name, clf in zip(names, classifiers):
    print name
    #ax = plt.subplot(1, len(classifiers) + 1, i)
    clf.fit(input_train, labels_train)
    score = clf.score(input_test, labels_test)
    print score
    print(name, cross_val_score(clf, input_train, labels_train, cv=5).mean())
    ##TODO
    # do youstratify your data during the cross validation?
    filename = name+'.sav'
    joblib.dump(clf, filename)
# Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    #if hasattr(clf, "decision_function"):
     #   Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    #else:
     #   Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
        # Put the result into a color plot
    #Z = Z.reshape(xx.shape)
    #ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)


names_F=["O N3","N N3", "D N3", "J N3", "F N3", "M N3","O N4","N N4", "D N4", "J N4", "F N4", "M N4","O N12","N N12", "D N12", "J N12", "F N12", "M N12"]
names_F2=["O N3","N N3", "D N3", "J N3", "F N3", "M N3","O N4","N N4", "D N4", "J N4", "F N4", "M N4","O N12","N N12", "D N12", "J N12", "F N12", "M N12"]

import matplotlib.pyplot as plt

classifiers = [DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    AdaBoostClassifier()]
for name, clf in zip(names, classifiers):
    #ax = plt.subplot(1, len(classifiers) + 1, i)
    clf.fit(input_train, labels_train)
    importances = clf.feature_importances_
    indices = np.argsort(importances)[::-1]
    for f in range(input_train.shape[1]):
        names_F2[f]=names_F[indices[f]]

# Print the feature ranking
    print("Feature ranking:")

    for f in range(input_train.shape[1]):
        print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))
        # Plot the feature importances of the forest
    #plt.figure()
    plt.title("Feature importances")
    plt.bar(range(input_train.shape[1]), importances[indices])
        #color="r", yerr=std[indices], align="center")
    plt.xticks(range(input_train.shape[1]), names_F2)#[indices.astype(int)])
    #plt.xlim([-1, input_train.shape[1]])
    plt.xticks(rotation=90)
    plt.show()















