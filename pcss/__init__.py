#!/usr/bin/env python


class Measurement(object):

    def __init__(self, val):
        self.value = val

    def _ensure_same_type(self, other):
        if type(self) is not type(other):
            raise ValueError('unit mismatch: %s vs %s' % (self, other))

    def __add__(self, other):
        self._ensure_same_type(other)
        return self.__class__(self.value + other.value)

    def __sub__(self, other):
        self._ensure_same_type(other)
        return self.__class__(self.value - other.value)

    def __mul__(self, n):
        self._ensure_same_type(other)
        return self.__class__(self.value * n)

    def __div__(self, n):
        self._ensure_same_type(other)
        return self.__class__(self.value / n)


class pct(Measurement):
    def __str__(self):
        return '%.2fpx' % self.value


class px(Measurement):
    def __str__(self):
        return '%dpx' % self.value


class css(object):
    all_css = []

    def __init__(self, selector, **attrs):
        self.selector = selector
        self.children = []
        self.attrs = {}
        for child in attrs.pop('_', []):
            child.selector = self.selector + ' ' + child.selector

        for k, v in attrs.iteritems():
            self.attrs[k.replace('_', '-')] = v

        self._add_css(self)

    @classmethod
    def reset(cls):
        cls.all_css = []

    @classmethod
    def _add_css(cls, obj):
        cls.all_css.append(obj)

    def __str__(self):
        header = '%s {\n' % self.selector
        footer = '}\n'
        body = ''.join('\t%s: %s;\n' % (k, str(v))
            for k, v in self.attrs.iteritems())
        return header + body + footer

    @classmethod
    def dumps(cls, minify=False):
        retval = '\n'.join(str(c) for c in cls.all_css)
        if minify:
            import re
            retval = re.sub(r'[\n\t ]+', ' ', retval)
        return retval

    @classmethod
    def dump(cls, fd, minify=False):
        fd.write(cls.dumps(minify=minify))
