from time import sleep
from move import Move

if __name__ == '__main__':
    move = Move(110, 150)
    move.open()
    while True:
        move.to(0, 100, 20)
        sleep(1)
        move.to(100, 100, 10)
        sleep(1)
        move.to(-100, 100, 30)
        sleep(1)
    move.close()
