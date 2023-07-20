class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)
    
    def testMethod(self):
        self.wasRun = 1

class TestCaseTest:
    def testRunning(self):
        test = WasRun("testmethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun
        
# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)