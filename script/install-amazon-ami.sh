#!/bin/bash -ex

sudo yum -y update
sudo yum -y install tmux git
curl https://repo.continuum.io/archive/Anaconda2-4.2.0-Linux-x86_64.sh > Anaconda2-4.2.0-Linux-x86_64.sh
bash Anaconda2-4.2.0-Linux-x86_64.sh -b -f
echo export PATH=$PATH:~/anaconda2/bin >> ~/.bashrc
. ~/.bashrc
conda create -y -n opencvapi opencv
source activate opencvapi
