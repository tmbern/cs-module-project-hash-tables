def no_dups(s):
    empty_list = []

    for i in s.split():
        if i not in empty_list:
            empty_list.append(i)
    
    return " ".join(empty_list)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))