import shlex
import atexit
from socket import *

MAX_BUFFER = 2048
BROKER_ADDR = ('127.0.0.1', 50000)

def handle_exit():
	global s
	if 's' in globals():
		s.send('__CANCEL__'.encode('UTF-8'))
		s.close()

def get_input():
	msg = shlex.split(input('> '))
	return msg, len(msg)

def main():
	while(True):
		global s
		arg, len_arg = get_input()
		command = arg[0].lower()

		if command == 'topic':
			if 's' in globals():
				print('Warning! Please cancel current topic before [Current topic is "{}"]'.format(topic))
			elif len_arg != 2:
				print('Warning! The topic must be 1 argument')
			else:
				try:
					topic = arg[1]
					s = socket(AF_INET, SOCK_STREAM)
					s.connect(BROKER_ADDR)
					s.send(topic.encode('UTF-8'))
				except:
					print('Cannot connect to broker..')
					del s

		elif command == 'publish':
			if 's' not in globals():
				print('Warning! Please assign topic before')
			elif len_arg != 2:
				print('Warning! Message must be 1 argument')
			else:
				s.send(arg[1].encode('UTF-8'))

		elif command == 'cancel':
			if 's' not in globals():
				print('Warning! Please assign topic before')
			elif len_arg != 2:
				print('Warning! The topic must be 1 argument')
			elif topic != arg[1]:
				print('Warning! The topics not match [Current topic is "{}"]'.format(topic))
			else:
				s.send('__CANCEL__'.encode('UTF-8'))
				s.close()
				del s

		elif len_arg == 1 and command == 'quit':
			exit()

		else:
			print('Warning! The command is wrong')

if __name__ == '__main__':
	atexit.register(handle_exit)
	main()