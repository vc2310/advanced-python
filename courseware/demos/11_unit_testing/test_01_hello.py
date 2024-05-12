"""demo of standalone tests"""

import pytest

from hello import hello, EmptyStringError


def test_hello_with_subject() -> None:
    """test hello with a subject"""

    # arrange

    subject = "world"
    expected = "hello, world"

    # act

    actual = hello(subject)

    # assert

    assert actual == expected


def test_hello_with_empty_subject() -> None:
    """test hello with an empty subject"""
    with pytest.raises(EmptyStringError):
        hello("")
