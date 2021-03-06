info = {'global': [[], [], 'built-in']}  # namespace: [[vars], [children], parent]


def create(namespace, parent):
    info[parent][1].append(namespace)
    info[namespace] = [[], [], parent]


def add(namespace, var):
    info[namespace][0].append(var)


def get(namespace, var):
    try:
        if var in info[namespace][0]:
            print(namespace)
        else:
            get(info[namespace][2], var)
    except KeyError:
        print(None)


def request_processing(inp):
    request, namespace, arg = inp.split()
    if request == 'create':
        create(namespace, arg)
    elif request == 'add':
        add(namespace, arg)
    elif request == 'get':
        get(namespace, arg)


while True:
    text = input()
    if text == 'stop':
        break
    else:
        request_processing(text)
