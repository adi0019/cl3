import xmlrpc.client

# Connect to the server
server = xmlrpc.client.ServerProxy('http://localhost:9000')  # Connect to localhost, port 9000

# Get input from the user
number = int(input("Enter an integer to calculate its factorial: "))

# Call the factorial method on the server
result = server.factorial(number)

# Display the result
print(f"The factorial of {number} is {result}")
