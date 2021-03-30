class Test:
    def printOwing(selfObject):
        selfObject.printBanner()

        # print details
        print("name:", selfObject.name)
        print("amount:", selfObject.getOutstanding())
