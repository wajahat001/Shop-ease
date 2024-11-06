# Use the official Nginx base image
FROM nginx:alpine

# Copy your HTML file to the default directory served by Nginx
COPY order-services.html /usr/share/nginx/html/order-services.html

# Expose port 80 for the web server
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]
