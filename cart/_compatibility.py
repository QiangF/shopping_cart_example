import sys

is_py3 = sys.version_info[0] >= 3


def utf8(string):
    """Cast to unicode DAMMIT!
    Written because Python2 repr always implicitly casts to a string, so we
    have to cast back to a unicode (and we now that we always deal with valid
    unicode, because we check that in the beginning).
    """
    if is_py3:
        return str(string)
    elif not isinstance(string, unicode):
        return unicode(str(string), 'UTF-8')
    return string


def use_metaclass(meta, *bases):
    """ Create a class with a metaclass. """
    if not bases:
        bases = (object,)
    return meta("HackClass", bases, {})
