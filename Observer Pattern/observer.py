

# the observer pattern

class Publisher:
    def __init__(self):
        # make it uninheritable
        pass

    def register(self):
        # Override
        pass

    def unregister(self):
        # Override
        pass

    def broadcast(self):
        # Override
        pass



class EmailCampaign(Publisher):
    def __init__(self):
        self._listOfClients = []
        self.emailSubject = None
        
    def register(self, clientObj):
        if clientObj not in self._listOfClients:
            self._listOfClients.append(clientObj)

    def unregister(self, clientObj):
        self._listOfClients.remove(clientObj)
        
    def broadcast(self):
        for objects in self._listOfClients:
            objects.sendMail(self.emailSubject)
        
    def craftNewMail(self, emailSubject):
        # User creates a new mail
        self.emailSubject = emailSubject
        # When sends the mail is broadcasted to all
        self.broadcast()
        

class Subscriber:
    def __init__(self):
        # make it uninheritable
        pass

    def sendMail(self):
        # Override
        pass



class Client1(Subscriber):
    def sendMail(self, emailSubject):
        print('A new mail %s is send to client1' %emailSubject)
        

class Client2(Subscriber):
    def sendMail(self, emailSubject):
        print('A new mail %s is send to client2' %emailSubject)


class MarketingAgencies(Subscriber):
    def __init__(self):
        self._marketingAgencies = ['Agency1', 'Agency2', 'Agency3']

    def sendMail(self, emailSubject):
        for agency in self._marketingAgencies:
            print('A new mail %s is send to Marketing %s' %(emailSubject, agency))
        


        
















































































































































































































































































