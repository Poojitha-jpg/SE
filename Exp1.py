# Stage 3: Reading from a File

def quadratic_weather_model(a, b, c, x):
    # Calculate the value using the quadratic equation
    y = a * x**2 + b * x + c
    return y

# Read coefficients and input value from the file
with open('coeff.txt', 'r') as file:
    for line in file:
        # Split the line into values and convert them to float
        a, b, c, x = map(float, line.split())

        # Calculate the result using the quadratic model
        result = quadratic_weather_model(a, b, c, x)

        # Print the result
        print(f"For x={x}, the result is: {result}")


Output:-
For x=30.0, the result is: 166.0
For x=25.0, the result is: 201.5
For x=40.0, the result is: 329.8
