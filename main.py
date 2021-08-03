#def is_hello_in_text(text):
    #if 'hello' in text:
        #return True
    #else:
        #return False


#print(is_hello_in_text('Hello everyone!'))


#def is_hello_in_text(text):
    #if 'hello' in text.lower():
        #return True
    #else:
        #return False


#def is_hello_in_text(text):
    #return 'hello' in text.lower()


#print(is_hello_in_text('Hello everyone!'))


#def is_hello_in_text(text):
    #return 'hello' in text.lower()


#print(is_hello_in_text('everyone!'))


#def is_string_in_text(string, text):
    #return string in text


#print(is_string_in_text('he', 'The apple'))
#print(is_string_in_text('hey', 'The apple'))


def greeting_depends_on_gender(name, gender):
    if gender == 'male':
        return gender
        print('Hello ' + name + '! You look great!')
    elif gender == 'female':
        print('Hello ' + name + '! You are so nice!')
        return gender
    else:
        print('Hello ' + name + 'I\'ve never seen the creature like you ')
        return gender


returned_value_1 = greeting_depends_on_gender('Jack', 'male')
returned_value_2 = greeting_depends_on_gender('Jane', 'female')
returned_value_3 = greeting_depends_on_gender('Ja', 'cmale')

print(returned_value_1)
print(returned_value_2)
print(returned_value_3)

