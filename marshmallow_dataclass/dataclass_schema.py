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
            data: Union[Mapping[str, Any], Iterable[Mapping[str, Any]]],
            *,
            many: Literal[False],
            partial: Union[bool, types.StrSequenceOrSet, None] = None,
            unknown: Union[str, None] = None,
        ) -> _T:
            ...

        @overload
        def load(
            self,
            data: Union[Mapping[str, Any], Iterable[Mapping[str, Any]]],
            *,
            many: Literal[True],
            partial: Union[bool, types.StrSequenceOrSet, None] = None,
            unknown: Union[str, None] = None,
        ) -> List[_T]:
            ...

        @overload
        def load(
            self,
            data: Union[Mapping[str, Any], Iterable[Mapping[str, Any]]],
            *,
            many: Union[bool, None] = None,
            partial: Union[bool, types.StrSequenceOrSet, None] = None,
            unknown: Union[str, None] = None,
        ) -> Union[_T, List[_T]]:
            ...

        def load(
            self,
            data: Union[Mapping[str, Any], Iterable[Mapping[str, Any]]],
            *,
            many: Union[bool, None] = None,
            partial: Union[bool, types.StrSequenceOrSet, None] = None,
            unknown: Union[str, None] = None,
        ) -> Union[_T, List[_T]]:
            # Implementation goes here
            ...

        @overload
        def loads(
            self,
            json_data: str,
            *,
            many: Literal[False],
            partial: Union[bool, types.StrSequenceOrSet, None] = None,
            unknown: Union[str, None] = None,
            **kwargs,
        ) -> _T:
            ...

        @overload
        def loads(
            self,
            json_data: str,
            *,
            many: Literal[True] = True,
            partial: Union[bool, types.StrSequenceOrSet, None] = None,
            unknown: Union[str, None] = None,
            **kwargs,
        ) -> List[_T]:
            ...

        @overload
        def loads(
            self,
            json_data: str,
            *,
            many: Union[bool, None] = None,
            partial: Union[bool, types.StrSequenceOrSet, None] = None,
            unknown: Union[str, None] = None,
            **kwargs,
        ) -> Union[_T, List[_T]]:
            ...

        def loads(
            self,
            json_data: str,
            *,
            many: Union[bool, None] = None,
            partial: Union[bool, types.StrSequenceOrSet, None] = None,
            unknown: Union[str, None] = None,
            **kwargs,
        ) -> Union[_T, List[_T]]:
            ...
