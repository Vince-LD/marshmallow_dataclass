from marshmallow import Schema, types

from typing import (
    TYPE_CHECKING,
    Any,
    Iterable,
    Generic,
    List,
    Literal,
    Mapping,
    TypeVar,
    Union,
    overload,
)

_T = TypeVar("_T")
_I = TypeVar("_I", bound=Iterable)


class DataclassSchema(Schema, Generic[_T]):
    if TYPE_CHECKING:

        @overload
        def load(
            self,
            data: (Mapping[str, Any] | Iterable[Mapping[str, Any]]),
            *,
            many: Literal[True] = True,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
        ) -> List[_T]:
            ...

        @overload
        def load(
            self,
            data: (Mapping[str, Any] | Iterable[Mapping[str, Any]]),
            *,
            many: Literal[False] = False,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
        ) -> _T:
            ...

        @overload
        def load(
            self,
            data: (Mapping[str, Any] | Iterable[Mapping[str, Any]]),
            *,
            many: bool | None = None,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
        ) -> Union[_T, List[_T]]:
            ...

        def load(
            self,
            data: (Mapping[str, Any] | Iterable[Mapping[str, Any]]),
            *,
            many: bool | None = None,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
        ) -> Union[_T, List[_T]]:
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
        ) -> List[_T]:
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
        ) -> Union[_T, List[_T]]:
            ...

        def loads(
            self,
            json_data: str,
            *,
            many: bool | None = None,
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
            **kwargs,
        ) -> Union[_T, List[_T]]:
            ...
