import os
os.system("clear")
while True:
	os.system("tput setaf 1")
	print("\t\t\t Welcome to Docker World")
	os.system("tput setaf 7")
	print("\t\t\t .......................")
	print("""
	Press 1: Installation of docker
	Press 2: Start the docker
	Press 3: setup Docker-compose
	Press 4: WORDPRESS server portno 8081
	Press 5: Exit 
	""")
	print("Enter your choice: ",end="")
	ch=int(input())
	if ch==1:
		os.system("python3 install_docker.py")
	if ch==2:
		os.system("systemctl start docker")
		print("Docker is Started..")
	elif ch==3:
		os.system("sudo curl -L 'https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)' -o /usr/local/bin/docker-compose")
		os.system("sudo chmod +x /usr/local/bin/docker-compose")
	elif ch==4:
		os.system("docker images | grep mysql")
		if os.system("echo $?")==1:
			os.system("docker pull mysql:5.7")
			os.system("yum install mysql")
		os.system("docker images | grep wordpress")
		if os.system("echo $?")==1:
			os.system("docker pull wordpress:5.1.1-php7.3-apache")
		os.chdir("mycompose")		
		os.system("docker-compose up -d")
		os.chdir("..")	
	elif ch==5:
		break
	else:
		print("Choose correct option....")
	input("Enter to continue...")
	os.system("clear")
		
