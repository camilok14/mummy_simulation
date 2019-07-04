# mummy_simulation

# install
```
pip3 install numpy nose scipy flask flask_restful tinydb
```
# tests
```
nosetests . */
```
# run
```
python3 . -t 5 -p 100 -d normal
```
-t: number of seconds to take 
-p: number of investors of the universe
-d: 'normal' will use normal distribution to generate investors attributes and 'uniform' will use uniform distribution to generate investors attributes
# help
```
python3 . -h
```
# docker
```
docker pull camilok14/mummy-simulation
docker run -it -e TIMELAPSE=5 -e POPULATION=100 -e DISTRIBUTION=normal -p 3030:3030 mummy-simulation
```
# dashboard
https://github.com/camilok14/mummy-dashboard
```
docker pull camilok14/mummy-dashboard
docker run -it -p 4200:80 mummy-dashboard
```