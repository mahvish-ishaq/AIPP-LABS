# TASK 3 - LINEAR OPTIMIZATION
# Brute-force Linear Optimization for Chocolate Problem

from pulp import LpMaximize, LpProblem, LpVariable

print("\n--- Task 3: Linear Optimization ---")
print("Solving maximization problem: Z = a*x + b*y")
a = float(input("Enter coefficient a for x: "))
b = float(input("Enter coefficient b for y: "))
c1 = float(input("Enter RHS for constraint 1 (2x + y <= ? ): "))
c2 = float(input("Enter RHS for constraint 2 (x + y <= ? ): "))
c3 = float(input("Enter RHS for constraint 3 (x <= ? ): "))

model = LpProblem("OptimizationCase", LpMaximize)

x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

model += a*x + b*y
model += 2*x + y <= c1
model += x + y <= c2
model += x <= c3

model.solve()

print("Optimal x:", x.value())
print("Optimal y:", y.value())
print("Maximum Value:", model.objective.value())