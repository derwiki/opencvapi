# OpenCV API
A web API into OpenCV computer vision APIs.

## Setup
```
sudo yum -y update
curl https://repo.continuum.io/archive/Anaconda2-4.2.0-Linux-x86_64.sh > Anaconda2-4.2.0-Linux-x86_64.sh
bash Anaconda2-4.2.0-Linux-x86_64.sh -b -f
sudo yum -y install tmux git
echo export PATH=$PATH:~/anaconda2/bin
conda create -y -n opencvapi opencv
source activate opencvapi
```

## Running
```
~/opencvapi$
$ source activate opencvapi
(opencvapi) ~/opencvapi$
$ python app/server.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

## Testing
In your browser, load:
[http://localhost:5000/face/squares](http://localhost:5000/face/squares)
