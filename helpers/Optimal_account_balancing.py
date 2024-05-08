# here we will try to generate all possible permutations of -ve and +ve list items.
# to do so we will fix -ve items list, we will start removing first element from -ve list.
# then that first element of -ve list will make pair with every item of +ve list.
# and recursively this will go on.
# once a -ve and +ve item pair built, the we will be remaining either with 0 , +ve or -ve as remainder.
# so if we got 0 we will ignore, but if we got -ve then that remainder will ber added to -ve list otherwise
# remainder will be added to +ve list.

# Its basically DFS traversal with Backtracking and DP.
# this code is also similar to permutations code.
def balance_account(data:dict):
    p_list = {}
    n_list = {}
    for k,v in data.items():
        if v<0:
            n_list[k] = v
        elif v>0:
            p_list[k] = v
    dp = {}

    def rec(p):
        count = float('inf')
        path = ''

        if len(p_list) ==0 and len(n_list)==0:
            return 0, p # both lists become empty then return path so far and current cost. which is 0 for last node

        elif len(p_list) ==0:
            return float('inf'), p # if not possible then cost will be infinity.
        elif len(n_list) == 0:
            return float('inf'), p

        if (tuple(p_list), tuple(n_list)) in dp:
            return dp[(tuple(p_list), tuple(n_list))]
            # if similar +ve and -ve list already traversed
            # then ignore duplicate traversal

        amt = n_list.pop(0)

        for i in range(len(p_list)):
            # we will try all subtraction permutations of -ve list first item with positive list all items.
            # we will pick positive list items one by one.
            g_amt = p_list.pop(i)
            n_amt = g_amt + amt

            # if new amount is negative then add it to -ve list else to postive list.
            if n_amt >0:
                p_list.insert(0,n_amt)
            elif n_amt <0:
                n_list.insert(0, n_amt)

            tp = p+(f'{g_amt}-{amt}, ') # generating string path, as string is immutable, so each
            # recursion stack will have its own path copy. so no need to undo it.
            c, pp = rec(tp)
            c+=1

            # if cost is leser then update path
            if c<count:
                path = pp
                count = c

            # for backtracking purpose we will undo all modifications we did above.
            if n_amt >0:
                p_list.pop(0)
            elif n_amt <0:
                n_list.pop(0)
            p_list.insert(i, g_amt)

        # for backtracking purpose we will undo -ve list
        n_list.insert(0, amt)

        # update result for problem into dp
        dp[(tuple(p_list), tuple(n_list))]= (count, path)
        return (count, path)


    return rec('')



if __name__ == '__main__':
    data= [80,25,-25,-20,-20,-20,-20]
    data2 = [50,30,40,100,100, -200, -70,-50]
    print(balance_account(data))
    print(balance_account(data2))
