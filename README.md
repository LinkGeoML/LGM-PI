# PI
This repository contains the code and documentation for LGM-PI,
a QGIS plugin for classifying integrated polygons based on their provenance information, in cadastration processes.
This repository includes the qgis plugin as an extent of the LGM-Polygon Classification library. The dependencies are 
the ones that are mandatory to execute the Polygon-Classification Library.
There are two separated sections when executing the plugin. The first one is the training section, where the algorithm is
trained based on the classifier that the user has chosen.Train the algorithm using csv files. The second one is the evaluating section. 

Available classifiers are: 
  SVM (Support Vector Machine)
  Decision Tree
  Random Forest
  Extra Trees
  XGBoost
  MLP (Multi Layer Perceptron)
  
Furthermore, after training the algorithm, the user is able to use a dataset (.csv) with polygon multipoints and extract the appropriate
information (evaluate section).If the user had chosen more than one classifier in the training part, the best score classifier is used 
in the evaluation division.
