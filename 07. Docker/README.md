# Homework Assignment 1: Docker Installation and Basic Commands
## 1. Install Docker on your local machine or a virtual environment.
```bash
adminn@ubuntudocker:~$ mkdir Docker
adminn@ubuntudocker:~$ cd Docker/
adminn@ubuntudocker:~/Docker$ ls
adminn@ubuntudocker:~/Docker$ sudo apt-get update
adminn@ubuntudocker:~/Docker$ sudo apt-get install ca-certificates curl
adminn@ubuntudocker:~/Docker$ sudo install -m 0755 -d /etc/apt/keyrings
adminn@ubuntudocker:~/Docker$ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
adminn@ubuntudocker:~/Docker$ sudo chmod a+r /etc/apt/keyrings/docker.asc
adminn@ubuntudocker:~/Docker$ echo \
>   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
>   $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
>   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
adminn@ubuntudocker:~/Docker$ sudo apt-get update
adminn@ubuntudocker:~/Docker$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
adminn@ubuntudocker:~/Docker$ sudo usermod -aG docker $USER
```
## 2. Verify the Docker installation by running the docker --version command.
```bash
adminn@ubuntudocker:~$ docker --version
Docker version 27.3.1, build ce12230
adminn@ubuntudocker:~$
```
## 3. Pull the official "hello-world" Docker image and run a container based on it.
```bash
adminn@ubuntudocker:~$ docker pull hello-world:latest
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete
Digest: sha256:d211f485f2dd1dee407a80973c8f129f00d54604d2c90732e8e320e5038a0348
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
adminn@ubuntudocker:~$ docker run hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
## 4. List the running containers using the docker ps command.
```bash
adminn@ubuntudocker:~$ docker ps -a
CONTAINER ID   IMAGE                COMMAND    CREATED         STATUS                     PORTS     NAMES
7635b70456e8   hello-world:latest   "/hello"   9 seconds ago   Exited (0) 8 seconds ago             heuristic_beaver
adminn@ubuntudocker:~$
```
## 5. Document the installation process and the commands used for verification.
```bash
Done
```


# Homework Assignment 2: Building a Docker Image with Dockerfile
## 1. Create a new directory for your Dockerfile and application code.
```bash
adminn@ubuntudocker:~/Docker$ ls
Dockerfile  Website.py
adminn@ubuntudocker:~/Docker$
```
## 2. Write a Dockerfile to build an image for a simple web application (e.g., Flask or Node.js).

## 3. Copy your application code into the image and set the necessary environment.
## 4. Build the Docker image using the docker build command.
## 5. Run a container based on the image and access the web application.
## 6. Document the steps taken to create the Dockerfile, build the image, and access the app.