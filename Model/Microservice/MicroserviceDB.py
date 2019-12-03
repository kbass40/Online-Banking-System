import sys
import os
from pathlib import Path

path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')

from Misc import Time as Time

class DB():
	def __init__(self): pass

class DBConnection(DB):
	def __init__(self):
		pass

class TestDBConnection(DB):
	def __init__(self):
		pass


