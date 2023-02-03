from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__queue_data = list()

    def __len__(self):
        return len(self.__queue_data)

    def enqueue(self, value):
        self.__queue_data.append(value)

    def dequeue(self):
        if self.__len__() == 0:
            return None
        return self.__queue_data.pop(0)

    def search(self, index):
        if index < 0 or index > (self.__len__() - 1):
            raise IndexError("Invalid index")
        return self.__queue_data[index]
