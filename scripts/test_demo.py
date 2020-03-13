import pytest


def test_funk():
    print("-----")
    assert True


if __name__ == '__main__':
    # pytest.main(["-s", "test_demo.py"])
    pytest.main(['-s', '--alluredir', './reports-xml', "test_demo.py"])
