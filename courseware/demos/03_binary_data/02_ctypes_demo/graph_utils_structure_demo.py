""" graph utils structure demo """

import ctypes
import sys

CALC_MIDPOINT_FN = ctypes.CFUNCTYPE(
    None,
    ctypes.POINTER(ctypes.c_char),
    ctypes.POINTER(ctypes.c_char),
    ctypes.POINTER(ctypes.c_char),
)


# Defines a new C-compatible data type called POINT using the Structure class
# from the ctypes module. The Structure class is used to define C-compatible
# data structures that can be used to interface with C code from Python.
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]


def main() -> None:
    """main"""

    match sys.platform:
        case "darwin":
            graph_utils_lib = ctypes.CDLL("./graph_utils.dylib")
        case "linux":
            graph_utils_lib = ctypes.CDLL("./graph_utils.so")
        case _:
            graph_utils_lib = ctypes.CDLL("./graph_utils.DLL")

    calc_midpoint: CALC_MIDPOINT_FN = graph_utils_lib.calc_midpoint  # type: ignore

    calc_midpoint.argtypes = [  # type: ignore
        ctypes.POINTER(POINT),
        ctypes.POINTER(POINT),
        ctypes.POINTER(POINT),
    ]

    start = POINT(1, 1)
    end = POINT(5, 5)
    mid = POINT(0, 0)

    calc_midpoint(  # type: ignore
        ctypes.pointer(start), ctypes.pointer(end), ctypes.pointer(mid)
    )

    print(mid.x, type(mid.x))
    print(mid.y, type(mid.y))


if __name__ == "__main__":
    main()
