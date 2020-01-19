class Parent:
    def func(self):
        print("Parent Class.")


class Child(Parent):
    def func(self):
        print("Child Class.")


ob = Child()
ob.func()