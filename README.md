# PCSS - The Python CSS preprocessor

[![Build Status](https://secure.travis-ci.org/senko/pcss.png?branch=master)](http://travis-ci.org/senko/pcss)


"I Regret Nothing" (Łukasz Langa, EuroPython 2012)

PCSS allows you to write CSS using Python syntax and using all the bells and
whistles that Python as (loops, functions, classes, etc).

## Quick Example

    #!/usr/bin/env python
    from pcss import css, pct, px

    css('div.header',
        width=pct(10),
        height=px(2),
        margin=0,
        _=[
            css('ul > li',
                display='inline-block',
                padding_left=px(10),
                padding_right=px(10))
        ])


    css('div.header a',
        color='blue')


    if __name__ == '__main__':
        print css.dumps()

Saving this to a `.css.py` file and running it with Python, you get the
following CSS:

    div.header ul > li {
            padding-right: 10px;
            display: inline-block;
            padding-left: 10px;
    }

    div.header {
            width: 10.00px;
            margin: 0;
            height: 2px;
    }

    div.header a {
            color: blue;
            display: inline-block;
            padding-left: 10px;
    }

## Installation

Get it from GitHub and install via the standard `python setup.py`:

    git clone https://github.com/senko/pcss.git
    cd pcss
    python setup.py install

## The Syntax

Create CSS declarations by invoking `css`. The first argument should be
the CSS selector string. The keyword arguments specify the CSS attributes
(if the CSS attribute use dashes (`-`), in Python code use underscores
(`_`) instead).

You can have nested CSS declarations by adding a list of `css` invocations
as the `_` keyword argument. The nested declarations will automatically prepend
the parent's selector to their own.

As your PCSS files are actually executable Python code, they should all have
the following (or similar) header:

    #!/usr/bin/env python
    from pcss import css, pct, px

And the footer to display the output if invoked directly:

    if __name__ == '__main__':
        print css.dumps()

You can also import the modules (you'll probably want to skip the `.css.` part
of the suffix then, though). All the processed CSS declarations are stored
globally and are available using `css.dumps()`.

For a working example, look in the `examples/` directory.

## Command Line Usage

You can invoke the PCSS file directly and it will output the CSS. You can
also use `pcss.process` to process all `*.css.py` files in the directory and
create `*.css` files. Or you can use `pcss.watch` to watch the directory
(scans every second) and process the changed `*.css.py` files.

Available syntax:

    python -mpcss.process /path/to/pcss/folder/
    python -mpcss.process # uses current directory
    python -mpcss.watch /path/to/pcss/folder
    python -mpcss.watch # uses current directory


## Minification

If you want to get the minified code back, supply `minify=True` argument to
`css.dumps()`. For example, change the `.css.py` file footer to:

    if __name__ == '__main__':
        print css.dumps(minify=True)


## WHY OH GOD WHY ?!?

Because I can.

## License

Copyright (C) 2013. by Senko Rašić and PCSS contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
