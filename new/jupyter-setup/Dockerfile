FROM ubuntu:22.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt install -y openjdk-11-jre-headless
RUN apt install -y scala
RUN apt install -y wget
RUN apt install -y screen
RUN apt-get -y install net-tools
RUN apt-get install -y python3-pip
RUN pip3 install pyspark===3.3.2 
RUN pip3 install notebook
RUN pip3 install h5py
RUN apt-get -y install git
# Install mongo-spark connector
RUN git clone https://github.com/mongodb/mongo-spark.git
WORKDIR mongo-spark
RUN ./gradlew clean check
WORKDIR /
# install spark
RUN wget https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz
RUN tar xvf spark-3.3.2-bin-hadoop3.tgz
RUN mv spark-3.3.2-bin-hadoop3/ /usr/local/spark
ENV PATH="${PATH}:$SPARK_HOME/bin"
ENV SPARK_HOME="/usr/local/spark"
ENV SPARK_NO_DAEMONIZE="true"
RUN $SPARK_HOME/bin/spark-shell --packages org.mongodb.spark:mongo-spark-connector_2.12:10.1.1
CMD jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=
