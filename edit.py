# coding=utf-8
import subprocess
import re


def op_edit(order):
    regex = re.compile(r' *edit +"(?P<name>(?:.+))" *(?:in /(?P<in>(?:.+))/?)?')
    if regex.match(order).group('name'):
        path = regex.match(order).group('name')
        if regex.match(order).group('in'):
            path = regex.match(order).group('in') + '/' + path
            if re.match(r'home/.+', path):
                path = '/' + path
        subprocess.call(['nano', path + '.txt'])
    return
