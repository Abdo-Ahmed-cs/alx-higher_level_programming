#!/usr/bin/python3
class LockedClass:
    """
    defining a class that prevents the user from
    initiating any new attributer unless it is called
    first_name
    """

    __slots__ = ["first_name"]

