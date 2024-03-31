import typing

P = typing.ParamSpec("P")


def run_in_background(coroutine: typing.Coroutine): ...


def run_in_background_decorator(
    func: typing.Callable[P, typing.Coroutine[typing.Any]]
) -> typing.Callable[P, None]: ...
