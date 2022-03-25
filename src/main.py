"""
Masterlist

A List Generator-typed Android application designed to be Quality-of-life focused.

GitHub URL: https://github.com/Thanatisia/masterlist-app
"""

# Import Internal Libraries
import os
import sys

# Import External Libraries
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# Import self-defined user libraries
import modules.settings as settings
from modules.settings import app, database


class MyLayouts():
	"""
	Hold my design, layouts and elements
	"""
	class Grid():
		"""
		Grid Layout design
		"""


class GUI(App): # Automatically call constructor 'App'
	"""
	Main Mobile Application
	"""
	def build(self):
		# Return what you want to draw
		grids = MyLayouts().Grid()
		return grids

def init():
	"""
	Class Initialization
	"""
	PROJ_INFO = app.init("Masterlist", "v20220324_1", "https://github.com/Thanatisia/masterlist-app")
	DB_INFO = database.init("MyDB", "1", "root", "")
	
	print(PROJ_INFO)
	print(DB_INFO)
	
def main():
	"""
	Main Program
	"""
	gui = GUI()
	gui.run()	

if __name__ == "__main__":
	init()
	main()