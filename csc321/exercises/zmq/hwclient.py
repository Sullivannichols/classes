#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://macbeth.local:5555")

#  Do 10 requests, waiting each time for a response
request = 0
while True:
    request += 1
    print("Sending request %s ..." % request)
    socket.send(b"Hi my name is Brandon Randle.")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))