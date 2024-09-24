from jinja2 import Environment, FileSystemLoader

## loading the environment 
env = Environment(loader=FileSystemLoader('templates'))

##poinitng at the jinja file
template = env.get_template('webTable.jinja')

##rendering the jinja file with the input as 5  
output = template.render(tableOf = 5)

##printing the output 
with open("renders/webTable.html","w") as f :
    print(output , file = f)

