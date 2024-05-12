from typing import TypedDict
from dataclasses import dataclass

# command = input("Enter a command > ")
# operand = float(input("Enter an operand > "))

# # switch case

# match command:
#     case "add":
#         print("do add numbers")
#     case "subtract":
#         print("do subtract numbers")
#     case _:
#         print("command not recognized")

# # match multiple values

# match command:
#     case "add" | "subtract":
#         print(f"do {command} numbers")
#     case _:
#         print("command not recognized")

# # match with conditions

# match command:
#     case "divide" if operand == 0:
#         print("cannot divide by zero")
#     case "add" | "subtract" | "multiply" | "divide":
#         print(f"do {command} numbers")
#     case _:
#         print("command not recognized")

# # match with list variable binding

# history = [
#     ["subtract", 10],
#     ["add", 20],
#     ["multiply", 30],
# ]

# for operation in history:
#     match operation:
#         case ["add", value]:
#             print(f"do add numbers: {value}")
#         case ["subtract", value]:
#             print(f"do subtract numbers: {value}")
#         case ["multiply", value]:
#             print(f"do multiply numbers: {value}")

# # match with dictionary variable binding

# class HistoryEntry(TypedDict):
#     id: int
#     name: str
#     operand: float


# history2: list[HistoryEntry] = [
#     {"id": 1, "name": "add", "operand": 23.0},
#     {"id": 2, "name": "multiply", "operand": 12.0},
#     {"id": 3, "name": "divide", "operand": 5.0},
# ]

# for operation2 in history2:
#     match operation2:
#         case {"id": op_id, "name": "add", "operand": op_value}:
#             print(f"{op_id} add {op_value}")
#         case _:
#             print("unsupported")


# # matching with a general object


# @dataclass
# class HistoryEntry2:
#     id: int
#     name: str
#     operand: float


# history3 = [
#     HistoryEntry2(1, "add", 23.5),
#     HistoryEntry2(2, "subtract", 13.5),
#     HistoryEntry2(3, "multiply", 6.5),
# ]

# for operation3 in history3:
#     match operation3:
#         case HistoryEntry2(id, "add", value):
#             print(f"{id} add {value}")
#         case HistoryEntry2(id, "subtract", value):
#             print(f"{id} subtract {value}")
#         case _:
#             print("unsupported")
