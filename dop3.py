data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def summ(a):
    summ_otw = 0
    for i in a:
        if isinstance(i, int):
            summ_otw += i
        if isinstance(i, str):
            summ_otw += len(i)
        if isinstance(i, list):
            summ_otw += summ(i)
        if isinstance(i, dict):
            summ_otw += (summ(i.keys()) + summ(i.values()))
        if isinstance(i, tuple):
            summ_otw += summ(i)
        if isinstance(i, set):
            summ_otw += summ(i)
    return summ_otw

print(summ(data_structure))