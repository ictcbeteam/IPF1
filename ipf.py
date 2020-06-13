print(".__           __   _________  ___.    ___________")
print("|__|  ____  _/  |_ \_   ___ \ \_ |__  \_   _____/")
print("|  |_/ ___\ \   __\/    \  \/  | __ \  |    __)  ")
print("|  |\  \___  |  |  \     \____ | \_\ \ |       \ ")
print("|__| \___  > |__|   \______  / |___  //_______ | ")
print("         \/                \/      \/         \/ ")
                                                 
                                                 











import socket
host = input("Enter Host Name: example www.google.com ->")
ip = socket.gethostbyname(host)
print ("IP of "+ host + ":\t" + ip )
