# Kafka Zookeeper Docker Container
## Overview
This is simply a docker compose file so that you can launch a ready made container that runs Apache Zookeeper and Kafka in a container to test your Kafka applications

## Build and Run
Simply change directory to the checkout root and run
```docker-compose up -d```
this will download and spin up a container with 2 services one for zookeeper and the other running kafka. 

## Accessing the container 
You can access a bash shell of the container by running 
```docker run -it kafka-zookeeper /bin/bash```

## Using the Kafka Instance
Kafka is exposed on port 9092. If you need to use it then Zookeeper is exposed on port 2181.

## Guide to Kafka Producers and Consumers
Consumer information can be found [here](https://docs.confluent.io/platform/current/clients/consumer.html) and producer docs [here](
https://docs.confluent.io/platform/current/clients/producer.html)