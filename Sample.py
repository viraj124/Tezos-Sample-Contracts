import smartpy as sp
class EventPlanner(sp.Contract):
    def __init__(self, initialOwner):
        self.init(owner = initialOwner,
                  nameToEvent = sp.map(tkey = sp.TString))
    @sp.entryPoint
    def setDate(self, params):
        sp.verify(sp.sender == self.data.owner)
        self.checkEvent(params.name)
        self.data.nameToEvent[params.name].date = params.newDate
    @sp.entryPoint
    def setNumGuests(self, params):
        sp.verify(sp.sender == self.data.owner)
        self.checkEvent(params.name)
        self.data.nameToEvent[params.name].numGuests = params.newNumGuests
    @sp.entryPoint
    def changeOwner(self, params):
        sp.verify(sp.sender == self.data.owner)
        self.data.owner = params.newOwner
    def checkEvent(self, name):
        sp.if ~(self.data.nameToEvent.contains(name)):
            self.data.nameToEvent[name] = sp.record(date = "", numGuests = 0)
