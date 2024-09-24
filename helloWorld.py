from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader('templates')) #identifying and setting up the environment where all jinja files will be 
template = env.get_template('helloWorld.jinja') #loading the jinja file 
output = template.render() #assigning the contents of the jinja file to output 
## method 1 : to print in the terminal
##print(output) # printing the output 

##method 2 : to save the output in a new file in the renders folder created 
with open("renders/helloWorld.txt", 'w') as f:
    print(output, file = f)

