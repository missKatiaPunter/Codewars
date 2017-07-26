def sort_array(source_array):
    odds=[]
    if source_array==[]:
        return source_array
    for i in range(0,len(source_array)):
        if source_array[i]%2==0:
            pass
        else:
            odds.append(source_array[i])
            source_array[i]='swap'
    odds.sort()
    for i in range(0,len(source_array)):
        if source_array[i]=='swap':
            source_array[i]=odds[0]
            odds=odds[1:]
            print(odds)
        else:
            pass
    return source_array
