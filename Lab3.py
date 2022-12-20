import random


class Vertex:
    def __init__(self, key, leftSon, rightSibling):
        self.key = key
        # значение в вершине
        self.leftSon = leftSon
        # левый ребенок вершины
        self.rightSibling = rightSibling
        # ссылки на "братьев" данной вершины


def depth(nums, i, head):
    if (int(nums[i]) < int(head.key)):
        if (head.leftSon.key == 0):
            if (int(head.leftSon.rightSibling.key) > 0):
                head.leftSon = Vertex(nums[i], Vertex(
                    0, Vertex(0, 0, 0), Vertex(0, 0, 0)), head.leftSon.rightSibling)
            else:
                head.leftSon = Vertex(nums[i],  Vertex(0,  Vertex(0, 0, 0),  Vertex(
                    0, 0, 0)),  Vertex(0, Vertex(0, 0, 0), Vertex(0, 0, 0,)))
        else:
            depth(nums, i, head.leftSon)
    else:
        if (head.leftSon.rightSibling.key is None or head.leftSon.rightSibling.key == 0):
            if (int(head.leftSon.key) == 0):
                head.leftSon = Vertex(0,  Vertex(0,  Vertex(0, 0, 0),  Vertex(
                    0, 0, 0)),  Vertex(0, 0, 0))
            head.leftSon.rightSibling = Vertex(nums[i],  Vertex(0,  Vertex(
                0, 0, 0),  Vertex(0, 0, 0)), Vertex(0,  Vertex(0, 0, 0), Vertex(0, 0, 0)))
        else:
            depth(nums, i, head.leftSon.rightSibling)


newNums = ''


def semetry(vertex):
    global newNums
    if (int(vertex.leftSon.key) > 0):
        semetry(vertex.leftSon)
        if (int(vertex.leftSon.rightSibling.key) > 0 and int(vertex.leftSon.key) > 0):
            newNums = newNums[:len(newNums)]
        else:
            newNums += str(vertex.key)
    if (int(vertex.leftSon.rightSibling.key) > 0):
        newNums += str(vertex.key)
        semetry(vertex.leftSon.rightSibling)
    if (vertex.leftSon.rightSibling.key == 0 and vertex.leftSon.key == 0):
        newNums += str(vertex.key)


def straight(vertex):
    global newNums
    if (int(vertex.key) > 0):
        newNums += str(vertex.key)
        straight(vertex.leftSon)
        straight(vertex.leftSon.rightSibling)


def back(vertex):
    global newNums
    if (vertex.key > 0):
        back(vertex.leftSon)
        back(vertex.leftSon.rightSibling)
        newNums += str(vertex.key)


arrayTree = []


def treeToArr(head, i, loor):
    global arrayTree
    arrayTree[i][loor] += str(head.key)
    if (head.leftSon != None and int(head.leftSon.key) > 0):
        arrayTree[i+1][loor] += str(head.key) + "->"
        treeToArr(head.leftSon, i+1, loor)
        arrayTree[i+1][loor] += " "

    if (head.leftSon.rightSibling != None and int(head.leftSon.rightSibling.key) > 0):
        if arrayTree[i + 1][loor] == None:
            arrayTree = '-'
        else:
            arrayTree[i+1][loor]

        if str(head.key) == arrayTree[i][loor] and head.leftSon.key != 0:
            arrayTree[i+1][loor] += str(head.leftSon.key) + "->"
            treeToArr(head.leftSon.rightSibling, i+1, loor)
            arrayTree[i+1][loor] += " "
        else:
            arrayTree[i+1][loor] += str(head.key) + "->"
            treeToArr(head.leftSon.rightSibling, i+1, loor)
            arrayTree[i+1][loor] += " "


def buildTree(nums, typeRead):
    global arrayTree
    newNums = ''
    arr = []
    arr2 = []
    arr3 = []

    for j in range(1, 11):
        arr.append(0)

    for i in range(1, 10):
        for j in range(len(nums)):
            if int(nums[j]) == i:
                arr[i] += 1
    weight = []
    temp = []
    for i in range(len(nums)):
        weight.append(round(1/(i+1 + 1), 2))
        temp.append(nums[i])

    a = random.choices(temp, weight, k=1)
    while len(temp) != 0:
        a = random.choices(temp, weight, k=1)

        weight.pop(temp.index(a[0]))
        arr2.append(temp.index(a[0]))
        arr3.append(temp[temp.index(a[0])])
        temp.pop(temp.index(a[0]))

    root = Vertex(int(arr3[0]), Vertex(0, Vertex(0, 0, 0), Vertex(0, 0, 0)), 0)

    for i in range(1, len(arr2)):
        depth(arr3, i, root)

    for i in range(len(arr3)):
        arrayTree.append([''])

    treeToArr(root, 0, 0)
    typeRead(root)
    return (newNums, arr2, arr3)


temp = [int(random.randint(1, 9)) for i in range(5)]
temp2 = [int(random.randint(1, 9)) for i in range(5)]

A = ''
for i in range(len(temp)):
    # A.append(temp[i])
    A += str(temp[i])

B = ''
for i in range(len(temp2)):
    # B.append(temp2[i])
    B += str(temp2[i])

[A_read, A_vertexes, A_price] = buildTree(A, straight)
# print("A:", A)
# for i in range(len(arrayTree)):
#     for j in range(len(arrayTree[i])):
#         if arrayTree[i][j] == '':
#             arrayTree[i].pop(j)

# for i in range(len(arrayTree)):
#     for j in range(len(arrayTree[i])):
#         print(arrayTree[i][j], "\n")

arrayTree = []
[B_read, B_vertexes, B_price] = buildTree(B, semetry)

# print("B:", B)
# for i in range(len(arrayTree)):
#     for j in range(len(arrayTree[i])):
#         if arrayTree[i][j] == '':
#             arrayTree[i].pop(j)

# for i in range(len(arrayTree)):
#     for j in range(len(arrayTree[i])):
#         print(arrayTree[i][j], "\n")

temp_A = A
constly = True
for i in range(len(A)):
    for j in range(len(B)):
        if int(A[i]) == int(B[j]):
            constly = False
    if constly:
        temp_A = A[:i] + A[i+1:]
    constly = True
# print(temp_A)
A = temp_A
arrayTree = []
[A_read, A_vertexes, A_price] = buildTree(A, straight)
print("А = A ⋂ B: ", A)
for i in range(len(arrayTree)):
    for j in range(len(arrayTree[i])):
        if arrayTree[i][j] == '':
            arrayTree[i].pop(j)

for i in range(len(arrayTree)):
    for j in range(len(arrayTree[i])):
        print(arrayTree[i][j], "\n")
