from socket import *
from threading import Thread

MAX_BUFFER = 2048
MAX_PUBLISHER = 10
BROKER_ADDR = ('127.0.0.1', 50000)
waiting_lists = {}

def wait_subscribers():
	global subscriber_socket 
	subscriber_socket = socket(AF_INET, SOCK_DGRAM)
	subscriber_socket.bind(BROKER_ADDR)

	while True:
		topic, addr = subscriber_socket.recvfrom(MAX_BUFFER)
		topic = topic.decode('UTF-8')

		if topic in waiting_lists:
			waiting_lists[topic].append(addr)
		else:
			waiting_lists[topic] = [addr]

	subscriber_socket.close()

def wait_publishers():
	publisher_socket = socket(AF_INET, SOCK_STREAM)
	publisher_socket.bind(BROKER_ADDR)
	publisher_socket.listen(MAX_PUBLISHER)

	while True:
		s, addr = publisher_socket.accept()
		try:
			Thread(target = handle_publisher, args = (s, addr, )).start()
		except:
			print('Cannot start thread..')

	publisher_socket.close()

def handle_publisher(s, addr):
	topic = s.recv(MAX_BUFFER).decode('UTF-8')
	print('New publisher connected.. Topic is "{}" {}'.format(topic, addr))

	while True:
		msg = s.recv(MAX_BUFFER).decode('UTF-8')
		
		if msg == '__CANCEL__':
			break
		
		print('{}> {}'.format(topic, msg))
		if topic in waiting_lists:
			for subscriber_addr in waiting_lists[topic]:
				subscriber_socket.sendto(msg.encode('UTF-8'), subscriber_addr)

	s.close()
	print('Publisher is canceled.. Topic is "{}" {}'.format(topic, addr))

def main():
	print('Broker started..')
	Thread(target = wait_subscribers).start()
	wait_publishers()		

if __name__ == '__main__':
	main()