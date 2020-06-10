"""Factory Method - pattern that generates classes.

Defines an interface for creating an object, but leaves subclasses
with a decision about which class to instantiate.

Allows you to delegate instantiation to subclasses.
"""


class FactoryMethod:
    """Factory Method - pattern that generates classes.

    The class works as a decorator.
    A class is created in which variables are initialized that point
    to the object that is generated at the right time.

    Example:
        @FactoryMethod
        class A():
            object_1 = class_1
            object_2 = class_2

    Client code:
        A.object_1()
    """

    __instanse = None

    def __new__(cls, *args, **kwargs):
        """Singleton pattern implementation."""
        if cls.__instanse is None:
            cls.__instanse = super().__new__(cls)
        return cls.__instanse

    def __init__(self, cls, *args, **kwargs):
        """Initialize."""
        self.class_ = cls

    def __getattr__(self, name):
        """Get the value of the specified variable."""
        try:
            x = self.class_.__dict__[name]
        except KeyError:
            raise AttributeError(
                f'Class \'{self.class_.__name__}\' does not contain \
                an attribute named \'{name}\'') from None
        else:
            return x

    def __setattr__(self, name, value):
        """Set the value of a variable."""
        if name != 'class_':
            if self.check_unique(value):
                setattr(self.class_, name, value)
            else:
                raise AttributeError(
                    f'Class \'{self.class_.__name__}\' should contain\
                    only unique values')
        else:
            super().__setattr__(name, value)

    def __call__(self):
        """Call when the instance is “called” as a function."""
        return self.__instanse

    def check_unique(self, value):
        """Check the uniqueness of variable values."""
        for v in self.class_.__dict__.values():
            if v == value:
                return False
        return True
