#pip install pytest
#test name should start with test_ and method name should start with test_
#Method name should have sense
#-k stands for method names execution ,-s logs in out put -v stand for verbos
#you can mark (tag) tests @pytest.mark.smoke and then run with py.test -m smoke -s -v
#you can skip the test with @pytest.mark.skip
#if you have run the test without any out put then you can run with below command
#@pytest.mark.xfail
#fixtures
#to run set up and tear down methods i will place setup and teardown methods in conftestdemo.py file
#fixture make it available to all the test cases
#data driven and parameterisation can be done with return statements in list format
#when you define fixture scope to class only ,it will run once before class initiated and at the end.
#py.test --html=report.html
#to run report as html
#py.test - -html = report.html - s - v
import pytest

@pytest.mark.skip
@pytest.mark.smoke
def test_firstprogram():
    print("Hello")

@pytest.mark.xfail
def test_secondCreditcardprogram():
    print("Good morning ")

def test_crossbrowser(crossBrowser):
    print(crossBrowser)