from __future__ import annotations
from typing import TypeVar, Generic, Any, Callable
from dataclasses import FrozenInstanceError


T = TypeVar('T')
R = TypeVar('R')


class Chain(Generic[T]):

    def __init__(self, value: T):
        self.value = value
  
    def __setattr__(self, __name: str, __value: Any) -> None:
        raise FrozenInstanceError()

    def apply(self, func: Callable[[T], R]) -> Chain[R]:
        return Chain(func(self.value))
