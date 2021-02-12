class Debugger():
    """A class to debug during development"""

    def __init__(self):
        self.debuglist = []

    def debug(self, obj):
        self.debuglist.append(obj)

    def printDebugs(self):
        for obj in self.debuglist:
            print(obj)
        # self.clearDebugs()

    def clearDebugs(self):
        self.debuglist = []


debugger = Debugger()
