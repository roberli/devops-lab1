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