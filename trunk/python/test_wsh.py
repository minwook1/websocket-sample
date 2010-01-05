#!/usr/bin/python

from mod_pywebsocket import msgutil

import thread
import getopt
import os
import sys
import time

_GOODBYE_MESSAGE = 'Goodbye'
_HEARTBEAT_ = 'Heartbeat'
_CONNECTING_ = 0
_OPEN_ = 1
_CLOSE_ = 2


_status_ = _CONNECTING_

class tail():

	last_mtime = None

	def __init__(self, filename, delay, sock):
		self.filename = filename
		self.delay = delay
		self.sock = sock

	def run(self):
		self.sendConnInfo()
		while True:
			if _status_ != _OPEN_:
				msgutil.send_message(self.sock, "status = "+str(_status_))
				break
			time.sleep(self.delay)
			stat = os.stat(self.filename)
			
			if stat.st_mtime != self.last_mtime:
				self.last_mtime = stat.st_mtime
				self.read()

	def read(self):
		try:
			length = 0
			f = open(self.filename, 'r')
			for line in f:
				length += 1

			f.seek(0)
			cnt = 0

			for line in f:
				cnt += 1
				if cnt == length:
					msgutil.send_message(self.sock, line[:-1])
			f.close
		except Exception:
			if(f):
				f.close

	def sendConnInfo(self):
		params = "ws_location : "+str(self.sock.ws_location) + "<br />"
		params += "ws_origin : "+str(self.sock.ws_origin) + "<br />"
		params += "ws_protocol : " + str(self.sock.ws_protocol)+"<br />"
		params += "ws_resource : " + str(self.sock.ws_resource)+"<br />"
		msgutil.send_message(self.sock, params)




def web_socket_do_extra_handshake(request):
	pass  # Always accept.

file = '/home/komasshu/websock_handler/test'

def web_socket_transfer_data(request):
	global _status_
	_status_ = _OPEN_
	attr = ()
	thread.start_new_thread(tail(file, 0.5, request).run, attr)
	while True:
		try:
			line = msgutil.receive_message(request)
			
			if line == _HEARTBEAT_:
				continue
		
			f = open(file, 'a')
			f.write(line+"\n")
			os.fsync(f.fileno())
			f.flush()
			f.close
			
#			if line == _GOODBYE_MESSAGE:
#				_status_ = _CLOSE_
#				return
		except Exception:
			_status_ = _CLOSE_
			return

