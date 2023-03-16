from hcloud import Client
import os
import time
from hcloud.server_types.domain import ServerType
from hcloud.images.domain import Image
print("Welcome to the one line minecraft server creator on hetzner cloud! (make sure u have enough credits on your account)")
eula = input("Do u Accept Minecraft's EULA? (yes/no): ")
if not eula==yes:
    os._exit("You need to accept EULA to continue")
else:
    token2 = input("Input ur API Token here: ")
    client = Client(token=token2)
    response = client.servers.create(name="minecraft", server_type=ServerType(name="cpx11"), image=Image(name="ubuntu-20.04"))
    server = response.server
    print(server + " is being prepared")
    print("Root Password: " + response.root_password)
    server.power_on()
    time.sleep(25)
    public_ip = server.public_net.ipv4.ip
    print("Ip to use after server has finished being set up: " + public_ip + ":25565")
    adminuser = input("Input the username of the user you want to have administrator permissions on the server: ")
    script = "ssh " + "ubuntu@" + public_ip + " -p " + response.root_password
    os.system(script)
    installer = "sudo apt-get -y install openjdk-17-jdk openjdk-17-jre screen"
    os.system(installer)
    ServerDownloader = "mkdir server ; cd server ; curl https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/448/downloads/paper-1.19.3-448.jar > server.jar"
    os.system(ServerDownloader)
    time.sleep(10)
    eulaaccepter = "cd server ; echo eula = true > eula.txt"
    os.system(eulaaccepter)
    startserver = "sudo screen -S Minecraft java -Xmx1G -jar server.jar"
    os.system(startserver)
    time.sleep(10)
    admin = "op " + adminuser
    os.system(admin)
