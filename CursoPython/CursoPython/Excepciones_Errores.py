#raise BlockingIOError()#en vez de throw, como en C# se usa raise

try: #control de excepciones
   3/0
except ZeroDivisionError as e:
    print("Division entre cero")
