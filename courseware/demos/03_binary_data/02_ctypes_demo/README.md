# Python Ctypes and Struct Data

The following instructions explain how to compile and run code that will enable
the share of `struct` data between Python and C. Two techniques are used: 
Python's `struct` module and Python's `Structure` class. Both solve the same
problem through different approaches.

## Windows

Open a web browser, and navigate to
[https://winlibs.com/](https://winlibs.com/). Download the latest version
of the UCRT runtime for Windows 64. Extract the archive and ensure the path
to the `bin` is added to your `PATH` environment variable. Once added, open a
new terminal window and verify `gcc` is available by running the following command:

```bash
gcc --version
```

Once `gcc` is available, build the shared library, by running the following
command:

```bash
gcc -std=c17 -Wall -Wextra -pedantic -shared -fPIC graph_utils.c -o graph_utils.dll
```

To use Python's `struct` module to create byte strings to pass C `struct` data
run `graph_utils_struct_demo.py`.

```bash
python ./graph_utils_struct_demo.py
```

To use Python's `ctypes` module `Structure` class to create objects to pass C
`struct` data run `graph_utils_structure_demo.py`.

```bash
python ./graph_utils_structure_demo.py
```

## macOS

The command `gcc` should be available on macOS without having to install any
additional dependencies. If it is not available, then try installing the
command-line tools for Xcode by running the following command:

```bash
xcode-select --install
```

To verify `gcc` is available, run the following command:

```bash
gcc --version
```

Once `gcc` is available, build the shared library, by running the following
command:

```bash
gcc -std=c17 -Wall -Wextra -pedantic -shared -fPIC graph_utils.c -o graph_utils.dylib
```

To use Python's `struct` module to create byte strings to pass C `struct` data 
run `graph_utils_struct_demo.py`.

```bash
python ./graph_utils_struct_demo.py
```

To use Python's `ctypes` module `Structure` class to create objects to pass C
`struct` data run `graph_utils_structure_demo.py`.

```bash
python ./graph_utils_structure_demo.py
```

## Linux

To verify `gcc` is available, run the following command:

```bash
gcc --version
```

Once `gcc` is available, build the shared library, by running the following
command:

```bash
gcc -std=c17 -Wall -Wextra -pedantic -shared -fPIC graph_utils.c -o graph_utils.so
```

To use Python's `struct` module to create byte strings to pass C `struct` data 
run `graph_utils_struct_demo.py`.

```bash
python ./graph_utils_struct_demo.py
```

To use Python's `ctypes` module `Structure` class to create objects to pass C
`struct` data run `graph_utils_structure_demo.py`.

```bash
python ./graph_utils_structure_demo.py
```
