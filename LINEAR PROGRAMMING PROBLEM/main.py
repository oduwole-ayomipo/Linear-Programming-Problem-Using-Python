# CODE BY ODUWOLE AYOMIPO COPYRIGHT 2022
from pulp import *

# Elementary Features:
lp = LpProblem("Space_Management", LpMinimize)

# Define Variables
x11 = LpVariable(name="x11", lowBound=0)
x21 = LpVariable(name="x21", lowBound=0)
x31 = LpVariable(name="x31", lowBound=0)
x41 = LpVariable(name="x41", lowBound=0)
x51 = LpVariable(name="x51", lowBound=0)
x12 = LpVariable(name="x12", lowBound=0)
x22 = LpVariable(name="x22", lowBound=0)
x32 = LpVariable(name="x32", lowBound=0)
x42 = LpVariable(name="x42", lowBound=0)
x13 = LpVariable(name="x13", lowBound=0)
x23 = LpVariable(name="x23", lowBound=0)
x33 = LpVariable(name="x33", lowBound=0)
x14 = LpVariable(name="x14", lowBound=0)
x24 = LpVariable(name="x24", lowBound=0)
x15 = LpVariable(name="x15", lowBound=0)

# Defining the objective function:
lp += ((65*(x11 + x21 + x31 + x41 + x51)) + (100*(x12 + x22 + x32 + x42)) + (135 * (x13 + x23 + x33)) + (160 * (x14 + x24)) + (190 * x15))

# Defining the constraints:
lp += (x11 + x12 + x13 + x14 + x15) >= 30000
lp += (x12 + x13 + x14 + x15 + x21 + x22 + x23 + x24) >= 20000
lp += (x13 + x14 + x15 + x22 + x23 + x24 + x31 + x32 + x33) >= 40000
lp += (x14 + x15 + x23 + x24 + x32 + x33 + x41 + x42) >= 10000
lp += (x15 + x24 + x33 + x42 + x51) >= 50000

# Solving the Linear Programming Problem:
print("CODE BY ODUWOLE AYOMIPO COPYRIGHT 2022")
status = lp.solve(PULP_CBC_CMD(msg=0))
print("Status: ", status)   # 1 = Optimal, 2 = Not Solved, 3 = Infeasible, 4 = Unbounded, 5 = Undefined

# Displaying the solution of the Linear Programming Problem
for var in lp.variables():
    print(var, "=", value(var))
print("OPTIMAL SOLUTION = ", value(lp.objective))

