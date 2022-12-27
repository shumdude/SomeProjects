n = int(input())
emulation_namespace = {'global': {'parent': [], 'values': []}}


def create(namespace, parent):
    global emulation_namespace

    emulation_namespace[namespace] = {'parent': [parent], 'values': []}
    # print(emulation_namespace)

    return None


def add(namespace, var):
    global emulation_namespace

    emulation_namespace[namespace]['values'].append(var)
    # print(emulation_namespace)

    return None


def get(namespace, var):
    global emulation_namespace

    if var in emulation_namespace[namespace]['values']:
        print(namespace)
    else:
        if namespace == 'global':
            print(None)
        else:
            parent = emulation_namespace[namespace]['parent'][0]
            get(parent, var)


for i in range(n):
    cmd, name, arg = input().split()
    if cmd == 'create':
        create(name, arg)
    if cmd == 'add':
        add(name, arg)
    if cmd == 'get':
        get(name, arg)


print(emulation_namespace)
