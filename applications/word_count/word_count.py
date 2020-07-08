def word_count(s):
    ignored ='" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    
    s = s.lower()

    for i in ignored:
        s = s.replace(i, " ")

    cache = {}
    for i in s.split():
        cache[i] = s.split().count(i)
    
    return cache




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))