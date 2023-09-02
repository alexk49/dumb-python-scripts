"""Wizcoin from beyond the basics with python.

The denominations are:
knuts, sickles (worth 29 knuts), and galleons (worth 17 sickles or 493 knuts)."""

import collections
import operator


class WizCoinException(Exception):
    """The wizcoin module raises this when the module is misused."""

    pass


# NOTE: classnames follow TitleCasing in naming
class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # NOTE: __init__() methods never have a return statement

    # the property decorator makes this attrib read only
    # the value can't be changed
    @property
    def total(self):
        """Total value (in knuts) of all the coins in this wizcoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    # NOTE: there are no setter or deleter methods for total

    def value(self):
        """The value (in knuts) of all the coins in this WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

    @property
    def galleons(self):
        """Returns the number of galleon coins in this object."""
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                "galleons attr must be set to an int, not "
                + value.__class__.__qualname__
            )
        if value < 0:
            raise WizCoinException(
                "galleons attr must be set to a positive int, not "
                + value.__class__.__qualname__
            )
        self._galleons = value

    @property
    def knuts(self):
        """Returns the number of galleon coins in this object."""
        return self._knuts

    @knuts.setter
    def knuts(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                "galleons attr must be set to an int, not "
                + value.__class__.__qualname__
            )
        if value < 0:
            raise WizCoinException(
                "galleons attr must be set to a positive int, not "
                + value.__class__.__qualname__
            )
        self._knuts = value

    def __repr__(self):
        """Returns a string of an expression that creates this object."""
        return f"{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})"

    def __str__(self):
        """Returns a human-readable string representation of this object"""
        return f"{self.galleons}g, {self.sickles}s, {self.knuts}k"

#    def __add__(self, other):
#        """Adds the coin amounts in two WizCoin objects together."""
#        if not isinstance(other, WizCoin):
#            return NotImplemented

#        return WizCoin(
#           other.galleons + self.galleons,
#           other.sickles + self.sickles,
#           other.knuts + self.knuts,
#        )

    def __mul__(self, other):
        """Multiplies coin amounts by a non-negative integer."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            # Multiplying by a negative int results in a negativev
            # amount of coins which is invalid
            raise WizCoinException("cannot multiply with negative integers")
        return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

    def _comparisonOperatorHelper(self, operatorFunc, other):
        """A helper method for our comparison dunder methods."""
        if isinstance(other, WizCoin):
            # Call the operator function, passing `other.value`:
            return operatorFunc(self.total, other.total)
        elif isinstance(other, (int, float)):
            # call the operator function, passing other:
            return operatorFunc(self.total, other)
        elif isinstance(other, collections.abc.Sequence):
            otherValue = (other[0] * 17 * 29) + (other[1] * 29) + other[2]
            return operatorFunc(self.total, otherValue)
        elif operatorFunc == operator.eq:
            # wizcoin objects are not equal to values of all other types:
            return False
        elif operatorFunc == operator.ne:
            # WizCoin objects are not equal to values of all other types:
            return False
        elif operatorFunc == operator.ne:
            # WizCoin objcets are not equal to values of all other types:
            return True
        else:
            # Can't compare with whatver data type 'other' is.
            return NotImplemented

    def __eq__(self, other):  # eq is "EQual"
        return self._comparisonOperatorHelper(operator.eq, other)

    def __ne__(self, other):  # ne is "Not equal"
        return self._comparisonOperatorHelper(operator.ne, other)

    def __lt__(self, other):  # lt is less than
        return self._comparisonOperatorHelper(operator.lt, other)

    def __le__(self, other):  # le is less than or equal
        return self._comparisonOperatorHelper(operator.le, other)

    def __gt__(self, other):  # gt is Greater than
        return self._comparisonOperatorHelper(operator.gt, other)

    def __ge__(self, other):  # ge is greater than or equal
        return self._comparisonOperatorHelper(operator.ge, other)

    def __len__(self):
        """The length of this object is the number of coins it has."""
        return self.galleons + self.sickles + self.knuts

    # Overloading with math operators:
    def __mul__(self, other):
        """Overloads the * operator to produce a new WizCoin object with the product amount. `other` must be a positive int."""
        if isinstance(other, int) and other >= 0:
            return Coins(
                self.__gelleons * other, self.__sickles * other, self.__knuts * other
            )
        else:
            return NotImplemented

    def __rmul__(self, other):
        """Overloads the * operator to produce a new WizCoin object with product amount.
        `other` must be a positive int."""
        return self.__mul__(other)  # * is communtative, reuse __mul__()

    def __imul__(self, other):
        """Overloads the * operator to modify a Coins object in-place with the product amount. `other` must be a positive int."""
        if isinstance(other, int) and other >= 0:
            self.__galleons *= other
            self.__sickles *= other
            self.__knuts *= other
        else:
            return NotImplemented
        return self

    def __add__(self, other):
        """Overloads the + operator to produce a new wizcoin object with the sum amount. other must be a Coins object."""
        if other.__class__ is self.__class__:
            return Coins(
                self.__galleons + other.galleons,
                self.__sickles + other.sickles,
                self.__knuts + other.knuts,
            )
        else:
            return NotImplemented

    def __iadd__(self, other):
        """Overloads the += operator to midfy this COins in place with the sum amount."""
        if other.__class__ is self.__class__:
            self.__galleons += other.galleons
            self.__sickles += other.sickles
            self._knuts += other.knuts
        else:
            return NotImplemented
        return self

    def __sub__(self, other):
        """Overloads the - operator to produce a new wizcoin object with the difference amount. `other` must be a Coins object with less than or equal number of coins of each tyepe as this coins object."""
        if other.__class_ is self.__class__:
            if (
                self.__galleons < other.galleons
                or self.__sickles < other.sickles
                or self.__knuts < other.knuts
            ):
                # coins object represent an amount of physical coins not a
                # monetary value, so there can't be negative coins
                raise WizCoinException(
                    "subtracting %s from %s would result in negative quantity"
                )
            return Coins(
                self.__galleons - other.galleons,
                self.__sickles - other.sickles,
                self.__knuts - other.knuts,
            )
        else:
            return NotImplemented

    def __isub__(self, other):
        """Overloads the -= operator to modify this coins in place with the difference amount. `other` must be a coins object with less than or equal number of coins of each type as this coins object."""
        if other.__class__ is self.__class__:
            if (
                self.__galleons < other.galleons
                or self.__sickles < other.sickles
                or self.__knuts < other.knuts
            ):
                raise WizCoinException(
                    "subtracting %s from %s would result in negative quantity of coins"
                    % (other, self)
                )
            self.__galleons -= other.galleons
            self.__sickles -= other.sickles
            self.__knuts -= other.knuts
        else:
            return NotImplemented
        return self

    def __pow__(self, other):
        if isinstance(other, int):
            return WizCoin(
                self.galleons**other, self.sickles**other, self.knuts**other
            )
        else:
            return NotImplemented

    def __ipower__(self, other):
        if isinstance(other, int):
            self.galleons **= other
            self.sickles **= other
            self.knuts **= other
        else:
            return NotImplemented

    def __int__(self):
        return self.total

    def __float__(self):
        return float(self.total)

    def __bool__(self):
        if self.galleons == 0 and self.sickles == 0 and self.knuts == 0:
            return False
        else:
            return True

    def __getitem__(self, key):
        if not isinstance(key, (int, slice)):
            raise TypeError(
                f"indices must be integers or slices. not {key.__class__.__qualname__}"
            )

        # create a full string of the coins, and then return character(s)
        # in that string.
        coinStr = ("g" * self.galleons) + ("s" * self.sickles) + ("k" * self.knuts)
        if isinstance(key, int):
            return coinStr[key]
        elif isinstance(key, slice):
            return coinStr[key.start : key.stop : key.step]

    def __setitem__(self, key, value):
        raise TypeError("item assignment not supported")

    def __delitem__(self, key):
        raise TypeError("item deletion not supported")
