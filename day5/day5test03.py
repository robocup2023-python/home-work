def data():
    import random
    with open("data.txt","w")as file:
        for _ in range(100000):
            file.write(str(random.randint(1,100)))
