from collections import deque
from timeit import timeit

test_dq = deque()
test_lst = list()
my_lst = [i for i in range(200, 300)]


print('Операции append')
print(timeit('for i in range(100): test_dq.append(i)', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst.append(i)', globals=globals(), number=10000))
print('Операции extend')
print(timeit('for i in range(100): test_dq.extend(my_lst)', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst.append(my_lst)', globals=globals(), number=10000))
print('Операции pop')
print(timeit('for i in range(100): test_dq.pop()', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst.pop()', globals=globals(), number=10000))


test_dq.clear()
test_lst.clear()


print('Операции appendleft')
print(timeit('for i in range(100): test_dq.appendleft(i)', globals=globals(), number=1000))
print(timeit('for i in range(100): test_lst.insert(0, i)', globals=globals(), number=1000))
print('Операции extendleft')
print(timeit('test_dq.extendleft(my_lst)', globals=globals(), number=10000))
print(timeit('my_lst + test_lst', globals=globals(), number=10000))
print('Операции popleft')
print(timeit('for i in range(10): test_dq.pop()', globals=globals(), number=10000))
print(timeit('for i in range(10): test_lst.pop(0)', globals=globals(), number=10000))

test_dq.clear()
test_lst.clear()


for i in range(101):
    test_lst.append(i)

for i in range(101):
    test_dq.append(i)

print('Операции получения элемента')
print(timeit('for i in range(100): test_dq[randint(0, 100)]', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst[randint(0, 100)]', globals=globals(), number=10000))

"""
В операциях добавления в конец списка, чуть лучше себя показал deque за исключением метода extend,
по добавлению в начало выигрывает deque
в получении элемента примерно равны, чуть лучше список
Вывод: deque лучше, когда нужно что-то дописать или извлечь 
list эффективен при произвольном доступе к элементам

"""