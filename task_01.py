#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This function calculate temprature."""


from decimal import Decimal

ABSOLUTE_DIFFERENCE = Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """ This function will convert fahrenheit to celsius.

    Args:
        degrees (mixed): temperature measurement
        fc (decimal): value
    Returns:
        temperature in celcius
    Example:
        >>>fahrenhiet_to_celsius(30.0)
        -1.111
    """

    return (Decimal(degrees) -32)*5/9


def celsius_to_kelvin(degrees):
    """ This function convert celsius to kelvin.

    Args:
        degrees (mixed): temperature value
        ck (decimal): value
    returns:
        temperature in kelvin
    Example:
        >>>celsius_to_kelvin(10)
        283.15
    """

    return Decimal(degrees)+ ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """This function convert fahrenheit to kelvin.

    Args:
       degrees (mixes): temperature measurement
       fk (decimal): values
    returns:
       temperature in kelvin
    Examples:
        >>> fahrenhiet_to_kelvin(30.2)
        272.26
    """

    # celsius_to_kelvin(fahrenheit_to_celsius())
    celsius = fahrenheit_to_celsius(degrees)
    kelvin = celsius_to_kelvin(celsius)

    return kelvin
