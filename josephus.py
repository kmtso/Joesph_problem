from queuem import*

n = int(input("total numbers of people:"))

m = int(input("count (Starting from the second person):"))
q = Queue()
for i in range(1, n+1):
    enqueue(q, i)

eli = Queue()
while not isemptyq(q):
    skip = dequeue(q)
    enqueue(q, skip)
    for i in range(1, m+1):
        if i != m:
            skip = dequeue(q)
            enqueue(q, skip)
        else:
            enqueue(eli, dequeue(q))

print("the sequence of elimination:", end="")
displayq(eli)
