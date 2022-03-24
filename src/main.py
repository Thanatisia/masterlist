"""
Masterlist

A List Generator-typed Android application designed to be Quality-of-life focused.

GitHub URL: https://github.com/Thanatisia/masterlist-app
"""

# Import Internal Libraries
import os
import sys
import kivy

# Import External Libraries
import modules.settings as settings
from modules.settings import app, database


def init():
	"""
	Class Initialization
	"""
	PROJ_INFO = app.init("Masterlist", "v20220324_1", "https://github.com/Thanatisia/masterlist-app")
	DB_INFO = database.init("MyDB", "1", "root", "")

	print(PROJ_INFO)
	print(DB_INFO)

def main():
	print("Hello World")		

if __name__ == "__main__":
	init()
	main()