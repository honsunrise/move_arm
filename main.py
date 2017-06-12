from time import sleep

from move import Move

if __name__ == '__main__':
    move = Move(105, 150)
    while True:
        move.to(0, 150, 105 * 1)
        sleep(1)
        move.to(0, 150, 105 / 3)
        sleep(1)
        move.to(0, 150, 105 / 3 * 2)
        sleep(1)
    move.close()
