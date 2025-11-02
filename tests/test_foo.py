import asyncio

import pytest

from . import foo


def test_example_raises_and_prints(capsys):
    with pytest.raises(ZeroDivisionError):
        foo.example("Alice")
    captured = capsys.readouterr()
    assert "hi Alice" in captured.out
    assert "bye" not in captured.out


def test_loops_stops_on_error(capsys):
    with pytest.raises(ZeroDivisionError):
        foo.loops()
    captured = capsys.readouterr()
    assert "loop 0 start" in captured.out
    assert "loop 0 end" in captured.out
    assert "loop 1 start" in captured.out
    assert "loop 1 end" not in captured.out
    assert "after loop" not in captured.out


def test_tricky_raises_after_print(capsys):
    with pytest.raises(ZeroDivisionError):
        foo.tricky()
    captured = capsys.readouterr()
    assert "before return" in captured.out
    assert "after return" not in captured.out


def test_async_exception(capsys):
    async def run_async():
        await foo.aex()

    with pytest.raises(ZeroDivisionError):
        asyncio.run(run_async())
    captured = capsys.readouterr()
    assert "astart" in captured.out
    assert "aend" not in captured.out


def test_class_method_raises(capsys):
    instance = foo.C()
    with pytest.raises(ZeroDivisionError):
        instance.m()
    captured = capsys.readouterr()
    assert "C.m before" in captured.out
    assert "C.m after" not in captured.out
