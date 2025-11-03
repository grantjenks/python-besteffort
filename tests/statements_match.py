"""Pattern matching examples for Python 3.10+."""

from __future__ import annotations

from typing import List


def match_example(kind: str) -> List[str]:
    log: List[str] = []
    match {"kind": kind}:
        case {"kind": "alpha"}:
            log.append("match alpha start")
            raise RuntimeError("match boom")
            log.append("match alpha end")
        case _:
            log.append("match default")
    log.append("after match")
    return log
