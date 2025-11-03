"""Helper module exercising a broad set of statements for instrumentation tests."""

from __future__ import annotations

import asyncio
from contextlib import nullcontext


def try_finally_example() -> list[str]:
    log: list[str] = []
    try:
        log.append("try start")
        raise RuntimeError("boom")
        log.append("try end")
    finally:
        log.append("finally block")
    log.append("after try")
    return log


def while_else_example() -> list[str]:
    log: list[str] = []
    count = 0
    while count < 3:
        log.append(f"while {count} start")
        if count == 1:
            raise ValueError("loop error")
        log.append(f"while {count} end")
        count += 1
    else:
        log.append("while else")
    log.append("after while")
    return log


def with_example() -> list[str]:
    log: list[str] = []
    with nullcontext():
        log.append("with start")
        raise RuntimeError("with boom")
        log.append("with end")
    log.append("after with")
    return log


async def async_with_example() -> list[str]:
    log: list[str] = []
    lock = asyncio.Lock()
    async with lock:
        log.append("async with start")
        raise RuntimeError("async with boom")
        log.append("async with end")
    log.append("async with after")
    return log


async def async_for_example() -> list[str]:
    log: list[str] = []

    async def _agen():
        for i in range(3):
            yield i

    async for i in _agen():
        log.append(f"async for {i} start")
        if i == 1:
            raise RuntimeError("async for boom")
        log.append(f"async for {i} end")
    log.append("async for done")
    return log


def match_example(kind: str) -> list[str]:
    log: list[str] = []
    match {"kind": kind}:
        case {"kind": "alpha"}:
            log.append("match alpha start")
            raise RuntimeError("match boom")
            log.append("match alpha end")
        case _:
            log.append("match default")
    log.append("after match")
    return log


def trystar_example() -> list[str]:
    log: list[str] = []
    try:
        log.append("trystar start")
        raise ValueError("boom")
        log.append("trystar end")
    except* ValueError as exc:
        log.append(f"trystar handler {len(exc.exceptions)}")
    finally:
        log.append("trystar finally")
    log.append("trystar after")
    return log
