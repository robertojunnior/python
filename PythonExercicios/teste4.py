def checa_valor( list ):
    elem = list[ 0 ]
    for a in list:
        if a > elem:
            elem = a
    return elem

print(checa_valor([4, 10, 18, -7]))
