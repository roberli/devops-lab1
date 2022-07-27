# Lab requirements
For all taks that will be executed in this first lab, I'm running everything necessary in my persornal notebook, but it doesn't mater where it'll be executed. We could run all servers necessary in the AWS, one private provider like VMware or like me using a Linux with Virtualbox.

## Operation System
I'm using one Linux running ParrotOS version 4.11, but I think that could run any other operation system as Windows, MacOS or other Linux too.

## Hardware Resources
    - 4 VCPUs
    - 16 GB RAM
    - 100 GB of disk

Consideration about the resources. With 4 VCPUs I didn't have any problem, with maximum used of 50 percent, and relation of RAM we're gonna use more because of the virtual machines necessary to run the lab. I could say that's possibly run with less, but for my case it's not necessary. 

And for last, but not least disk here is the trick for me. I'm using one SSD M2 of 256 GB. Because with quick answer of the disk, I don't have to generate load of queue to processor and with this the lab run more smothilly.

## Necessary Softwares
I'm not gonna cover how to install the softwares that'll be installed bellow. But all of them are necessary to properly run the lab in some point:

    - git;
    - curl;
    - VirtualBox;
    - Vagrant;
    - Docker;
    - Docker Compose.

## Files
The files necessary to start this environment are:

    - playbook-rancherserver.yml
    - Vagrantfile
    - docker-compose.yml
    - AddingNodetoK8S.py

## Commands
Here we'll execute the commands to leave the environment Up and able to receive the properly interactions. Let's see:

### The step to execute to start the environment to study DevOps
    
    - Added one entry in the file /etc/hosts, with the IP Address choosed by you, per example:
    192.168.0.121   gitlab-ce
    
    - Access the directory of Vagrantfile
    cd /somepath/docker-compose/gitlab

    - Start the VM of Rancher Server 
    sudo vagrant up node80

    - Start the Node of Rancher Cluster
    sudo vagrant up node81

    - Start the registry server to execute pull and push of pipelines
    sudo vagrant up node82

    - Start the docker service to execute the docker-compose file
    sudo systemctl start docker.service

    - Access the directory of docker-compose
    cd /somepath/docker-compose/gitlab

    - Start the docker-compose environment necessary to run the pipelines
    docker-compose up -d

    - Access URL of Rancher Server
    URL: https://192.168.56.80/
    User: admin
    Pass: strong_password

    - Access URL GitLab
    URL: http://gitlab-ce:8080
    User: admin_user
    Pass: strong_password

With theses commands and configuration files, we're gonna running 3 virtual machines and 2 containers. The server labeled as node80 will run the rancher-server, the node81 will run the roles of etcd, control plane and worker of the cluster k8s, the node82 will run the private registry.

After run the comand "docker-compose up -d" this will start 2 container the GiLab and the GitLab Runner. Similar output will be prompted after execute the steps of vagrant and docker-compose:

    └──╼ $sudo vagrant status
    Current machine states:

    node80                    running (virtualbox)
    node81                    running (virtualbox)
    node82                    running (virtualbox)

    This environment represents multiple VMs. The VMs are all listed
    above with their current state. For more information about a specific
    VM, run `vagrant status NAME`.

    └──╼ $docker container ls
    CONTAINER ID   IMAGE                         COMMAND                  CREATED        STATUS                 PORTS                                                               NAMES
    26dd17bafedb   gitlab/gitlab-runner:alpine   "/usr/bin/dumb-init …"   19 hours ago   Up 7 hours                                                                                 gitlab-runner
    d7ff816c016b   gitlab/gitlab-ce:latest       "/assets/wrapper"        19 hours ago   Up 7 hours (healthy)   0.0.0.0:1111->22/tcp, 0.0.0.0:8080->80/tcp, 0.0.0.0:8443->443/tcp   gitlab-ce