
class Server:

    def __init__(self):
        self.pending_msg = []

    def receiveMessage(self, senderId, receiverId, msg):
        self.pending_msg = [senderId, receiverId, msg]
    
    def getMessage(self, Id):
        if (Id == self.pending_msg[1]):
            return self.pending_msg

    

