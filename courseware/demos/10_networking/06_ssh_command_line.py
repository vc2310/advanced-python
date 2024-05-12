from paramiko import SSHClient, AutoAddPolicy

# Paramiko SSH Client/Server for Python: https://www.paramiko.org/

# the `paramiko` will need to be installed
# - `python -m pip install paramiko`
# - `conda install -y paramiko`
# - `micromamba install -y paramiko`

# create the SSH Client and load the keys
with SSHClient() as client:
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy)

    # connect to the SSH server with a username/password
    client.connect(
        "74.249.98.120", username="student", password="tesTp@ss!123"
    )

    # run a command on the SSH server
    stdin, stdout, stderr = client.exec_command("ls -al")

    print("remote client folder contents")

    # output the result of the command to the console
    for line in stdout:
        # rstrip is going to remove all extra whitespace characters at the end
        print(line.rstrip())
