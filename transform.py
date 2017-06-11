import math as m


class Transform:
    def __init__(self, b, c):
        self.C1 = b * b + c * c
        self.C2 = 2.0 * b * c
        self.C3 = b * b - c * c
        self.C4 = 2.0 * b
        pass

    # sqrt(pow(b, 2)+pow(c, 2)-2*b*c*cos(alpha))
    def __d(self, alpha, beta):
        return m.sqrt(self.C1 - self.C2 * m.cos(beta - alpha))

    def __theta(self, alpha, beta):
        v_d = self.__d(alpha, beta)
        xi = m.acos((self.C3 + v_d * v_d) / (self.C4 * v_d))
        theta = alpha - xi
        return m.fabs(theta), 1 if alpha > xi else -1

    def f(self, alpha, beta, gamma):
        v_d = self.__d(alpha, beta)
        theta, flag = self.__theta(alpha, beta)
        k = v_d * m.cos(theta)
        z = v_d * m.sin(theta) * flag
        x = k * m.sin(gamma)
        y = k * m.cos(gamma)
        return x, y, z

    @staticmethod
    def __i_d(x, y, z):
        return m.sqrt(x * x + y * y + z * z)

    def __C(self, x, y, z):
        v_id = self.__i_d(x, y, z)
        k = (self.C3 + v_id * v_id) / (self.C4 * v_id)
        r = m.asin(k)
        return r

    def __D(self, x, y, z):
        v_id = self.__i_d(x, y, z)
        k = (self.C1 - v_id * v_id) / self.C2
        r = m.asin(k)
        return r

    @staticmethod
    def __Z(x, y, z):
        if z == 0:
            return 0.0
        return m.atan(m.sqrt(x * x + y * y) / z)

    def i(self, x, y, z):
        if y == 0:
            gamma = 0.0
        else:
            gamma = m.atan(x / y)
        C_plus_Z = self.__C(x, y, z) + self.__Z(x, y, z)
        alpha = -C_plus_Z
        v_D = m.degrees(self.__C(x, y, z))
        beta = m.pi / 2 + self.__D(x, y, z)
        return m.degrees(alpha), m.degrees(beta), m.degrees(gamma)
