""" graph utils structure demo """

import ctypes
import sys
import struct

CALC_MIDPOINT_FN = ctypes.CFUNCTYPE(
    None,
    ctypes.POINTER(ctypes.c_char),
    ctypes.POINTER(ctypes.c_char),
    ctypes.POINTER(ctypes.c_char),
)


def main() -> None:
    """main"""

    match sys.platform:
        case "darwin":
            graph_utils_lib = ctypes.CDLL("./graph_utils.dylib")
        case "linux":
            graph_utils_lib = ctypes.CDLL("./graph_utils.so")
        case _:
            graph_utils_lib = ctypes.CDLL(".\\graph_utils.dll")

    calc_midpoint: CALC_MIDPOINT_FN = graph_utils_lib.calc_midpoint  # type: ignore

    # Uses the pack function from the struct module to create a binary
    # representation of a tuple of two integers. The struct module is
    # used to convert between Python values and C structs represented
    # as Python bytes objects.
    start = struct.pack("=2i", 1, 2)
    end = struct.pack("=2i", 5, 6)
    mid = struct.pack("=2i", 0, 0)

    # Defines the argument types for a C function called calc_midpoint using
    # the argtypes attribute of the function. The argtypes attribute is a list
    # that specifies the expected argument types for the function.
    calc_midpoint.argtypes = [  # type: ignore
        ctypes.POINTER(ctypes.c_char),
        ctypes.POINTER(ctypes.c_char),
        ctypes.POINTER(ctypes.c_char),
    ]

    calc_midpoint(start, end, mid)  # type: ignore

    # Uses the unpack function from the struct module to convert a binary
    # representation of a tuple of two integers into two separate integer
    # variables. The struct module is used to convert between Python values
    # and C structs represented as Python bytes objects.
    mid_x, mid_y = struct.unpack("=2i", mid)

    print(mid_x, type(mid_x))
    print(mid_y, type(mid_y))


if __name__ == "__main__":
    main()
