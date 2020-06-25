def sentence(words):
    string = ''
    for i in words :
        if i != ' ':
            string += i
        if i == ' ':
            print(string)
            string = ''
    print(string)
            # string = ''


sentence('Winter is coming')



