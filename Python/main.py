import socket
import psutil

hostname = socket.gethostname()

if len(hostname) < 10:
    print("You have a stupid hostname.")


psutil.virtual_memory()

