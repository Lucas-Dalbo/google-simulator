import pytest
from ting_file_management.priority_queue import PriorityQueue


BIG_FILE = {
    "nome_do_arquivo": "big_1",
    "qtd_linhas": 6,
    "linhas_do_arquivo": ["muitas linhas"],
}

SMALL_FILE = {
    "nome_do_arquivo": "small",
    "qtd_linhas": 4,
    "linhas_do_arquivo": ["poucas linhas"],
}


def test_basic_priority_queueing():
    __test_priority_len()
    __test_dequeue()
    __test_search()
    __test_search_error()


def __test_priority_len():
    p_queue = PriorityQueue()
    p_queue.enqueue(BIG_FILE)
    p_queue.enqueue(SMALL_FILE)
    assert p_queue.high_priority.__len__() == 1
    assert p_queue.regular_priority.__len__() == 1


def __test_dequeue():
    p_queue = PriorityQueue()
    p_queue.enqueue(BIG_FILE)
    p_queue.enqueue(SMALL_FILE)
    removed = p_queue.dequeue()
    assert removed == SMALL_FILE


def __test_search():
    p_queue = PriorityQueue()
    p_queue.enqueue(BIG_FILE)
    p_queue.enqueue(SMALL_FILE)
    searched = p_queue.search(0)
    assert searched == SMALL_FILE


def __test_search_error():
    p_queue = PriorityQueue()
    p_queue.enqueue(BIG_FILE)
    p_queue.enqueue(SMALL_FILE)
    with pytest.raises(IndexError):
        p_queue.search(3)
