from queue import Queue


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.circle_buffer = Queue(capacity)

    def read(self):
        if self.circle_buffer.empty():
            raise BufferEmptyException('No items to read.')
        return self.circle_buffer.get_nowait()

    def write(self, data):
        if self.circle_buffer.full():
            raise BufferFullException('Items cannot be written to a full '
                                      'queue until a slot becomes free.')

        self.circle_buffer.put_nowait(data)

    def overwrite(self, data):
        if self.circle_buffer.full():
            self.circle_buffer.get_nowait()

        self.circle_buffer.put_nowait(data)

    def clear(self):
        while not self.circle_buffer.empty():
            self.circle_buffer.get_nowait()
