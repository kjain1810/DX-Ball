class Debugger():
    """A class to debug during development"""

    def __init__(self):
        self.debuglist = []

    def debug(self, obj):
        """Add object to debug list"""
        self.debuglist.append(obj)

    def printDebugs(self):
        """Print all debug statements"""
        for obj in self.debuglist:
            print(obj)
        self.clearDebugs()

    def clearDebugs(self):
        """Clear debugs"""
        self.debuglist = []


debugger = Debugger()
