
# a variable in python that holds string value 

message = 'Single quotes are used if there a "Double quote" within the string and vice versa'

message_new = """Triple quotes are used
for multi line string"""

print (message_new)
print(message)

# len funtion returns the number of characters in a message

print ( len (message))

# to access individual characters in a string, we use square brackets, starts 0

print (message[7])

# to print an index to the other

print (message[0:6]) # prints from 0 upto but not including 7th index
print (message[:6]) # prints from 0 anyways
print (message[76:]) # prints right until the end
#^^^ called slicing

print (message.lower()) # prints all in lower case; .upper for upper case

print (message.count('quote')) #counts times 'quote' is repeated in the message

print (message.find('if')) # returns index of where if is found in the message returns negative is char doesn't exist

message = message.replace('are','ARE') # replaces are with ARE

print (message)

greet = 'Hello'
name = 'Tanzil'
new_message = greet + ', ' + name # concat string w a + sign
placeholder = '{}, {}. Welcome!'.format(greet,name) # place holders format string to replace {} with the variables mentioned in format argument in that order

print (placeholder)

fstri = f'{greet}, {name.upper()}. Welcome' # fstrings in pythin 3 onwards make string formatting easier. can even write code within {}

print(fstri)

print(dir(fstri)) # prints all the methods available to be used with that variable 

print(help(str.lower)) # prints all the methods with their description for string's lowe rfunction