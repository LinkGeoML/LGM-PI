# PI
This repository contains the code and documentation for LGM-PI,
a QGIS plugin for classifying integrated polygons based on their provenance information, in cadastration processes.
This repository includes the qgis plugin as an extent of the LGM-Polygon Classification library. The dependencies are 
the ones that are mandatory to execute the Polygon-Classification Library.
There are two separated sections when executing the plugin. The first one is the training section, where the algorithm is
trained based on the classifier that the user has chosen.Train the algorithm using csv files containing a collection of matched
polygon pairs. The second one is the evaluating section. 

Available classifiers are: 

 * SVM (Support Vector Machine),
  
 * Decision Tree,
  
 * Random Forest,
  
 * Extra Trees,
  
 * XGBoost,
  
  * MLP (Multi Layer Perceptron)
  
  
Furthermore, after training the algorithm, the user is able to use a dataset (.csv) with polygon multipoints and extract the appropriate
information (evaluate section).If the user had chosen more than one classifier in the training part, the best score classifier is used 
in the evaluation division.


# Model Training

* Step 1 

The user defines the dataset that is going to be used during the training section, through the Train Data button.

* Step 2

The user defines the classifier(s) in order to produce the appropriate models when the training is completed by selecting the 
checkboxes from the Set Classifier(s) section.

* Step 3

The user starts the training procedure through Run Model Training button.

# Evaluating Section

* Step 1

The user defines the dataset that is going to be classified through the Test Data button.

* Step 2

The user selects the desired classifier in order to execute the evaluation of the dataset. The classifier should be one of 
the classifiers that was used during the training procedure.

* Step 3 

The evaluation of the input dataset is executed by pressing the Model Evaluation button.


