"""Chrome DevTools Protocol command-line utilities."""

from .core import (
    CdpClient,
    HttpClient,
    TargetInfo,
    main,
    main_async,
    wait_network_idle,
    wait_ready_state,
)

__all__ = [
    "CdpClient",
    "HttpClient",
    "TargetInfo",
    "main",
    "main_async",
    "wait_network_idle",
    "wait_ready_state",
]
