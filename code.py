class Test:
    def printOwing(selfObject):
        selfObject.printBanner()
        selfObject.printDetails(selfObject.getOutstanding())

    def printDetails(selfObject, outstanding):
        print("name:", selfObject.name)
        print("amount:", outstanding)
