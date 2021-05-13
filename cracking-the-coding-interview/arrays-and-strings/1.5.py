def one_away_helper(st1, st2):
    if abs(len(st1) - len(st1)) > 1:
        return False

    # Equal length handled
    elif len(st1) == len(st2):
        if st1 == st2:
            return True
        else:
            ignored_once = False
            for i in range(len(st1)):
                if st1[i] != st2[i]:
                    if ignored_once is False:
                        ignored_once = True
                    else:
                        return False
            if ignored_once is True:
                return True

    else:
        deletion_failed = False
        addition_failed = False
        for i in range(len(st2)):
            if st1[i] != st2[i]:
                new_string = st1[:i] + st1[i+1:] if i+1 < len(st1) else ""
                if new_string != st2:
                    deletion_failed = True
                else:
                    return True

                new_string = st2[:i] + st1[i] + st2[i:]
                if new_string != st1:
                    addition_failed = True
                else:
                    return True

                print("bitvh")
                return deletion_failed ^ addition_failed

        return st1[:-1] == st2


def one_away(st1, st2):
    if len(st1) >= len(st2):
        return one_away_helper(st1, st2)
    else:
        return one_away_helper(st2, st1)



st1 = "pales"
st2 = "pale"
print(one_away(st1, st2))

