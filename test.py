def extender(func):
    def extra(word):
        return func(f"{word} ashhab")
    return extra
    


@extender
def show(word):
    print(word)


word="hello world"
show(word)