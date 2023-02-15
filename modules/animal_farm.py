# nonlocal scope
# changes i made inside are not affecting the value of the global variable
# if i comment out the animal = "elephant", it gives me error

def d():
    animal = "elephant"

    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside nested function: " + animal)

    print("Inside nested function: " + animal)
    e()
    print("After nested function: " + animal)

animal = "camel"
d()
print("Inside nested function: " + animal)

# Inside nested function: elephant
# Inside nested function: giraffe
# After nested function: giraffe
# Inside nested function: camel
