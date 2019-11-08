

class DatabaseConnection():
	def foo(self, a): pass

class DBConnection(DatabaseConnection):
	def foo(self, a):
		return a

class TestDBConnection(DatabaseConnection):
	def foo(self, a):
		return "test"