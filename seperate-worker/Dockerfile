FROM ubuntu:22.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt install -y openjdk-11-jre-headless
RUN apt-get install -y python3-pip
RUN apt install -y scala
RUN apt install -y wget
RUN apt install -y screen
RUN wget https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz
RUN tar xvf spark-3.3.2-bin-hadoop3.tgz
RUN mv spark-3.3.2-bin-hadoop3/ /usr/local/spark
ENV PATH="${PATH}:$SPARK_HOME/bin"
ENV SPARK_HOME="/usr/local/spark"
ENV SPARK_NO_DAEMONIZE="true"
# The following can be uncommented when we know this works
#RUN apt-get -y install git
#RUN git clone https://github.com/mongodb/mongo-spark.git
#WORKDIR mongo-spark
#RUN ./gradlew clean check
#WORKDIR /
ENTRYPOINT $SPARK_HOME/sbin/start-worker.sh spark://192.168.2.249:7077

