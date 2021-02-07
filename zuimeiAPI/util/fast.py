# coding=<encoding name> ： # coding=utf-8
import concurrent.futures


def do_fast(name, *data):
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        executor.map(name, *data)
