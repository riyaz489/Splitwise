from helpers.Optimal_account_balancing import balance_account
from helpers.data_objects import Group,UserExpense,Expense,User


class GroupHandler:

    def __init__(self):
        self.groups = {}

    def add_group(self, name):
        self.groups[name] = Group(name=name, users=set())

    def add_memeber(self, gn: str, un: str):
        self.groups[gn].users.add(un)

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
        self.expenses = {}

    def add_expense(self, total_amt, user_amt_map, grp_name:Group,  name):
        u_map = []
        for um in user_amt_map:
            if um[1] == 0:
                continue
            t = UserExpense(user=um[0], amount=um[1] )
            u_map.append(t)

        if grp_name.name in self.expenses:

            self.expenses[grp_name.name].append(Expense(name=name, grp=grp_name, user_expense=u_map, total=total_amt))

        else:
            self.expenses[grp_name.name] = [(Expense(name=name, grp=grp_name, user_expense=u_map, total=total_amt))]


    def settle_grp_expense(self, grp_name):
        # first aggregate all users balance
        balance = {}
        for e in self.expenses[grp_name]:
            for u in e.user_expense:
                if u.user in balance:
                    balance[u.user] += u.amount
                else:
                    balance[u.user] = u.amount
        # then call the algo to settle balances
        return balance_account(balance)


