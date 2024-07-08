#!/usr/bin/env bash
# This script installs and configures HAproxy on Ubuntu to load balance traffic between web-01 and web-02.

# Update package list and install HAproxy
sudo apt-get update
sudo apt-get install -y haproxy

# Configure HAproxy
cat <<EOL > /etc/haproxy/haproxy.cfg
frontend http_front
    bind *:80
    mode http
    default_backend http_back

backend http_back
    mode http
    balance roundrobin
    server web-01 54.237.58.68:80 check
    server web-02 52.207.70.223:80 check
EOL

# Enable HAproxy service to start on boot and start the service
sudo systemctl enable haproxy
sudo systemctl start haproxy

# Output success message
echo "HAproxy installed and configured successfully for load balancing."
