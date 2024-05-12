from paramiko import SSHClient, AutoAddPolicy

# Paramiko SSH Client/Server for Python: https://www.paramiko.org/

# create the SSH Client and load the keys
with SSHClient() as client:
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy)

    # connect to the SSH server with a username/password
    client.connect(
        "74.249.98.120", username="student", password="tesTp@ss!123"
    )

    # sftp is really just ssh, so using sftp upload a file to the server
    with client.open_sftp() as sftp_client:
        sftp_client.chdir("/home/student")
        print(sftp_client.getcwd())
        sftp_client.put("test.sh", "/home/student/test.sh")

    # get a directory listing to see if the file was uploaded
    stdin, stdout, stderr = client.exec_command("ls -al")
    for line in stdout:
        print(line.rstrip())

    # update the script to be executable
    client.exec_command("chmod u+x ./test.sh")
    for line in stdout:
        print(line.rstrip())

    # execute the uploaded script
    stdin, stdout, stderr = client.exec_command("./test.sh")
    for line in stdout:
        print(line.rstrip())
