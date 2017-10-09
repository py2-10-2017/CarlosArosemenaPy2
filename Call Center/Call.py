from datetime import datetime
class Call(object):
    callId = 1
    def __init__(self,name,phone,reason):
        self.uniqueId = Call.callId
        self.name = name
        self.phone = phone
        self.timeOfCall = datetime.now()
        self.reason = reason
        Call.callId += 1

    def display(self):

        print "======================================="
        print "Unique Id: "+ str(self.uniqueId)
        print "Caller Name: "+ self.name
        print "Caller Phone Number: "+ self.phone
        print "Time of Call: "+ str(self.timeOfCall.strftime("%c"))
        print "Reason for call: "+ self.reason
        print "======================================="
