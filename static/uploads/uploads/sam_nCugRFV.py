def sam(s):
    out={}
    a=s.split()
    for i in a:
        if len(i)>=5:
            out[i]=i+str(len(i))
        else:
            out[i]=i[::-1]
    return out
print(sam('python is easy'))
