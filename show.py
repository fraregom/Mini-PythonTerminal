# coding=utf-8
import os
import re
import auxiliar

# show "hola mundo"
# show "hola mundo" in /home/cosa
# show all
# show all in /home/cosa
# show all where name is "hola mundo"
# show all where name contains "hola mundo"
# show all where name contains "hola mundo" in /home/cosa
# show all where tag is "taaaags"
# show all where tag is "taaaags" sorted by modified
# show all where name is "hola mundo" sorted by tags  in /home/cosa

# *show +(?:"(?P<name_file>.*)"|(?P<all>all(?: +where(?:(?: +name(?: +is +"(?P<is>.*?)"| +contains +"(?P<contains>.*?)"))|(?: +tag +is +"(?P<tag>.+?)")))?)(?: +sorted +by +(?P<sort>(?:names|tags|modified|creation)))?)(:? +in +/(?P<route>(.*))/*)?

def show(order,path_origin):
    regex = re.compile(r'^ *show +(?:"(?P<name_file>.*)"|'
                       r'(?P<all>all(?: +where(?:(?: +name(?: +is +"(?P<is>.*?)"|'
                       r' +contains +"(?P<contains>.*?)"))|(?: +tag +is +"(?P<tag>.+?)")))?)'
                       r'(?: +sorted +by +(?P<sort>(?:names|tags|modified|creation)))?)'
                       r'(:? +in +/(?P<route>(.*))/?)?$')
    match = regex.match(order)
    if match:
        name = match.group("name_file")
        all = match.group("all")
        iss = match.group("is")
        contains = match.group("contains")
        tag = match.group("tag")
        sort = match.group("sort")
        route = match.group("route")
        if route:
            route = str(route)
            if re.match(r'home/.+', route):
                route = "/"+route+"/"
            else:
                route = os.getcwd()+"/"+route+"/"
        if name:
            if route:
                archivo = open(route + name + ".lpy")
            else:
                archivo = open(name + ".lpy")

            print auxiliar.multiple_replace(auxiliar.styles,archivo.read())
            archivo.close()
        elif all:
            print "all"

    else:
        print "Error: Incorrect Command"
