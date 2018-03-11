import sys
from socket import *

MAX_BUFFER = 2048
BROKER_ADDR = ('127.0.0.1', 50000)

def main():
	if len(sys.argv) != 2:
		print('Warning! Topic must be 1 argument')
		exit()

	topic = sys.argv[1]
	print('Subscriber started.. Topic is "{}"'.format(topic))

	s = socket(AF_INET, SOCK_DGRAM)
	s.sendto(topic.encode('UTF-8'), BROKER_ADDR)

	while True:
		msg, _ = s.recvfrom(MAX_BUFFER)
		print('> {}'.format(msg.decode('UTF-8')))

	s.close()

if __name__ == '__main__':
	main()