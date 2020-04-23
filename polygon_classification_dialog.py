# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PolygonClassificationDialog
                                 A QGIS plugin
 A python library for accurate classification of polygon types
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Eratosthenis sa
        email                : iliasvrk@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os,subprocess

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
from qgis.core import *
from qgis.gui import *
from PyQt5.QtWidgets import QPushButton,QFileDialog,QProgressBar,QMessageBox

from .polygon_classification_dialog2 import PolygonClassificationTrainingDialog

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'polygon_classification_dialog_base.ui'))


class PolygonClassificationDialog(QtWidgets.QDialog, FORM_CLASS):
	def __init__(self, parent=None):
		"""Constructor."""
		super(PolygonClassificationDialog, self).__init__(parent)
		# Set up the user interface from Designer through FORM_CLASS.
		# After self.setupUi() you can access any designer object by doing
		# self.<objectname>, and you can use autoconnect slots - see
		# http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
		# #widgets-and-dialogs-with-auto-connect
		self.setupUi(self)
		self.classifier_combo_box(self.classifier_comboBox)
		self.testbtn.clicked.connect(self.testbtn_clicked)
		self.model_evaluationbtn.clicked.connect(self.model_evaluationbtn_clicked)
		self.training_sectionbtn.clicked.connect(self.training_sectionbtn_clicked)
		
		default_path=QgsApplication.qgisSettingsDirPath() + "\python\plugins"  #OS independent default  path for qgis plugins
		os.chdir(default_path)
        	temp1=os.getcwd()
		temp2=os.listdir(path=str(temp1))               

		if 'polygon_classification' in temp2:
			os.chdir('.\polygon_classification') 
		
	def training_sectionbtn_clicked(self):
		self.dlg = PolygonClassificationTrainingDialog()
		self.dlg.show()
		
		
	def clearbtn_clicked(self):
		self.checkBox_svm.setCheckState(Qt.Unchecked)
		self.checkBox_decisionTree.setCheckState(Qt.Unchecked)
		self.checkBox_randomForest.setCheckState(Qt.Unchecked)
		self.checkBox_extraTrees.setCheckState(Qt.Unchecked)
		self.checkBox_xgboost.setCheckState(Qt.Unchecked)
		self.checkBox_mlp.setCheckState(Qt.Unchecked)		
		
	
	def classifier_combo_box(self,componame):
		componame.addItem("\"SVM\"")
		componame.addItem("\"DecisionTree\"")
		componame.addItem("\"RandomForest\"")
		componame.addItem("\"ExtraTrees\"")
		componame.addItem("\"XGBoost\"")
		componame.addItem("\"MLP\"")
		
	
	
	
	def testbtn_clicked(self):
		try:
			test_file_dir = QFileDialog()
			fulldir=str(test_file_dir.getOpenFileName(self,"Select Train CSV File",os.getcwd()))
			file_name=fulldir[2:fulldir.index("'",4,1000)]
			self.test_data_chosen_file.setText(file_name)
		
		except FileNotFoundError:
			QMessageBox.warning(self,"CAUTION","No train data specified")
			self.test_data_chosen_file.clear()
		
	def model_evaluationbtn_clicked(self):	
		if "LGM-PolygonClassification-master" in str(os.getcwd()):
			pass
		else:
			#os.chdir()
			os.chdir(os.getcwd()+"\\LGM-PolygonClassification-master")
		#choose test dataset file
		file_path = self.test_data_chosen_file.text()
		temp12 = str(file_path).replace("[","").replace("]","").replace("'",'').replace(" ","")
		
		
		
		#choose classifier
		theclassifierstr=self.classifier_comboBox.itemText(self.classifier_comboBox.currentIndex())
		theclassifierstr=theclassifierstr.replace('"',"")
		
		evaluation_cmd = f'python -m polygon_classification.cli evaluate --dataset {temp12} --classifier {theclassifierstr}'
		#need to check if the selected classifier-model exists inside models folder
		if theclassifierstr=="SVM":
			
			if os.path.exists(os.getcwd()+"\\models\\SVM_model.joblib"):
				QMessageBox.information(self,"INFO","The selected model exists. You may proceed")
				try:
					progress = QProgressBar()
					progress.setGeometry(200, 80, 250, 20)
					progress.move(600,600)
					progress.setWindowTitle('Processing..')
					progress.setAlignment(QtCore.Qt.AlignCenter)
					progress.show()
					
					output = subprocess.check_output(evaluation_cmd,shell=True,stderr=subprocess.STDOUT)
				except subprocess.CalledProcessError:
					QMessageBox.warning(self,"WARNING",str(output))
				#print(output)	
				QMessageBox.information(self,"OUTPUT",str(output))
			else:
				QMessageBox.information(self,"INFO","The selected classifier does not exist. Choose again")
		
		if theclassifierstr=="DecisionTree":
			if os.path.exists(os.getcwd()+"\\models\\DecisionTree_model.joblib"):
				QMessageBox.information(self,"INFO","The selected model exists. You may proceed")
				try:
					progress = QProgressBar()
					progress.setGeometry(200, 80, 250, 20)
					progress.move(600,600)
					progress.setWindowTitle('Processing..')
					progress.setAlignment(QtCore.Qt.AlignCenter)
					progress.show()
				
					output = subprocess.check_output(evaluation_cmd,shell=True,stderr=subprocess.STDOUT)
				except subprocess.CalledProcessError:
					QMessageBox.warning(self,"WARNING",str(output))
				#print(output)	
				QMessageBox.information(self,"OUTPUT",str(output))
			else:
				QMessageBox.information(self,"INFO","The selected classifier does not exist. Choose again")				
		
		if theclassifierstr=="RandomForest":
		
			if os.path.exists(os.getcwd()+"\\models\\RandomForest_model.joblib"):
				QMessageBox.information(self,"INFO","The selected model exists. You may proceed")
				try:
					progress = QProgressBar()
					progress.setGeometry(200, 80, 250, 20)
					progress.move(600,600)
					progress.setWindowTitle('Processing..')
					progress.setAlignment(QtCore.Qt.AlignCenter)
					progress.show()
				
					output = subprocess.check_output(evaluation_cmd,shell=True,stderr=subprocess.STDOUT)
				except subprocess.CalledProcessError:
					QMessageBox.warning(self,"WARNING",str(output))
				#print(output)	
				QMessageBox.information(self,"OUTPUT",str(output))				
			else:
				QMessageBox.information(self,"INFO","The selected classifier does not exist. Choose again")
		
		if theclassifierstr=="ExtraTrees":
			if os.path.exists(os.getcwd()+"\\models\\ExtraTrees_model.joblib"):
				QMessageBox.information(self,"INFO","The selected model exists. You may proceed")
				try:
					progress = QProgressBar()
					progress.setGeometry(200, 80, 250, 20)
					progress.move(600,600)
					progress.setWindowTitle('Processing..')
					progress.setAlignment(QtCore.Qt.AlignCenter)
					progress.show()
				
					output = subprocess.check_output(evaluation_cmd,shell=True,stderr=subprocess.STDOUT)
				except subprocess.CalledProcessError:
					QMessageBox.warning(self,"WARNING",str(output))
				print(output)	
				QMessageBox.information(self,"OUTPUT",str(output))				
			else:
				QMessageBox.information(self,"INFO","The selected classifier does not exist. Choose again")
				
		if theclassifierstr=="XGBoost":
			if os.path.exists(os.getcwd()+"\\models\\XGBoost_model.joblib"):
				QMessageBox.information(self,"INFO","The selected model exists. You may proceed")
				try:
					progress = QProgressBar()
					progress.setGeometry(200, 80, 250, 20)
					progress.move(600,600)
					progress.setWindowTitle('Processing..')
					progress.setAlignment(QtCore.Qt.AlignCenter)
					progress.show()
				
					output = subprocess.check_output(evaluation_cmd,shell=True,stderr=subprocess.STDOUT)
				except subprocess.CalledProcessError:
					QMessageBox.warning(self,"WARNING",str(output))
				#print(output)	
				QMessageBox.information(self,"OUTPUT",str(output))				
			else:
				QMessageBox.information(self,"INFO","The selected classifier does not exist. Choose again")
		
		if theclassifierstr=="MLP":
			if os.path.exists(os.getcwd()+"\\models\\MLP_model.joblib"):
				QMessageBox.information(self,"INFO","The selected model exists. You may proceed")
				try:
					progress = QProgressBar()
					progress.setGeometry(200, 80, 250, 20)
					progress.move(600,600)
					progress.setWindowTitle('Processing..')
					progress.setAlignment(QtCore.Qt.AlignCenter)
					progress.show()
				
					output = subprocess.check_output(evaluation_cmd,shell=True,stderr=subprocess.STDOUT)
				except subprocess.CalledProcessError:
					QMessageBox.warning(self,"WARNING",str(output))
				#print(output)	
				QMessageBox.information(self,"OUTPUT",str(output))				
			else:
				QMessageBox.information(self,"INFO","The selected classifier does not exist. Choose again")
		QWidget.update(self)
		
		
		
