from collections import Counter, deque


class BinaryTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(text):
    count_elem = Counter(text)
    sorted_elem = deque(sorted(count_elem.items(), key=lambda items: items[1]))
    while len(sorted_elem) > 1:
        weight = sorted_elem[0][1] + sorted_elem[1][1]
        node = BinaryTree(left=sorted_elem.popleft()[0], right=sorted_elem.popleft()[0])
        for i, item in enumerate(sorted_elem):
            if weight > item[1]:
                continue
            else:
                sorted_elem.insert(i, (node, weight))
                break
        else:
            sorted_elem.append((node, weight))
    return sorted_elem[0][0]


def haffman_code(tree, path=''):
    if not isinstance(tree, BinaryTree):
        code_table[tree] = path
    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


code_table = dict()
my_text = "one one two two three"
haffman_code(haffman_tree(text))
print(code_table)
for i in my_text:
    print(code_table[i], end=' ')