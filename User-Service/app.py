from flask import Flask

app = Flask(__name__)

# Define the main heading and services
user_service = "User Services"
other_services = [
    "Product Service",
    "Order Service",
    "Payment Service",
    "Notification Service",
    "Inventory Service"
]

@app.route('/')
def hello_world():
    # Start with the main heading
    response = f"<h1>{user_service}</h1>"
    
    # Add a line under the heading
    response += "<hr>"
    
    # Loop through the services and display them
    for service in other_services:
        response += f"<p>{service}</p>"
    
    return response

if __name__ == "__main__":
    # Run Flask app and make it accessible on all IPs (0.0.0.0) at port 5000
    app.run(host='0.0.0.0', port=5000)
