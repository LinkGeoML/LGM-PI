import os,subprocess
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
from qgis.core import *
from qgis.gui import *
from PyQt5.QtWidgets import QPushButton,QFileDialog,QProgressBar,QMessageBox

FORM_CLASS1, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'training_section_dialog.ui'))
class PolygonClassificationTrainingDialog(QtWidgets.QDialog, FORM_CLASS1):	
	def __init__(self,parent=None):
		"""Constructor."""
		super(PolygonClassificationTrainingDialog, self).__init__(parent)
		self.setupUi(self)
		self.trainbtn.clicked.connect(self.trainbtn_clicked)
		self.run_model_trainingbtn.clicked.connect(self.run_model_trainingbtnclicked)
		self.clearbtn.clicked.connect(self.clearbtn_clicked)
	
	def trainbtn_clicked(self):
		QMessageBox.information(self,"INFO","Please select a training dataset (.csv)")
		try:
			train_file_dir = QFileDialog()
			full_dir=str(train_file_dir.getOpenFileName(self,"Select Train CSV",os.getcwd()))
			file_name=full_dir[2:full_dir.index("'",4,1000)]
			self.train_data_chosen_file.setText(file_name)
		
		except FileNotFoundError:
			QMessageBox.warning(self,"CAUTION","Please choose training dataset to proceed")
			self.train_data_chosen_file.clear()
			
	def run_model_trainingbtnclicked(self):

		checkbox_list = []
		if self.checkBox_svm.isChecked():
			checkbox_list.append(self.checkBox_svm.text())
		if self.checkBox_decisionTree.isChecked():
			checkbox_list.append(self.checkBox_decisionTree.text())
		if self.checkBox_randomForest.isChecked():
			checkbox_list.append(self.checkBox_randomForest.text())
		if self.checkBox_extraTrees.isChecked():
			checkbox_list.append(self.checkBox_extraTrees.text())
		if self.checkBox_xgboost.isChecked():
			checkbox_list.append(self.checkBox_xgboost.text())
		if self.checkBox_mlp.isChecked():
			checkbox_list.append(self.checkBox_mlp.text())
		
		if "LGM-PolygonClassification-master" in str(os.getcwd()):
			pass
		else:
			os.chdir(os.getcwd()+"\\LGM-PolygonClassification-master")
		fpath = self.train_data_chosen_file.text()
		
		temp11 = str(checkbox_list).replace("[","").replace("]","").replace("'",'').replace(" ","")
		
		while len(temp11)>3:
			command = f'python -m polygon_classification.cli train --dataset {fpath} --classifiers {temp11}'
			print(command)
			progress = QProgressBar()
			progress.setGeometry(200, 80, 250, 20)
			progress.move(600,600)
			progress.setWindowTitle('Processing..')
			progress.setAlignment(QtCore.Qt.AlignCenter)
			progress.show()				
			try:
				output = subprocess.check_output(command,shell=True,stderr=subprocess.STDOUT)
			except subprocess.CalledProcessError:
				QMessageBox.warning(self,"WARNING","Execution of command failed")
		
			QMessageBox.information(self,"INFO",str(output))
			break
		while len(fpath)<2:
			QMessageBox.warning(self,"WARNING","Please choose training dataset to proceed")
			break
		while len(temp11)<4:
			QMessageBox.warning(self,"WARNING","Please choose classifier to proceed")
			break
		
	def clearbtn_clicked(self):
		self.checkBox_svm.setCheckState(Qt.Unchecked)
		self.checkBox_decisionTree.setCheckState(Qt.Unchecked)
		self.checkBox_randomForest.setCheckState(Qt.Unchecked)
		self.checkBox_extraTrees.setCheckState(Qt.Unchecked)
		self.checkBox_xgboost.setCheckState(Qt.Unchecked)
		self.checkBox_mlp.setCheckState(Qt.Unchecked)	
		
