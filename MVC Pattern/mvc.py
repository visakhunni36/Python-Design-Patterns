
# mvc core

# import libraries
import sqlite3
import types


# define model
class ComplaintModel:
	def getComplaintList(self, customer):
		query = "SELECT rowid FROM complaints WHERE Customer = '%s' " %customer
		complaintlist = self._dbselect(query)
		resultlist = []
		for row in complaintlist:
			resultlist.append(row[0])
		return resultlist
	
	def getContent(self, id):
		query = "SELECT Content FROM complaints WHERE rowid = %d " %id
		complaint = self._dbselect(query)
		for row in complaint:
			return row[0]
		
	def _dbselect(self, query):
		connection = sqlite3.connect('customer_support.db')
		cursorObj = connection.cursor()
		results = cursorObj.execute(query)
# 		connection.commit()
# 		cursorObj.close()
		return results
		



# define view
class ComplaintView:
	def content(self, content, complaint_id):
		print("### Complaints content for complaint # %d ### \n %s" %(complaint_id, content))

	def complaintList(self, complaintlist, customer):
		print("### Complaint List for %s ###\n" % customer)
		for complaint in complaintlist:
			print(complaint)
		


# define controller
class Controller:
	def __init__(self):
		pass

	def getComplaintContent(self, complaint_id):
		model = ComplaintModel()
		view = ComplaintView()
		content_data = model.getContent(complaint_id)
		return view.content(content_data, complaint_id)
		
	def getComplaintList(self, customer):
		model = ComplaintModel()
		view = ComplaintView()
		complaintlist_data = model.getComplaintList(customer)
		return view.complaintList(complaintlist_data, customer)
		






















































































































































































