"================================="
"Gurobi_helper"
"================================="
"Created on: Jan 21, 2021"
"Author: Rafael Gardel Azzariti Brasil"
"https://github.com/rafaelgard/Gurobi_helper"
"================================="

import gurobipy as gp
import numpy as np
import pandas as pd

class gurobi_helper():
    '''This project is a set of multiple usefull functions to utilize with Gurobipy library'''

    def __init__(self, model, only_non_zero_variables):
        self.model = model
        self.only_non_zero_variables = only_non_zero_variables

    def extract_am_of_index(self, variable: str):
        '''Identify the amount of index in the variable'''
        qtd_index = 1

        for c in variable:
            if c == ',':
                qtd_index += 1

        return qtd_index

    def extract_index(self, variable: str):
        '''Identify the indexes in the variable'''

        initial_index = 0
        final_index = 0

        '''Identify the inicial and the final index that countain the indexes'''
        for index, value in enumerate(variable):
            if value == '[':
                initial_index = index

            elif value == ']':
                final_index = index + 1

        '''Create a slice that contain the the indexes'''
        slice = variable[initial_index:final_index]

        ''''Transform the string in list'''
        slice = list(slice)

        '''Create a new list to storage the indexes'''
        indexes = []

        for index, value in enumerate(slice):
            if value.isnumeric() == True:
                indexes.append(int(value))

        return indexes

    def identify_variable_name(self, variable: str):
        '''Identify the variable name'''

        final_index = 0

        for index, value in enumerate(variable):
            if value == '[':
                final_index = index
                break

        variable_name = variable[0:final_index]

        return variable_name

    def extract_variables(self):
        '''Receive the model'''
        m = self.model

        '''Create 2 lists to storage the information about the variables'''
        names_of_variables = []
        values_of_variables = []

        '''Return the variables of model '''
        for v in m.getVars():
            if self.only_non_zero_variables == True:
                if v.x != 0:
                    names_of_variables.append(v.varName)
                    values_of_variables.append(v.x)

            else:
                names_of_variables.append(v.varName)
                values_of_variables.append(v.x)


        '''Each variable has at least one index'''
        qtd_max_index = 1

        '''Iterate over all variables names to determinate the variable with major number of index '''
        for var in names_of_variables:
            qtd = self.extract_am_of_index(var)

            if qtd > qtd_max_index:
                qtd_max_index = qtd

        '''Create a dataframe to storage the information about the variables'''
        df = pd.DataFrame(data=np.zeros(shape=(len(names_of_variables), qtd_max_index + 2)),
                          columns=['Index_' + str(i) for i in range(0, qtd_max_index + 2)])

        '''Change the name of the first column to variable'''
        df = df.rename(columns={'Index_0': 'Variable'})

        '''Change the name of the last column to Value'''
        df = df.rename(columns={df.columns[-1]: 'Value'})

        '''Save the name of the variables on the first column'''
        for index, value in enumerate(names_of_variables):
            df.iloc[index, 0] = self.identify_variable_name(value)

        '''Save the values of the index on the columns'''
        for line_index, variable in enumerate(names_of_variables):
            indices = self.extract_index(variable)

            for index, value in enumerate(indices):
                df.iloc[line_index, index + 1] = value

        '''Save the values on the last column'''
        for index, value in enumerate(values_of_variables):
            df.iloc[index, -1] = value

        '''Return a pandas dataframe with the values of the variables'''
        return df.copy()

    def save_variables(self, df: pd.DataFrame):

        '''Save the values of the variables on a .csv file'''
        pd.DataFrame(df).to_csv('variables.csv', index=False, sep=';', encoding='UTF-8')

    def print_results(self):
        '''This function print the results of the model'''

        '''Receive the model'''
        m = self.model

        print('=========================================')
        print('Amount of Restrictions: ', round(m.NumConstrs, 3))
        print('Amount of Variables: ', round(m.NumVars, 3))
        print('Amount of Binary Variables: ', round(m.NumBinVars, 3))
        print('Amount of NumNZs: ', round(m.NumNZs, 3))
        print('=========================================')
        print('Status of The Model: ', m.Status)
        print('Computational Time', round(m.Runtime, 3))
        print('=========================================')
        print('GAP: ', round(m.MIPGap, 3))
        print('=========================================')
        print('Objective Function Value: ', round(m.ObjVal, 3))
        print('=========================================')

        for v in m.getVars():
            if self.only_non_zero_variables == True:
                if v.x != 0:
                    print('%s %g' % (v.varName, v.x))
                    print('=========================================')

            else:
                print('%s %g' % (v.varName, v.x))
                print('=========================================')


    def save_model_results(self):
        '''This function save the model results in a .csv file'''

        '''Receive the model'''
        model = self.model

        '''Create a dict to storage the results'''
        results = {'Z': [], 'Computational Time': [], 'Amount of Restrictions': [], 'Amount of Variables': [],
                      'Amount of Binary Variables': [], 'NumNZs': [], 'GAP': []}

        '''Save the results'''
        results['Z'].append(round(model.ObjVal, 3))
        results['Computational Time'].append(round(model.Runtime, 3))
        results['Amount of Variables'].append(round(model.NumVars, 3))
        results['Amount of Binary Variables'].append(round(model.NumBinVars, 3))
        results['Amount of Restrictions'].append(round(model.NumConstrs, 3))
        results['NumNZs'].append(round(model.NumNZs, 3))
        results['GAP'].append(round(model.MIPGap, 3))

        '''Save the results in a .csv file'''
        pd.DataFrame(results).to_csv('results.csv', index=False, sep=';', encoding='UTF-8')

    def save_model(self):
        '''Save the model'''

        '''Receive the model'''
        model = self.model

        '''Write the model in the same directory of this code'''
        model.write("model.lp")
        model.write("model.sol")

    def test_model(self):
        '''Test if the model is only loaded or the already try to find a solution'''

        '''Receive the model'''
        m = self.model

        if type(m) != type(gp.Model()):
            return False, 1

        '''If the model is only loaded, there are any solutions yet'''
        if m.Status == 1:
            return False, 2

        else:
            #todo test with other codes like unbounded cases
            return True, 0

    def main(self):

        test_result = self.test_model()[0]
        test_code = self.test_model()[1]


        if test_result == True:
            '''Print the results'''
            self.print_results()

            '''Extract the variables'''
            df = self.extract_variables()

            '''Save the values of the variables on a .csv file'''
            self.save_variables(df)
            print('Variables saved with sucess as Variables.csv')
            print('=========================================')

            '''Create the files model.lp and model.sol'''
            self.save_model()
            print('model.lp and model.sol saved with sucess')
            print('=========================================')

            '''Create a file with all the model results in a .csv file'''
            self.save_model_results()
            print('Model results saved with sucess as results.csv')
            print('=========================================')


        elif test_result == False and test_code == 1:
            print('=========================================')
            print('Wrong use of Gurobyhelper!')
            print('You should send a Gurobi model in the first parameter')
            print('===================Example_of_Usage======================')
            print('model = gp.Model()')
            print('model.optimize()')
            print('Gurobi_helper_eng.gurobi_helper(model, True).main()')
            exit()

        elif test_result == False and test_code == 2:
            print('=========================================')
            print('Wrong use of Gurobyhelper!')
            print('You should call the Gurobyhelper after the line "model.optimize()" like the example bellow')
            print('===================Example_of_Usage======================')
            print('model.optimize()')
            print('Gurobi_helper_eng.gurobi_helper(model, True).main()')
            exit()