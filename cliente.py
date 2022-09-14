class Cliente:

    def __init__(self, Id):
        self.Id = Id

    def sendMessage(self,remoteId, msg, server):
        server.receiveMessage(self.Id, remoteId, msg)
        
    def checkMessage(self,server):
        print(server.getMessage(self.Id))


    
def Main():

    

Main()