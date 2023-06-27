def get_ranges(lst):
    res = []
    for i in range(len(lst)):
        if i == 0:
            min_ = lst[0]
            max_ = lst[0]
        else:
            if (lst[i] - max_ ) == 1:
                max_ = lst[i]
            else:
                if min_ == max_:
                    res.append(str(min_))
                else:
                    res.append(str(min_) + '-' + str(max_))
                min_ = lst[i]
                max_ = lst[i]
        if i == len(lst)-1:
            if min_ == max_:
                res.append(min_)
            else:
                res.append(str(min_) + '-' + str(max_))
    return(res)

get_ranges([0, 1, 2, 3, 4, 8, 10])
