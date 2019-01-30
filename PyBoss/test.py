def social_security(ssn):

    x = ssn.split("-")

    for elements in x[:2]:
        empty_str = ''
        for i in range(len(elements)):
            empty_str+='*'
        x[x.index(elements)]=empty_str
    
    social = '-'.join(x)
    
    print(social)


social_security('213434-45412123-5235')