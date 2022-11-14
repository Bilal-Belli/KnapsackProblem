def total_value(items, max_weight):
    return  sum([x[2] for x in items]) if sum([x[1] for x in items]) <= max_weight else 0
cache = {}
def solve(items, max_weight):
    if not items:
        return ()
    if (items,max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include = (head,) + solve(tail, max_weight - head[1])
        dont_include = solve(tail, max_weight)
        if total_value(include, max_weight) > total_value(dont_include, max_weight):
            answer = include
        else:
            answer = dont_include
        cache[(items,max_weight)] = answer
    return cache[(items,max_weight)]
items = (("Objet_1", 10, 12), ("Objet_2", 12, 13), ("Objet_3", 8, 14), ("Objet_4", 15, 20),
    ("Objet_5", 16, 21), ("Objet_6", 18, 22), ("Objet_7", 25, 23), ("Objet_8", 8, 10),
    ("Objet_9", 13, 11), ("Objet_10", 20, 16),
    )
max_weight = 100
solution = solve(items, max_weight)
print("Les Objets: ")
for x in solution:
    print(x[0])
print("Valeur Max:", total_value(solution, max_weight))
print("Poid Max:", sum([x[1] for x in solution]))