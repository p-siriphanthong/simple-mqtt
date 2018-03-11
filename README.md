# Simple MQTT
MQTT (MQ Telemetry Transport) is a popular application layer protocol for Internet of Things (IoT) applications. The communication model is the published-subscribed pattern, which consists of three node roles – Publisher, Subscriber, and Broker. A publisher publishes its topic to Broker and one or more subscribers subscribe for the topic. Whenever the publisher publishes data, Broker will automatically relay it to all nodes subscribed to that topic.
<br /><br />
This is a simple command-line version of MQTT with the above functionality. So, the software will have three parts – publisher, broker, and subscriber. The software can be coded in Python language.
<br /><br />
You can download source codes at [github](https://github.com/p-siriphanthong/simple_mqtt)
### Prerequisites
Python version is Python 3.6+
<br />
The packages require:
* sys
* socket
* threading
* atexit
* shlex
### Running
1. Get started with Broker
```
python Broker.py
```
2. Start Subscriber and attach the topic with 1 argument
```
python Subscriber.py Topic
```
or
```
python Subscriber.py "Topic With Space"
```
3. Start Publisher
```
python Publisher.py
```
* Create topic for communicate to Subscribers: `topic "Topic With Space"`
* Send message: `publish "Message With Space"`
* Cancel current topic: `cancel "Topic With Space"`
<br /><br />
> You can run many Subscribers and Publishers at the same time.
<br />
> Publisher can send a massage serveral times before cancel topic.