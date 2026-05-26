# Step 1: Grab a pre-built shipping container that already has the Nginx web server installed
FROM nginx:alpine

# Step 2: Copy your football tracker into the exact folder Nginx uses to serve web pages
COPY football_tracker.html /usr/share/nginx/html/index.html

# Step 3: Tell the container to open network port 80 (the standard web port)
EXPOSE 80
