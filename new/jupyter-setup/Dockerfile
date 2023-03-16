FROM ubuntu:22.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt install -y openjdk-8-jre-headless
RUN apt install -y scala
RUN apt install -y wget
RUN apt install -y screen
RUN apt-get -y install net-tools
RUN apt-get install -y python3-pip
RUN pip3 install pyspark===3.2.3 
RUN pip3 install notebook
RUN apt install -y curl
RUN apt-get -y install git
RUN curl -L https://services.gradle.org/distributions/gradle-8.0.2-bin.zip -o  gradle-8.0.2-bin.zip
RUN apt-get install -y unzip
RUN unzip gradle-8.0.2-bin.zip
ENV GRADLE_HOME=/app/gradle-8.0.2
ENV PATH="$PATH:$GRADLE_HOME/bin"
RUN export PATH=$PATH:/opt/gradle/gradle-8.0.2/bin
RUN git clone https://github.com/mongodb/mongo-spark.git
# RUN cd mongo-spark
# RUN ./gradlew clean check
EXPOSE 8888
CMD jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=
