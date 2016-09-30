"""
Some good examples about string usage in Python.
"""


def fill_template(name):
    return "fill %s" % (name)


def fill_template_named(name):
    return "fill {name}".format(name=name)


def fill_template_dict(name):
    return "fill %(name)s" % {'name': name}
