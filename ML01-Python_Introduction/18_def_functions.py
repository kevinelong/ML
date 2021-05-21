def addTwo(a: int = 0, b: int = 0) -> int:
    return a + b


addResult1 = addTwo()  # uses default parameters
print(addResult1)

addResult2 = addTwo(2, 4)
print(addResult2)


def twice(text):
    return text + text  # CONCATENATE
    #     return f"{text}{text}"


twiceResult = twice("abc")
print(twiceResult)
