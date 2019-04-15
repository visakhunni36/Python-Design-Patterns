# the command pattern 


class Order:
	"""The Invoker Class"""

	def __init__(self, placeOrederCmd, cancelOrderCmd):
		self.__placeOrderCommand = placeOrederCmd
		self.__cancelOrderCommand = cancelOrderCmd
		

	def placeOrder(self):
		self.__placeOrderCommand.execute()
		
	def cancelOrder(self):
		self.__cancelOrderCommand.execute()
		


class Supplier:
	"""The Receiver Class"""

	def confirmOrder(self):
		print('The Order is Confiremed')
		
	def deleteOrder(self):
		print('The Order is Cancelled')
		


class Command:
	"""The Command Abstract Class"""

	def __init__(self):
		# customize for your need
		pass

	def execute(self):
		# Override
		pass



class PlaceOrederCommand(Command):
	"""The Command Class for placing the order"""

	def __init__(self, supplier):
		self.__supplier = supplier
		
	def execute(self):
		self.__supplier.confirmOrder()
		


class CancelOrderCommand(Command):
	"""The Command Class for cancelling the oreder"""

	def __init__(self, supplier):
		self.__supplier = supplier
		
	def execute(self):
		self.__supplier.deleteOrder()
		


class Customer:
	"""The Client Class"""
	def __init__(self):
		self.__service_provider = Supplier()
		self.__placeOrder = PlaceOrederCommand(self.__service_provider)
		self.__cancelOrder = CancelOrderCommand(self.__service_provider)
		self.__order = Order(self.__placeOrder, self.__cancelOrder)

	def order(self, cmd):
		cmd = cmd.strip().upper()
		print(cmd)

		try:
			if cmd == 'CONFIRM':
				self.__placeOrder.execute()
			elif cmd == 'CANCEL':
				self.__cancelOrder.execute()
			else:
				print('Invalid COMMAND, Please Enter CONFIRM or CANCEL')
		except Exception as e:
			print('Exception')
		
		