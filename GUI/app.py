import pandas as pd
import numpy as np
import pulp
from pulp import LpProblem, LpMaximize, lpSum, LpVariable, value, makeDict, LpInteger
from flask import Flask, render_template, request

def max_sol(final_demand, supply_name_list_true, final_supply, cost_excel):
    """
        Solves the material supply problem using the transportation algorithm.

        Args:
            final_demand (dict): A dictionary containing the demand for each project.
            supply_name_list_true (list): A list of supply node names.
            final_supply (dict): A dictionary containing the supply for each supply node.
            cost_excel (np.array): A numpy array containing the costs of each transportation path.

        Returns:
            A dictionary containing the optimized value of the variables and the optimized objective function value.
    """

    # Creates a list of all the supply nodes
    warehouses = supply_name_list_true

    # Creates a dictionary for the number of units of supply for each supply node
    supply = final_supply

    # Creates a list of all demand nodes
    projects = supply_name_list_true

    # Creates a dictionary for the number of units of demand for each demand node
    demand = final_demand

    # Creates a list of costs of each transportation path
    costs = cost_excel

    # The cost data is made into a dictionary
    costs = pulp.makeDict([warehouses, projects], costs, 0)
    # Creates the 'prob' variable to contain the problem data
    prob = LpProblem("Material Supply Problem", LpMaximize)
    # Creates a list of tuples containing all the possible routes for transport
    Routes = [(w, b) for w in warehouses for b in projects]

    # A dictionary called 'Vars' is created to contain the referenced variables(the routes)
    vars = LpVariable.dicts("Route", (warehouses, projects), 0, None, LpInteger)

    # The minimum objective function is added to 'prob' first
    prob += (
        lpSum([vars[w][b] * costs[w][b] for (w, b) in Routes]),
        "Sum_of_Transporting_Costs",
    )

    # The supply maximum constraints are added to prob for each supply node (warehouses)
    for w in warehouses:
        prob += (
            lpSum([vars[w][b] for b in projects]) <= supply[w],
            "Sum_of_Products_out_of_warehouses_%s" % w,
        )

    # The demand minimum constraints are added to prob for each demand node (project)
    for b in projects:
        prob += (
            lpSum([vars[w][b] for w in warehouses]) >= demand[b],
            "Sum_of_Products_into_projects%s" % b,
        )
    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # Return the variables optimized value
    results = {}
    for v in prob.variables():
        results[v.name] = v.varValue
    # The optimised objective function value is returned
    results["Value of Objective Function"] = value(prob.objective)
    return results
app = Flask(__name__)

@app.route('/')
def index():
    """
        Renders the index.html template.
    """
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_results():
    """
    Accepts user input from HTML form and returns the results of the optimization problem.

    Returns:
    --------
    render_template : HTML page
        An HTML page containing the results of the optimization problem.

    Raises:
    ------
    None

    """
    # Read input excel files using pandas
    df = pd.read_excel(request.files['demand'])
    costs = pd.read_excel(request.files['costs'], header=None)

    # Extract necessary data from input excel files
    supply_name_list_temp = np.array(df['Pick up location'])
    supply_name_list_true = [i for i in supply_name_list_temp if type(i) != str]
    Demand = df['Demand']
    Demand = np.array(Demand.dropna())
    final_supply = dict(zip(supply_name_list_true, Demand))
    final_demand = dict(zip(supply_name_list_true, Demand))

    cost_excel = np.array(costs)

    # Call max_sol() function to solve the optimization problem
    results = max_sol(final_demand, supply_name_list_true, final_supply, cost_excel)

    # Return the HTML page containing the results
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
