

# python script

import observer



# create the publisher object
emailCampaign = observer.EmailCampaign()


# create the subscriber objects
client1 = observer.Client1()
client2 = observer.Client2()
marketingAgencies = observer.MarketingAgencies()


# register the subscribers
emailCampaign.register(client1)
emailCampaign.register(client2)
emailCampaign.register(marketingAgencies)



# broadcast new mail
emailCampaign.craftNewMail("Broadcasting Test Mail")


# unregister a client
emailCampaign.unregister(client2)


# braodcast new mail to the updated clientbase
emailCampaign.craftNewMail("Broadcasting Test Mail To New Client Base")































































































































































































