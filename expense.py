from data_objects import Group,UserExpense,Expense,User,AmountType
from Optimal_account_balancing import balance_account


class GroupHandler:

    def __init__(self):
        self.groups = {}

    def add_group(self, name):
        self.groups[name] = Group(name=name, users=set())

    def add_memeber(self, gn, un):
        self.groups[gn].users.append(un)

    def show_groups(self):
        return set(self.groups.keys())


class UserHandler:

    def __init__(self):
        self.users = {}

    def add_user(self, name):
        self.users[name] = User(name=name)

    def show_users(self):
        return set(self.users.keys())


class ExpenseHandler:

    def __init__(self):
        self.expenses = []

    def add_expense(self, total_amt, user_amt_map, grp_name, amnt_type:AmountType, name):
        u_map = []
        for um in user_amt_map:
            if um[1] == 0:
                continue
            if amnt_type == AmountType.percent:
                t = UserExpense(user=um[0], percent=um[1], amount=um[1] * total_amt /100 )
            else:
                t = UserExpense(user=um[0], percent=um[1] *100/ total_amt, amount=um[1] )
            u_map.append(t)

        self.expenses.append(Expense(name=name, grp=grp_name, user_expense=u_map, total=total_amt))


    def settle_grp_expense(self, grp_name):
        pass


