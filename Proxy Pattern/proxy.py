
# The Proxy Pattern

import time

class Manager:
	def work(self):
		pass

	def tak(self):
		pass


class SalesManager(Manager):
	def work(self):
		print('The SalesManager is working')

	def talk(self):
		print('The SalesManager is talking')



class Proxy(Manager):
	def __init__(self):
		self.busy = 'No'
		self.sales = None

	def work(self):
		if self.busy == 'Yes':
			self.sales = salesManager()
			time.sleep(2)
			self.sales.talk()
		else:
			time.sleep(2)
			print('The SalesManager is busy')












































