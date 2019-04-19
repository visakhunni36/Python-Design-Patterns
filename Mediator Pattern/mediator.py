

# The Mediator Pattern 

import time

class TC:
	def __ini__(self):
		self._tm = tm
		self._bProblem = 0
		
	def setup(self):
		print('Setting up the test')
		time.sleep(1)
		self._tm.prepareReporting()

	def execute(self):
		if not self._bProblem:
			print('Executing the test')
			time.sleep(1)
		else:
			print('Problem in setup. Test not executed')

	def tearDown(self):
		if not self._bProblem:
			print('Tearing down')
			time.sleep(1)
			self._tm.publishReport()
		else:
			print('Test not executed. No tear down required')

	def setTM(self, tm):
		self._tm = tm
		
	def setProblem(self, value):
		self._bProblem = value
		


class Reporter:
	def __init__(self):
		self._tm = None

	def prepare(self):
		print('Reporter class is preparing to report the results')
		time.sleep(1)

	def report(self):
		print('Reporting the results of the Test')
		time.sleep(1)
		
	def setTM(self, tm):
		self._tm = tm
		

class DB:
	def __init__(self):
		self._tm = None

	def insert(self):
		print('Insert the execution begin status in the DB')		
		time.sleep(1)
		
		# simulating the communication from TC to DB
		import random
		if random.randrange(1,4) == 3:
			return -1

	def update(self):
		print('Updating the test results in Database')
		
	def setTM(self, tm):
		self._tm = tm
		pass


# define the mediator
class TestManager:
	def __init__(self):
		self._reporter = None
		self._db = None
		self._tc = None
	
	def prepareReporting(self):
		rvalue = self._db.insert()
		if rvalue == -1:
			self._tc.setProblem(1)
			self._reporter.prepare()
		else:
			self._tc.setProblem(0)

	def setReporter(self, reporter):
		self._reporter = reporter
		
	def setDB(self, db):
		self._db = db
		
	def publishReport(self):
		self._db.update()
		rvalue = self._reporter.report()

	def setTC(self, tc):
		self._tc = tc










		








		








		








		








		








		








		