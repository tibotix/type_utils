import pytest
from src import conversions


def test_b2s():
    assert conversions.b2s(b"hello") == "hello"
    assert conversions.b2s("hello") == "hello"
    with pytest.raises(TypeError):
        conversions.b2h(123)


def test_s2b():
    assert conversions.s2b("hello") == b"hello"
    assert conversions.s2b(b"hello") == b"hello"
    with pytest.raises(TypeError):
        conversions.b2h(123)


def test_b2h():
    assert conversions.b2h(b"\xff\xea") == "ffea"
    assert conversions.b2h(b"\x00") == "00"
    with pytest.raises(TypeError):
        conversions.b2h("\x00")


def test_h2b():
    assert conversions.h2b("ffea") == b"\xff\xea"
    assert conversions.h2b(b"00") == b"\x00"
    with pytest.raises(TypeError):
        conversions.h2b(None)


def test_timestamp2b():
    assert conversions.timestamp2b(1641312213.718596, n=4) == b"a\xd4o\xd5"
    assert conversions.timestamp2b(1641312213, n=4) == b"a\xd4o\xd5"
    with pytest.raises(TypeError):
        conversions.timestamp2b(None)


def test_b2timestamp():
    assert conversions.b2timestamp(b"a\xd4o\xd5") == 1641312213
    assert conversions.b2timestamp(b"a\xd4o\xd5") == 1641312213
    with pytest.raises(TypeError):
        conversions.b2timestamp("a\xd4o\xd5")


def test_b2b64urlsafe():
    assert conversions.b2b64urlsafe(b"hello") == "aGVsbG8="
    assert conversions.b2b64urlsafe(b"test") == "dGVzdA=="
    with pytest.raises(TypeError):
        conversions.b2b64urlsafe("test")


def test_b64urlsafe2b():
    assert conversions.b64urlsafe2b("aGVsbG8=") == b"hello"
    assert conversions.b64urlsafe2b(b"aGVsbG8=") == b"hello"
    with pytest.raises(TypeError):
        conversions.b64urlsafe2b(None)


def test_b2b64():
    assert conversions.b2b64(b"testmessage") == "dGVzdG1lc3NhZ2U="
    assert conversions.b2b64(b"testhello") == "dGVzdGhlbGxv"
    with pytest.raises(TypeError):
        conversions.b2b64("testmessage")


def test_b642b():
    assert conversions.b642b(b"dGVzdG1lc3NhZ2U=") == b"testmessage"
    assert conversions.b642b("dGVzdG1lc3NhZ2U=") == b"testmessage"
    with pytest.raises(TypeError):
        conversions.b642b(None)
