FROM python
COPY . /app
WORKDIR /app
RUN pip3 install numpy nose scipy flask flask_restful tinydb
EXPOSE 3030
CMD python3 . -t ${TIMELAPSE} -p ${POPULATION} -d ${DISTRIBUTION}