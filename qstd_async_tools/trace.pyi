import typing


def trace_id() -> typing.ContextManager[str]: ...


def get_trace_ids() -> typing.Union[typing.List[str], None]: ...


def add_trace_id(
    trace_id_str: typing.Optional[typing.Union[str], typing.List[str]] = None
) -> typing.Optional[str]: ...

