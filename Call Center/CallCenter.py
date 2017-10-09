
from Call import Call

class CallCenter(object):
    calls = []
    def __init__(self):
        self.calls = CallCenter.calls
        self.queue = len(CallCenter.calls)

    def info(self):
        if len(self.calls) > 0:
            for call in self.calls:
                print "Call Id: "+ str(call.uniqueId)
                print "Caller Name: "+call.name
                print "Caller Phone Number: "+call.phone
                print "Time of Call: "+ str(call.timeOfCall.strftime("%c"))
                print "Reason: "+call.reason
                print "====================================="


    def add_call(self,name,phone,reason):
        call = Call(name,phone,reason)
        CallCenter.calls.append(call)


        return self

    def queue_size(self):
        if len(self.calls) <=0:
            print "No calls in Queue"
        else:
            print "Queue Size is: " + str(len(CallCenter.calls))
        return self

    def remove(self, remphone):
        if len(self.calls) <=0:
            print "No calls in Queue"
        else:
            for call in self.calls:
                if remphone == call.phone:
                    self.calls.pop(self.calls.index(call))
                    print "removed " + call.phone
                    #self.info()
                else:
                    print str(remphone)+" not in queue"


        return self



Dell = CallCenter()
#.add_call('Carlos',"6479286874","techsupport").add_call("Amanda","23423423","dunno how to use computer")
Dell.add_call('Carlos',"6479286874","techsupport").add_call("Amanda","23423423","dunno how to use computer").queue_size().info()
Dell.remove("23423423").info()
