from dataclasses import dataclass
from enum import Enum
from typing import Set, List



@dataclass
class User:
    name: str

@dataclass
class Group:
    name: str
    users: Set[User]

@dataclass
class UserExpense:
    user: User
    amount: float

@dataclass
class Expense:
    grp: Group
    name: str
    total: float
    user_expense: List[UserExpense]
    is_settled: bool = False