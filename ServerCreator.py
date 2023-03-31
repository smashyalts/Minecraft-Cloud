from hcloud import Client
import os
import time
from cryptography.hazmat.primitives.asymmetric import rsa
from hcloud.server_types.domain import ServerType
import paramiko
import io
from hcloud.images.domain import Image
print("Welcome to the one line minecraft server creator on hetzner cloud! (make sure u have enough credits on your account)")
eula = input("Do u Accept Minecraft's EULA? (yes/no): ")
if not eula=="yes":
    print("To continute you need to accept EULA")
    quit()
else:
    token2 = input("Input ur API Token here: ")
    client = Client(token=token2)
    key = paramiko.RSAKey.generate(2048)
    a3 = key.get_base64()
    a4 = "ssh-rsa  " + a3
    sshpublic = client.ssh_keys.create("minecraft", a4)
    list=[sshpublic]
    response = client.servers.create(name="minecraft", server_type=ServerType(name="cpx11"), image=Image(name="ubuntu-20.04"), ssh_keys=list)
    server = response.server
    print("minecraft server is being prepared")
    time.sleep(25)
    public_ip = server.public_net.ipv4.ip
    print("Ip to use after server has finished being set up: " + public_ip + ":25565")
    adminuser = input("Input the username of the user you want to have administrator permissions on the server: ")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    ssh.connect(public_ip, username='root', pkey=key)
    command = "sudo apt-get update ; sudo apt-get -y install openjdk-17-jre-headless screen ; mkdir server ; cd server ; curl https://api.papermc.io/v2/projects/paper/versions/1.>    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    time.sleep(25)
    print("Server has been setup!")
