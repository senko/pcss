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


css('div.header ul > li',
    display='inline-block',
    padding_left=px(10),
    padding_right=px(10))


if __name__ == '__main__':
    print css.dumps()
