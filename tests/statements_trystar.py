"""Exception group examples for Python 3.11+."""

from __future__ import annotations

from typing import List


def trystar_example() -> List[str]:
    log: List[str] = []
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
