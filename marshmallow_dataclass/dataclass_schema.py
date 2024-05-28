from marshmallow import Schema
from typing import (
    TYPE_CHECKING,
    Collection,
    Generic,
    Literal,
    TypeVar,
    Union,
    cast,
    overload,
)
import sys

if sys.version_info < (3, 10):
    from typing_extensions import ParamSpec
else:
    from typing import ParamSpec

_T = TypeVar("_T")
_P = ParamSpec("_P")


class DataclassSchema(Schema, Generic[_T]):
    if TYPE_CHECKING:

        @overload
        def load(self, *args, many: Literal[True] = True, **kwargs) -> Collection[_T]:
            ...

        @overload
        def load(self, *args, many: Literal[False] = False, **kwargs) -> _T:
            ...

        def load(
            self, *args, many: bool | None = False, **kwargs
        ) -> Union[_T, Collection[_T]]:
            return cast(_T, super().loads(*args, **kwargs))

        @overload
        def loads(self, *args, many: Literal[True] = True, **kwargs) -> Collection[_T]:
            ...

        @overload
        def loads(self, *args, many: Literal[False] = False, **kwargs) -> _T:
            ...

        def loads(
            self, *args, many: bool | None = False, **kwargs
        ) -> Union[_T, Collection[_T]]:
            ...
