#def is telling python to prepare for a function, which is hello here. Name is the parameter
def hello(name):
#print is giving output, which is hello in this case. the plus is taking hello and placeholder or parameter, name, and putting them together. Concatenate
    print("Hello " + name)
#calling function hello and giving the argument, which is bubbles, which is something that resides within paranthesis and quotes.
hello ("Bubbles")
hello ("Alex")
hello (" ")
#hard coding
print("Hello Bubbles")

#the function name compute can be switched with any word as long as proceeding def and stays consistent throughout, number is the parmeter here. 
def compute(number):
#return is quiet print, supressing the output of the parameter being calculated..which can be added, subtracted, etc
    return number ** 2
#putting argument, 70, inside the penguin box, compute is the function name, variable penguins which is before an equals which is assignment
penguins = compute(70)
#print is giving output of variable penguins which contains the function name and argument
print(penguins)