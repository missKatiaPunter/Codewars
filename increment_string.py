def increment_string(strng):
    strng=list(strng)
    num=''
    num2=''
    numnum=0
    if strng==[]:
        return '1'
    if ord(strng[len(strng)-1])<=47 or ord(strng[len(strng)-1])>=58:
        strng.append('1')
    
    else:
        i=len(strng)-1
        while i>=0:
            if ord(strng[i])>47 and ord(strng[i])<58:
                num=strng[i]+num
                del(strng[i])
                i=i-1
            else:
                break
        numnum = int(num)
        numnum+=1
        num2=str(numnum)
        zeros=len(num)-len(num2)
        for i in range(0, zeros):
            strng.append('0')
        strng.append(num2)
    return ''.join(strng)
