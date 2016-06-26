import socket
import threading
import queue
import time
data = [] #for testing purposes
def sender(port, send_queue):
	host = '127.0.0.1'
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:#DGRAM for UDP sockets
		s.bind((host, port))
		s.listen(1)
		conn, addr = s.accept()
		print('Connected by', addr)
		while(True):
			#would actuall be:
			#msg = send_queue.get_nowait()
			#conn.sendall(data)
			data.pop()
			data.append(conn.recv(2048)+1)
			conn.sendall(data)
def receiver(port, receive_queue):
	#same thing as the client side from python docs
	host = '127.0.0.1'
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #DGRAM for UDP sockets
	#need to receive data
	#will be implemented after proof of concept
	s.bind((host, port))
	s.listen(1)
	conn, addr = s.accept()
	#while(True):
		#msg = conn.recv(2048)
		#recv_queue.putnowait(msg)

send_queue = queue.Queue()
recv_queue = queue.Queue()
send_port = 1235
recv_port = 1236

send_thread = threading.Thread(target=sender, name = "ansible_sender", args=(send_port, send_queue))
recv_thread = threading.Thread(target=receiver, name = "ansible_receiver", args=(recv_port,  recv_queue))
send_thread.daemon = True
recv_thread.daemon = True
send_thread.start()
recv_thread.start()

while(True):
	time.sleep(1)
	1/0
	print(data)

	

