# coding=utf-8
import os
import re


def multiple_replace(dictionary, text):
    regex = re.compile("(%s)" % "|".join(map(re.escape, dictionary.keys())))
    if regex.search(text):
        return regex.sub(lambda mo: dictionary[mo.string[mo.start():mo.end()]], text)
    return


def op_find(order):
    anything_find = False
    if re.search("some", order):
        text_temp = ""
        ready = False
        re_result = dict()
        for word in re.findall(r'"(\w+)"', order):
            re_result[word] = '\033[42m' + word + '\033[0m'
        for name_file in os.listdir(os.getcwd()):
            if name_file.endswith(".txt"):
                tmp = open(name_file)
                for line in tmp:
                    if multiple_replace(re_result, line):
                        text_temp += multiple_replace(re_result, line)
                        ready = True
                    else:
                        text_temp += line
                if ready:
                    anything_find = True
                    print "Found in " + name_file + ":\n"
                    print text_temp
                    text_temp = ""
                    ready = False
                    print "------------------------------"
                else:
                    text_temp = ""
                tmp.close()

    elif re.search("exact", order):
        text_temp = ""
        ready = False
        for name_file in os.listdir(os.getcwd()):
            if name_file.endswith(".txt"):
                tmp = open(name_file)
                for line in tmp:
                    find = re.search(r'"(.*?)"', order).group(1)
                    if re.search(find, line):
                        text_temp += re.sub(find, '\033[42m' + find + '\033[0m', line)
                        ready = True
                    else:
                        text_temp += line
                if ready:
                    anything_find = True
                    print "Found in " + name_file + ":\n"
                    print text_temp
                    text_temp = ""
                    ready = False
                    print "------------------------------"
                else:
                    text_temp = ""
                tmp.close()
    else:
        anything_find = True
        print "Error: Incorrect Command"

    if not anything_find:
        print "Nothing was found.."

    return
