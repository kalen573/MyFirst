class OriginalError(Exception):
    def __str__(self):
        return "例外が発生しています"

class TestCase:
    def __init__(self, name: str):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result

class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "    
    def testMethod(self):
        self.log = self.log + "testMethod "
    def testBrokenMethod(self):
        raise OriginalError()
    def tearDown(self):
        self.log = self.log + "tearDown"

class TestResult:
    def __init__(self):
        self.runCount = 0
    def testStarted(self):
        self.runCount += 1
    def summary(self):
        return "{0} run, 0 failed".format(self.runCount)

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown"
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert result.summary() == "1 run, 0 failed"
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert result.summary() == "1 run, 1 failed"
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert result.summary() == "1 run, 1 failed"

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
# TestCaseTest("testFailedResult").run()
TestCaseTest("testFailedResultFormatting").run()