# TODO решите задачу
import json

def task() -> float:
    with open('input.json') as f:
        data = json.load(f)

    totalSum = 0
    for item in data:
        totalSum += item["score"] * item["weight"]
    return round(totalSum, 3)


print(task())
