from marshmallow import Schema, types
from typing import (
    TYPE_CHECKING,
    Collection,
    Generic,
    Literal,
    TypeVar,
    Union,
    overload,
)
import typing
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
        def load(
            self,
            data: (
                typing.Mapping[str, typing.Any]
                | typing.Iterable[typing.Mapping[str, typing.Any]]
            ),
            *,
            many: Literal[True] = True,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
        ) -> Collection[_T]:
            ...

        @overload
        def load(
            self,
            data: (
                typing.Mapping[str, typing.Any]
                | typing.Iterable[typing.Mapping[str, typing.Any]]
            ),
            *,
            many: Literal[False] = False,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
        ) -> _T:
            ...

        @overload
        def load(
            self,
            data: (
                typing.Mapping[str, typing.Any]
                | typing.Iterable[typing.Mapping[str, typing.Any]]
            ),
            *,
            many: bool | None = None,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
        ) -> Union[_T, Collection[_T]]:
            ...

        def load(
            self,
            data: (
                typing.Mapping[str, typing.Any]
                | typing.Iterable[typing.Mapping[str, typing.Any]]
            ),
            *,
            many: bool | None = None,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
        ) -> Union[_T, Collection[_T]]:
            ...

        @overload
        def loads(
            self,
            json_data: str,
            *,
            many: Literal[False] = False,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
            **kwargs,
        ) -> _T:
            ...

        @overload
        def loads(
            self,
            json_data: str,
            *,
            many: Literal[True] = True,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
            **kwargs,
        ) -> Collection[_T]:
            ...

        @overload
        def loads(
            self,
            json_data: str,
            *,
            many: bool | None = None,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
            **kwargs,
        ) -> Union[_T, Collection[_T]]:
            ...

        def loads(
            self,
            json_data: str,
            *,
            many: bool | None = None,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
            **kwargs,
        ) -> Union[_T, Collection[_T]]:
            ...
