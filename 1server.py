from xmlrpc.server import SimpleXMLRPCServer

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Create the XML-RPC server

server = SimpleXMLRPCServer(("localhost", 9000))  # Start on localhost, port 9000
server.register_function(factorial, "factorial")  # Register the function for remote access

print("Server is running on port 9000...")
server.serve_forever()  # Keep the server running
