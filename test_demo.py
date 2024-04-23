import time


def testa():
    print(f'--------------, {time.time()}\n')
    assert 1 == 1
    time.sleep(2)
    # assert int(time.time()) != 1713853810
