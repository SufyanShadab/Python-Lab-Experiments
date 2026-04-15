# Base class
class X:
    def alpha(self):
        x = 5
        print(x)


# single inheritance
class Y(X):
    def beta(self):
        y = 8
        print(y)


obj = Y()
obj.alpha()
obj.beta()


# multiple inheritance
class M:
    def gamma(self):
        m = 15
        print(m)


class Z(M, X):
    def delta(self):
        z = 20
        print(z)


obj1 = Z()
obj1.alpha()
obj1.gamma()
obj1.delta()


# hybrid inheritance
class P(X):
    def epsilon(self):
        p = 2
        print(p)


class Q(Y, P):
    def zeta(self):
        q = 25
        print(q)


obj2 = Q()
obj2.alpha()
obj2.beta()
obj2.epsilon()
obj2.zeta()


# multilevel inheritance
class R(X):
    def eta(self):
        r = 30
        print(r)


class S(R):
    def theta(self):
        s = 40
        print(s)


obj3 = S()
obj3.alpha()
obj3.eta()
obj3.theta()


# hierarchical inheritance
class T(X):
    def iota(self):
        t = 50
        print(t)


class U(X):
    def kappa(self):
        u = 60
        print(u)


obj4 = T()
obj4.alpha()
obj4.iota()

obj5 = U()
obj5.alpha()
obj5.kappa()


# polymorphism
class V:
    def operate(self, a):
        return a * 2


class W(V):
    def operate(self, a, b):
        print("double:", super().operate(a))
        return a + b


obj6 = W()
print("sum:", obj6.operate(6, 4))