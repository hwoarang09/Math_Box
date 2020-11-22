{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "import socket\n",
    "\n",
    "server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)\n",
    "\n",
    "server.bind('13.124.80.47', 5001 )\n",
    "\n",
    "server.listen(0)\n",
    "\n",
    "client, addr = server.accept()\n",
    "data = client.recv(65535)\n",
    "\n",
    "print(\"recieve Data : \", data.decode())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
