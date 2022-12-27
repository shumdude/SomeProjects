imitated_classes = {}
answers = []
n = int(input())
for i in range(n):
    new_class = input().split()
    imitated_classes[new_class[0]] = []
    if len(new_class) > 1:
        imitated_classes[new_class[0]] += new_class[2:]
print(imitated_classes)


def recursion_function(target_parent, parents_list):
    if target_parent in parents_list:
        return True
    else:
        for element in parents_list:
            if recursion_function(target_parent, imitated_classes[element]):
                return True


q = int(input())

for i in range(q):
    parent, child = input().split()
    if recursion_function(parent, imitated_classes[child]) or parent == child:
        answers.append('Yes')
    else:
        answers.append('No')

for i in answers:
    print(i)

#  оно работает!!! я молодец
