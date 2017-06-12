import serial
from transform import Transform


class Move:
    def __init__(self, b, c, port='/dev/ttyUSB0', baudrate=19200):
        self.m1 = 0
        self.m2 = 0
        self.m3 = 0
        self.offset_m1 = 0
        self.offset_m2 = 24 - 90  # 90
        self.offset_m3 = 180 - 61  # 180
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = baudrate
        self.ser.open()
        self.transform = Transform(b, c)

    def close(self):
        self.ser.close()

    def __rotate_m1(self, degrees):
        self.m1 = degrees

    def __rotate_m2(self, degrees):
        self.m2 = degrees

    def __rotate_m3(self, degrees):
        self.m3 = degrees

    # #1P600#2P900#8P2500T100\r\n
    # P 500-2500
    # T 100-9999
    def __degrees_to_pos(self, degrees):
        pos_per_degree = 2000 / 180
        return 1500 + degrees * pos_per_degree

    def __do(self):
        t = 100
        param = '#1P%d#2P%d#3P%dT%d\r\n' % \
                (self.__degrees_to_pos(self.m1), self.__degrees_to_pos(self.m2), self.__degrees_to_pos(self.m3), t)
        self.ser.write(param)

    def to(self, x, y, z):
        alpha, beta, gamma = self.transform.i(x, y, z)
        self.__rotate_m1(gamma + self.offset_m1)
        self.__rotate_m2(alpha + self.offset_m2)
        self.__rotate_m3(-beta + self.offset_m3)
        self.__do()
