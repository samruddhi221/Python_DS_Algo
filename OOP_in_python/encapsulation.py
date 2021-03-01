# single underscore '_': protected members
# double underscore '__': private members


class Base:
    def __init__(self):
        self.public_var = 2
        self._protected_var = 3
        self.__private_var = 4

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("public var:", self.public_var)
        print("protected var:", self._protected_var)
        #print("private var:", self.__private_var)


if __name__ == '__main__':
    d = Derived()
    print(d.public_var)
    print(d._protected_var)
    print(d.__private_var)