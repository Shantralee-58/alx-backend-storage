# Use the official Ubuntu 18.04 image
FROM ubuntu:18.04

# Install Python 3.7 and other dependencies
RUN apt-get update && apt-get install -y python3.7 python3-pip mysql-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Start MySQL
CMD service mysql start && sleep infinity
