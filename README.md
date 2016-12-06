# opencvapi

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
source activate opencvapi
python app/server.py
```

## Testing
```
$ curl -X PUT -F "image=@filename.jpg" http://localhost:5000/face

{
  "face_count": 2
}
```
