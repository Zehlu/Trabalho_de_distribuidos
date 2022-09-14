class Cliente:

    def __init__(self, Id):
        self.Id = Id
        self.srv = 0

    def sendMessage(self,remoteId, msg):
        self.srv.receiveMessage(self.Id, remoteId, msg)
        
    def checkMessage(self):
        print(self.srv.getMessage(self.Id))

    def connect(self, serv):
        self.srv = serv

    def desconnect(self):
        self.srv = None


class Server:

    def __init__(self):
        self.pending_msg = {}

    def receiveMessage(self, senderId, receiverId, msg):
        try:
            self.pending_msg.insert(receiverId , msg)
        except:
            self.pending_msg = {receiverId:msg}
        
    
    def getMessage(self, Id):
        try:
            return self.pending_msg[Id]
        except:
            return "Sem mensagens"

    
def Main():

    src = Server()
    cli1 = Cliente("jose")
    cli1.connect(src)
    cli2 = Cliente("maria")
    cli2.connect(src)
    
    
    cli1.sendMessage(cli2.Id,"teste")
    cli1.sendMessage(cli2.Id,"ter2ste")

    cli2.checkMessage()

    
    
    cli1.desconnect()
    cli2.desconnect()

    

Main()