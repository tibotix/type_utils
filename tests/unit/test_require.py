import pytest
import datetime
from src import require

def test_require_bytes():
    assert require.require_bytes(b"aaa") == b"aaa"
    assert require.require_bytes("aaa") == b"aaa"
    assert require.require_bytes(10, int_to_string=True) == b"10"

    with pytest.raises(TypeError):
        assert require.require_bytes(10)


def test_require_timestamp_bytes():
    assert require.require_timestamp_bytes(b"aaa") == b"aaa"
    assert require.require_timestamp_bytes(10) == b"\x00\x00\x00\x00\x00\x00\x00\x0A"
    assert require.require_timestamp_bytes(10, n=4) == b"\x00\x00\x00\x0A"
    assert (
        require.require_timestamp_bytes(datetime.datetime.fromtimestamp(100000))
        == b"\x00\x00\x00\x00\x00\x01\x86\xa0"
    )

    with pytest.raises(TypeError):
        assert require.require_timestamp_bytes("aaa")


def test_require_string():
    assert require.require_string("aaa") == "aaa"
    assert require.require_string(b"aaa") == "aaa"
    assert require.require_string(10, int_to_string=True) == "10"

    with pytest.raises(TypeError):
        assert require.require_string(10)


def test_require_int():
    assert require.require_int(123) == 123
    assert require.require_int("123", str_to_int=True) == 123
    assert require.require_int(b"AB") == 16961

    with pytest.raises(TypeError):
        require.require_int("123", str_to_int=False)

    with pytest.raises(TypeError):
        require.require_int("hello")
