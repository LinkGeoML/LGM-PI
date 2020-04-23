
import os,subprocess

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
from qgis.core import *
from qgis.gui import *
from PyQt5.QtWidgets import QPushButton,QFileDialog,QProgressBar,QMessageBox
#from .polygon_classification_dialog2 import PolygonClassificationTrainingDialog


FORM_CLASS1, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'training_section_dialog.ui'))
class PolygonClassificationTrainingDialog(QtWidgets.QDialog, FORM_CLASS1):	
	def __init__(self,parent=None):
		"""Constructor."""
		super(PolygonClassificationTrainingDialog, self).__init__(parent)
		# Set up the user interface from Designer through FORM_CLASS.
		# After self.setupUi() you can access any designer object by doing
		# self.<objectname>, and you can use autoconnect slots - see
		# http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
		# #widgets-and-dialogs-with-auto-connect
		
		self.setupUi(self)

