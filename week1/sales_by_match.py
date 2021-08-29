def sockMerchant(n, ar):
    unique = set(ar)
    pairs = 0
    for i in unique:
        if(ar.count(i)%2 == 0):
            pairs += ar.count(i)//2
        else:
            pairs += (ar.count(i) - 1)//2
    return(pairs)
