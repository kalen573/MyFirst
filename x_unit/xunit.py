import traceback

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
        try:
            method = getattr(self, self.name)
            method()
        except OriginalError as e:
            print(e)
            result.testFailed()
            traceback.print_exc()
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
        self.errorCount = 0
    def testStarted(self):
        self.runCount += 1
    def testFailed(self):
        self.errorCount += 1
    def summary(self):
        return "{0} run, {1} failed".format(self.runCount, self.errorCount)
    
class TestSuite:
    def __init__(self):
        self.tests = []
    def add(self, test):
        self.tests.append(test)
    def run(self):
        result = TestResult()
        for test in self.tests:
            test.run(result)
        return result

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
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = suite.run()
        assert result.summary() == "2 run, 1 failed"

print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCaseTest("testResult").run().summary())
print(TestCaseTest("testFailedResult").run().summary())
print(TestCaseTest("testFailedResultFormatting").run().summary())
print(TestCaseTest("testSuite").run().summary())
