class partner:
    def __init__(self):
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, a):
        self.__age = a
    
    def del_age(self):
        del self.__age

    age = property(get_age, set_age, del_age)

mark = partner()
mark.age = 18
mark.__age = 15
print(mark.age)