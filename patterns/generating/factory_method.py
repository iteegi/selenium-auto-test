"""Factory Method - pattern that generates classes.

Defines an interface for creating an object, but leaves subclasses
with a decision about which class to instantiate.

Allows you to delegate instantiation to subclasses.
"""

from typing import Callable, TypeVar

T = TypeVar('T')


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

    def __init__(self, cls: T, *args, **kwargs) -> None:
        """Initialize."""
        self.class_ = cls

    def __getattr__(self, name: str) -> Callable[..., bool]:
        """Get the value of the specified variable."""
        try:
            x: Callable[..., bool] = self.class_.__dict__[name]
        except KeyError:
            raise AttributeError(
                f'Class \'{self.class_.__name__}\' does not contain' +
                f'an attribute named \'{name}\'') from None
        else:
            return x

    def __setattr__(self, name: str, value: Callable[..., bool]) -> None:
        """Set the value of a variable."""
        if name != 'class_':
            if self.check_unique(value):
                setattr(self.class_, name, value)
            else:
                raise AttributeError(
                    f'Class \'{self.class_.__name__}\' should contain' +
                    f'only unique values')
        else:
            super().__setattr__(name, value)

    def __call__(self) -> 'FactoryMethod':
        """Call when the instance is “called” as a function."""
        return self

    def check_unique(self, value: Callable[..., bool]) -> bool:
        """Check the uniqueness of variable values."""
        for v in self.class_.__dict__.values():
            if v == value:
                return False
        return True
