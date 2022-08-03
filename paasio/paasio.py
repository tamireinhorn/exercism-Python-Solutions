import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""
    # Subclassing means that you start the parent class using super
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._calls_for_reading = 0
        self._calls_for_writing = 0
        self._bytes_written = 0
        self._bytes_read = 0

    def __enter__(self): # This is a method for context managing, basically.
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Since the class it inherits from already has this method:
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        # The file is already iterable, so:
        return self

    def __next__(self):
        data = super().readline() # The class this inherits from has a method for reading a line.
        self._update_reads(data)
        if data:
            return data
        else:
            raise StopIteration # If there is nothing, we have to stop.
        
    def _update_reads(self, data):
        self._calls_for_reading += 1
        self._bytes_read += len(data)

    def read(self, size=-1):
        # The super class also has a read method:
        data = super().read(size)
        self._update_reads(data)
        return data

    @property
    def read_bytes(self):
        return self._bytes_read

    @property
    def read_ops(self):
        return self._calls_for_reading

    def write(self, b):
        #Same logic as read:
        size = super().write(b)
        self._bytes_written += size
        self._calls_for_writing += 1
        return size

    @property
    def write_bytes(self):
        return self._bytes_written

    @property
    def write_ops(self):
        return self._calls_for_writing


class MeteredSocket:
    """Implement using a delegation model.""" # This means that we DELEGATE the functions to the socket.

    def __init__(self, socket):
        self._socket = socket
        self._calls_for_receiving = 0
        self._calls_for_sending = 0
        self._bytes_received = 0
        self._bytes_sent = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        data = self._socket.recv(bufsize, flags)
        self._calls_for_receiving += 1
        self._bytes_received += len(data)
        return data

    @property
    def recv_bytes(self):
        return self._bytes_received

    @property
    def recv_ops(self):
        return self._calls_for_receiving

    def send(self, data, flags=0):
        self._calls_for_sending += 1
        size = self._socket.send(data, flags)
        self._bytes_sent += size
        return size

    @property
    def send_bytes(self):
        return self._bytes_sent

    @property
    def send_ops(self):
        return self._calls_for_sending
