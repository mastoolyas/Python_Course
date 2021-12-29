def fib(cnt):         # Generator will always operate on function
    print("Innnnnn")  # will display it only on the first call of the for loop
    n1 = 1
    n2 = 1
    current = 0

    while current < cnt:
        current += 1
        if current <= 2:
            yield 1          # a sign of a generator, yield stop the function a return the value, in the next call
                             # it will retuen to the while and not the beginng of the function
        else:
            n3 = n1 + n2
            n1, n2 = n2, n3
            yield n3


res = fib(10)  # notting happens yet
for n in res:  # the previous item was deleted from memory
    print(n)

# x = fib(50)
