
#question number 10
def camel(string):
    snake = ''.join(['_'+i.lower() if i.isupper() else i for i in string]).lstrip('_')
    kebab = ''.join(['-'+i.lower() if i.isupper() else i for i in string]).lstrip('-')
    print(snake, kebab, sep=" , " )


string = input("Enter CamelCased String: ")
camel(string)



