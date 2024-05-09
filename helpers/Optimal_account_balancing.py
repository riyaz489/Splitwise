# here we will try to generate all possible permutations of -ve and +ve list items.
# to do so we will fix -ve items list, we will start removing first element from -ve list.
# then that first element of -ve list will make pair with every item of +ve list.
# and recursively this will go on.
# once a -ve and +ve item pair built, the we will be remaining either with 0 , +ve or -ve as remainder.
# so if we got 0 we will ignore, but if we got -ve then that remainder will ber added to -ve list otherwise
# remainder will be added to +ve list.
# here basically we are trying to close/settle one user balance at a time let say user A has -20 and user has 30 balance
# then If we make pair of A and B then user A pays user B 20 and then user left with 10. so as you notice user A
# balance is settled.

# Its basically DFS traversal with Backtracking and DP.
# this code is also similar to permutations code.
def balance_account(data: dict):
    p_list = []
    p_user = []
    n_list = []
    n_users = []
    for k,x in data.items():
        if x<0:
            n_list.append(x)
            n_users.append(k)
        elif x>0:
            p_list.append(x)
            p_user.append(k)
    dp = {}

    def rec():
        count = float('inf')
        path = ()

        if len(p_list) ==0 and len(n_list)==0:
            return 0, () # both lists become empty then return path so far and current cost. which is 0 for last node

        elif len(p_list) ==0:
            return float('inf'), () # if not possible then cost will be infinity.
        elif len(n_list) == 0:
            return float('inf'), ()

        if (tuple(p_list), tuple(n_list)) in dp:
            return dp[(tuple(p_list), tuple(n_list))]
            # if similar +ve and -ve list already traversed
            # then ignore duplicate traversal

        amt = n_list.pop(0)
        n_user = n_users.pop(0)

        for i in range(len(p_list)):
            # we will try all subtraction permutations of -ve list first item with positive list all items.
            # we will pick positive list items one by one.
            g_amt = p_list.pop(i)
            g_user = p_user.pop(i)
            n_amt = g_amt + amt

            # if new amount is negative then add it to -ve list else to postive list.
            if n_amt >0:
                p_list.insert(0,n_amt)
                p_user.insert(0,g_user)
            elif n_amt <0:
                n_list.insert(0, n_amt)
                n_users.insert(0,n_user)


            c, pp = rec()
            # notice we are adding cost and path while we are moving from bottom to top.
            # it is because of DP, as DP returns lower subtree path and cost.
            c+=1
            pp = (*pp, (f'{g_user}-- {g_amt if g_amt<=(amt *-1) else (amt*-1)} --> {n_user}'))  # generating string path, as string is immutable, so each
            # recursion stack will have its own path copy. so no need to undo it.
            # if cost is leser then update path
            if c<count:
                path = pp
                count = c

            # for backtracking purpose we will undo all modifications we did above.
            if n_amt >0:
                p_list.pop(0)
                p_user.pop(0)
            elif n_amt <0:
                n_list.pop(0)
                n_users.pop(0)
            p_list.insert(i, g_amt)
            p_user.insert(i,g_user)

        # for backtracking purpose we will undo -ve list
        n_list.insert(0, amt)
        n_users.insert(0,n_user)

        # update result for problem into dp
        dp[(tuple(p_list), tuple(n_list))]= (count, path)
        return (count, path)

    return rec()


if __name__ == '__main__':

    data1 = {'A':80, 'B':25, 'C':-25, 'D':-20, 'E':-20, 'F':-20, 'G':-20}
    data2 = {'A':50, 'B':30, 'C':40, 'D':100, 'E':100, 'F': -200, 'G': -70, 'H':-50}
    data3 = {'A':10, 'B':20, 'C':30, 'D':-45, 'E': -10, 'F':-5}
    print(balance_account(data1))
    print(balance_account(data2))
    print(balance_account(data3))

