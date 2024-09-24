Source : geekeforgeeks : 
All our python files to render the templates will be put directly under the repository and the jinja templates would be put under templates folder. We will run the python programs from the repository as the current working directory/folder and any files rendered will be saved in renders folder.

## Installing python 
- First get the python extension in the visual studio to highlight the syntax 
- next download python from [here](https://www.python.org/downloads/) 
- create a vistual ~venv environment and select the path of the installed python as the python interpreter 

## Installing Jinja2 
- After installing python and setting up the interpreter, install jinja2 using pip 
- use the following command in the VS terminal
- python -m pip install jinja2

## Setup the project
- Create 2 folders in teh project repository as described in teh beginning :  templates, renders

## Rendering a template 
- Step 1: Import the necessary libraries and components (objects, functions, etc.) from libraries.
- Step 2: Create a jinja rendering environment and store it in a variable. This environment will be used in further steps.
- Step 3: Load the template in a variable.
- Step 4: Render the template using <template-object>.render() function to obtain text.
- Step 5: Print the rendered text to the screen or a file as suitable.

## Code
- create helloWorld.jinja
- create helloWorld.py 
- run .py file
