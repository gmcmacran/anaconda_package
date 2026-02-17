from typing import Any


def identity(x: Any) -> Any:
    """
    Return the input value unchanged.

    This function accepts a value of any type and returns it exactly as
    received. It is useful for testing, debugging, or as a placeholder
    in higher‑order functions where a callable is required but no
    transformation is desired.

    Parameters
    ----------
    x : Any
        Any value of any type.

    Returns
    -------
    Any
        The same value that was passed in.
    """
    return x
