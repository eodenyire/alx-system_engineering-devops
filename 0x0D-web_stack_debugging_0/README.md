# 0x0D-web_stack_debugging_0

## Description
This project is part of the ALX Software Engineering Program and focuses on debugging a web stack. The objective is to ensure that Apache is running on a Docker container and that it returns a page containing "Hello Holberton" when querying the root.

## Tasks

### 0. Give me a page!
In this task, you need to get Apache to run on a Docker container and return a page containing "Hello Holberton" when queried. The solution involves debugging the web stack to fix any issues and ensure Apache serves the required page.

#### Example
```bash
vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
vagrant@vagrant:~$ docker ps
vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$
How to Use

Run the Docker container:
docker run -p 8080:80 -d -it holbertonschool/265-0

Check the status of the running container:
docker ps

Access the running container:
docker exec -ti <CONTAINER_ID> /bin/bash
Investigate and fix the issue:

Check if Apache is installed and running.
Start Apache if it is not running.
Create or edit the index.html file to contain "Hello Holberton".

Test the setup:
curl 0:8080

Create the Bash script:
#!/usr/bin/env bash
# This script fixes the Apache setup in the Docker container
apt-get update
apt-get install -y apache2
echo "Hello Holberton" > /var/www/html/index.html
service apache2 restart

Author
Emmanuel Odenyire Anyira - Senior Data Analytics Engineer at Safaricom PLC, student at ALX Africa taking the ALX Software Engineering Program. For collaborations, contact me through:

Email: eodenyire@gmail.com
LinkedIn: Emmanuel Odenyire
