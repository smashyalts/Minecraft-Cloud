import os
public_ip = input("Input the ip of ur previously made server: ")
password = input("Input the password of ur previously made server: ")
script = "ssh " + "ubuntu@" + public_ip + " -p " + password
os.system(script)
startserver = "sudo screen java -Xmx1500MB -jar server.jar"
os.system(startserver)
