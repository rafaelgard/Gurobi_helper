# Gurobi_helper
This project is a set of multiple usefull functions to utilize with Gurobipy library

## What the code does?
- Show all the variales final values and results about the model in a legible way to read
- Create a .csv file with the information about all the variables in the model includind they values and indexes separated by column.<br/>
- Create the files model.lp and model.sol
- Create a .csv file with all the model results

## Example of Results
![Retorno](https://user-images.githubusercontent.com/25333881/146276009-3b0bdb83-4716-47b7-a7f3-d545f8e1a2ad.png)

## How to run the code?
Passo 1 - Install all the required packages by the pip<br/>
Passo 2 - Put the file Gurobi_helper.py in the same paste of your code and import the class Gurobi_helper<br/>
Passo 3 - Call the class passing the inicial parameters model and True or False<br/>

## Config
If you want only the variables with non zero values, you should pass "True" as the second parameter, but if you want to include the variables that contain zeros in the final values you shold pass the parameter "False" as the second parameter.<br/>

Obs: Verify the file example_1.py on past "Examples" the see how to utilize correcly the code.<br/>

## Limitations of the program
Your model should be runining fine and find at least one solution.

## Pacotes Requeridos
- python 3
- pandas
- numpy
- gurobipy
