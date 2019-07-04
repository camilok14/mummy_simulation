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
# docker
```
docker pull camilok14/mummy-simulation
docker run -it -e TIMELAPSE=5 -e POPULATION=100 -e DISTRIBUTION=normal -p 3030:3030 mummy-simulation
```