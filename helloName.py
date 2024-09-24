from jinja2 import Environment, FileSystemLoader

#loading the environment
env = Environment(loader=FileSystemLoader('templates'))

#loading the template 
template = env.get_template('helloName.jinja')

#rendering the template and adding the name input to it 
output = template.render(name = 'Muskan')

#printing the output in a seperate file 
#with open("renders/helloName.txt", 'w') as f: #a function that opens the file specified and has a mode as write so writes into that file
 #   print(output, file = f)

print (output)