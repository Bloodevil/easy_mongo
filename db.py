from pymongo import MongoClient

class Mongo(object):
	_connection = None
	def __init__(self, *args):
		if args:
			self.connect(*args)

	def connect(self, *args):
		self._connection = MongoClient(*args)
	def __getattr__(self, db):
		return getattr(self._connection, db)

	def __getitem__(self, db):
		return self._connection[db]

mongo = Mongo()
