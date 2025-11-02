import asyncio

import importlib

import besteffort.core  # noqa: F401 ensures finder is installed

foo = importlib.import_module("besteffort.tests.foo")


def test_example_raises_and_prints(capsys):
    foo.example("Alice")
    captured = capsys.readouterr()
    assert "hi Alice" in captured.out
    assert "bye" in captured.out


def test_loops_stops_on_error(capsys):
    foo.loops()
    captured = capsys.readouterr()
    assert "loop 0 start" in captured.out
    assert "loop 0 end" in captured.out
    assert "loop 1 start" in captured.out
    assert "loop 1 end" in captured.out
    assert "loop 2 start" in captured.out
    assert "loop 2 end" in captured.out
    assert "after loop" in captured.out


def test_tricky_raises_after_print(capsys):
    foo.tricky()
    captured = capsys.readouterr()
    assert "before return" in captured.out
    assert "after return" in captured.out


def test_async_exception(capsys):
    async def run_async():
        await foo.aex()

    asyncio.run(run_async())
    captured = capsys.readouterr()
    assert "astart" in captured.out
    assert "aend" in captured.out


def test_class_method_raises(capsys):
    instance = foo.C()
    instance.m()
    captured = capsys.readouterr()
    assert "C.m before" in captured.out
    assert "C.m after" in captured.out
