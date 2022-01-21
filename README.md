# Gurobi Helper
This project is a set of multiple usefull functions to utilize with Gurobipy library

## What the code does?
- Show all the variales final values and results about the model in a legible way to read
- Create a .csv file with the information about all the variables in the model includind they values and indexes separated by column.<br/>
- Create the files model.lp and model.sol
- Create a .csv file with all the model results

## Example of Results
![image](https://user-images.githubusercontent.com/25333881/150533115-8d476005-0543-43cc-96b6-78c51df2a160.png)


## Final Variables Values in the file variables.csv
![image](https://user-images.githubusercontent.com/25333881/150533625-93b5ea58-0340-4aa0-85cc-896167dae766.png)

## Final Results in the file results.csv
![image](https://user-images.githubusercontent.com/25333881/150534468-c4e4612b-0f8f-48da-882c-9effc70e80c1.png)

## Files created
![image](https://user-images.githubusercontent.com/25333881/150535089-6813b67a-0903-4383-874a-cdf1a2c4eaf0.png)

## How to run the code?
Step 1 - Install all the required packages by the pip<br/>
Step 2 - Put the file Gurobi_helper.py in the same paste of your code and import the class Gurobi_helper<br/>
Step 3 - Call the class passing the inicial parameters model and True or False<br/>
Step 4 - Declare all the variables, parameters, constrains and call the gurobi_helper class as the image bellow
![image](https://user-images.githubusercontent.com/25333881/150536235-433c03e4-ca29-45ad-98a0-21ceae1c4061.png)


## Config
If you want only the variables with non zero values, you should pass "True" as the second parameter, but if you want to include the variables that contain zeros in the final values you shold pass the parameter "False" as the second parameter.<br/>

Obs: Verify the file example_1.py on past "Examples" the see how to utilize correcly the code.<br/>

## Limitations of the program
Your model should be running fine and find at least one solution.

## Pacotes Requeridos
- python 3
- pandas
- numpy
- gurobipy
