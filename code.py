class Test:
    def printOwingTest(selfObject):
        selfObject.printBanner()
        selfObject.printDetails(selfObject.getOutstanding())

    def printDetailsTest(selfObject, outstanding):
        print("name:", selfObject.name)
        print("amount:", outstanding)
