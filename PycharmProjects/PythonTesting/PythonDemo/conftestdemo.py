import pytest


@pytest.fixture(scope='class')
def setup():
    print("I will execute first")
    yield
    print("I will be executed last")
@pytest.fixture()
def dataLoad():
    print("user profile data is being created ")
    return ["rahul","shetty","rahulshettyacademy.com"]
@pytest.fixture(params=[('chrome','rahul','shetty'),('firefox','shetty'),('IE','academy')])
def crossBrowser(request):
    return request.param