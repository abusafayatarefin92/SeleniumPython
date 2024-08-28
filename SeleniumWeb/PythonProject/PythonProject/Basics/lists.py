class list(object):
    """
    Built-in mutable sequence.

    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified.
    """

    def append(self, *args, **kwargs):  # real signature unknown
        """ Append object to the end of the list. """
        pass #important

    def clear(self, *args, **kwargs):  # real signature unknown
        """ Remove all items from list. """
        pass #important

    def copy(self, *args, **kwargs):  # real signature unknown
        """ Return a shallow copy of the list. """
        pass #important

    def count(self, *args, **kwargs):  # real signature unknown
        """ Return number of occurrences of value. """
        pass #important

    def extend(self, *args, **kwargs):  # real signature unknown
        """ Extend list by appending elements from the iterable. """
        pass

    def index(self, *args, **kwargs):  # real signature unknown
        """
        Return first index of value.

        Raises ValueError if the value is not present.
        """
        pass #important list.index(x[, start[, end]])

    def insert(self, *args, **kwargs):  # real signature unknown
        """ Insert object before index. """
        pass #important

    def pop(self, *args, **kwargs):  # real signature unknown
        """
        Remove and return item at index (default last).

        Raises IndexError if list is empty or index is out of range.
        """
        pass #important

    def remove(self, *args, **kwargs):  # real signature unknown
        """
        Remove first occurrence of value.

        Raises ValueError if the value is not present.
        """
        pass #important

    def reverse(self, *args, **kwargs):  # real signature unknown
        """ Reverse *IN PLACE*. """
        pass #important

    def sort(self, *args, **kwargs):  # real signature unknown
        """
        Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).

        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.

        The reverse flag can be set to sort in descending order.
        """
        pass #important list.sort(*, key = None, reverse = False)

    def __add__(self, *args, **kwargs):  # real signature unknown
        """ Return self+value. """
        pass

    def __class_getitem__(self, *args, **kwargs):  # real signature unknown
        """ See PEP 585 """
        pass

    def __contains__(self, *args, **kwargs):  # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs):  # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, y):  # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args, **kwargs):  # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):  # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs):  # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs):  # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, seq=()):  # known special case of list.__init__
        """
        Built-in mutable sequence.

        If no argument is given, the constructor creates a new empty list.
        The argument must be an iterable if specified.
        # (copied from class doc)
        """
        pass

    def __iter__(self, *args, **kwargs):  # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs):  # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs):  # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    def __reversed__(self, *args, **kwargs):  # real signature unknown
        """ Return a reverse iterator over the list. """
        pass

    def __rmul__(self, *args, **kwargs):  # real signature unknown
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs):  # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sizeof__(self, *args, **kwargs):  # real signature unknown
        """ Return the size of the list in memory, in bytes. """
        pass

    __hash__ = None