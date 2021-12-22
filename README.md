README: 

Folders:
Input files are in the folder obs

Files for the classifier that includes strong events are in the folder include ST

classifier_model_output contains the output from the classified SMILEs

Import python environment:
To use the python environment type: environement conda env create --file environment.yaml

Jupyter notebooks: 
Final classifier:
build_ensemble_classifier → creates the final classifier
ensemble_classifier_final.sav is the saved final classifier

Tests:
2 step classifier → tests a classifier that first classifier into El Nino, La Nina and netural, then in a second step classifies El Ninos into EP and CP

test_features → tests a range of input features

test_final_classifier_fulldata → tests using all SST data in the region rather than nino boxes

test_classifier_augmentation_split → test the choice of training/evaluation data split

Optimisation:
Scripts called opimise- test the hyperparametrs and optimise them for use in the final classifier for each of the classification algorithms

Other code:
labels_create_ENSO → creates labels for the input observed data
utility_classification → has the functions used in the code


