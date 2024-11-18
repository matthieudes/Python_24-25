import animal

def test_animal_say_hello():
    animale = animal.Animal("Hugo")
    assert animale.say_hello() == f"Hello, my name is {animale.name}"

def test_dog_say_hello():
    dog = animal.Dog("Buddy")
    assert dog.say_hello() == f"Woof, my name is {dog.name}"


def test_cat_say_hello():
    cat = animal.Cat("Whiskers")
    assert cat.say_hello() == f"Meow, my name is {cat.name}"
