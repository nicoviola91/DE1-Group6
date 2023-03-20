FROM ubuntu:22.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt install -y openjdk-11-jre-headless
RUN apt install -y scala
RUN apt install -y wget
RUN apt install -y screen
RUN apt-get -y install net-tools
RUN apt-get install -y python3-pip
#RUN pip3 install pyspark===3.3.2 
#RUN pip3 install notebook
RUN apt-get -y install git
# Install mongo-spark connector
RUN git clone https://github.com/mongodb/mongo-spark.git
WORKDIR mongo-spark
RUN ./gradlew clean check
WORKDIR /
CMD jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=
