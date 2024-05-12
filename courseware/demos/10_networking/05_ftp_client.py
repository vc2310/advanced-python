from ftplib import FTP
from pathlib import Path

download_path = Path("download")
download_path.mkdir(exist_ok=True)

upload_path = Path("upload")

# install `pyftpdlib` package
# - `python -m pip install pyftpdlib`
# - `conda install -y pyftpdlib`
# - `micromamba install -y pyftpdlib`

# pyftpdlib is a Python module that provides a high-level implementation of
# an FTP server. It is built on top of Python's built-in ftplib module and
# provides a simple and efficient way to create custom FTP servers in Python.

# `python -m pyftpdlib -w -u user -P pass -d files`

# Creates a new instance of the FTP class from Python's built-in ftplib
# module. This class provides a set of methods and attributes that can be
# used to interact with an FTP server.
ftp = FTP()

# Connects to an FTP server using an instance of the FTP class from Python's
# built-in ftplib module. The connect method takes two arguments: the first
# argument is a string that specifies the hostname or IP address of the server
# to connect to, and the second argument is an optional integer that specifies
# the port number to use for the connection (the default is 21)
ftp.connect("localhost", 2121)

# Authenticate with an FTP server using an instance of the FTP class from
# Python's built-in ftplib module. The login method takes two arguments: the
# first argument is a string that specifies the username to use for
# authentication, and the second argument is a string that specifies the
# password to use for authentication.
ftp.login("user", "pass")

# Retrieves a list of files and directories from an FTP server using an
# instance of the FTP class from Python's built-in ftplib module. The
# retrlines method takes one argument: a string that specifies the command to
# be sent to the server.
print(ftp.retrlines("LIST"))

download_file_name = "download_item.txt"

with open(download_path.joinpath(download_file_name), "wb") as fp:
    # The ftp.retrbinary method is a function call that is used in Python's
    # built-in ftplib module. This method is used to retrieve a file from an
    # FTP server in binary mode. The method takes two arguments: the first
    # argument is a string that specifies the command to be sent to the server,
    # and the second argument is a callback function that is called for each
    # block of data received from the server.
    ftp.retrbinary(f"RETR {download_file_name}", fp.write)

upload_file_name = "upload_item.txt"

with open(upload_path.joinpath(upload_file_name), "rb") as fp:
    # The ftp.storbinary method is a function call that is used in Python's
    # built-in ftplib module. This method is used to upload a file to an FTP
    # server in binary mode. The method takes two arguments: the first
    # argument is a string that specifies the command to be sent to the
    # server, and the second argument is a file-like object that provides
    # the data to be uploaded.
    ftp.storbinary(f"STOR {upload_file_name}", fp)

ftp.quit()
