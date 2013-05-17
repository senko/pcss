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

OUTPUT = """div.header ul > li {
\tpadding-right: 10px;
\tdisplay: inline-block;
\tpadding-left: 10px;
}

div.header {
\twidth: 10.00px;
\tmargin: 0;
\theight: 2px;
}

div.header a {
\tcolor: blue;
}
"""

assert css.dumps() == OUTPUT
