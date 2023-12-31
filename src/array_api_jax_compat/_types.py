"""Copyright (c) 2023 Nathaniel Starkman. All rights reserved.

array-api-jax-compat: Array-API JAX compatibility
"""


__all__: list[str] = []

from typing import Any, Protocol, TypeVar, runtime_checkable

import numpy as np


@runtime_checkable
class DType(Protocol):
    """The dtype of an array."""

    dtype: np.dtype[Any]


@runtime_checkable  # TODO: need actual implementation
class SupportsBufferProtocol(Protocol):
    """Supports the buffer protocol."""


_T_co = TypeVar("_T_co", covariant=True)


@runtime_checkable
class NestedSequence(Protocol[_T_co]):
    """A nested sequence."""

    def __getitem__(self, key: int, /) -> "_T_co | NestedSequence[_T_co]":
        ...

    def __len__(self, /) -> int:
        ...
