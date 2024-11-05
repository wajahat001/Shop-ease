# Define the services
user_service = "User Services"
other_services = [
    "Product Service",
    "Order Service",
    "Payment Service",
    "Notification Service",
    "Inventory Service"
]

# Print the User Services heading
print(user_service)
print("=" * len(user_service))  # Create a line under the heading

# Print other services
for service in other_services:
    print(service)
