import pytest
import sys


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    assert some_data == 42


@pytest.mark.skip(reason="Баг в продукте - <ссылка>")
def test_one():
    assert True


@pytest.mark.skipif(sys.version_info != (3, 8), reason="Тест требует python версии 3.8")
def test_python36_and_greater():
    assert True


@pytest.mark.xfail
def test_flaky():
    assert False


@pytest.mark.xfail(sys.platform != "win32",
                   reason="Ошибка в системной библиотеке")
def test_not_for_windows():
    assert True
