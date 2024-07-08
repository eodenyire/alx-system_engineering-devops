# Load Balancer Project

## Introduction

This repository contains solutions to the Load Balancer project as part of the ALX Software Engineering Program. This project focuses on configuring a load balancer using HAProxy to distribute traffic between two web servers, ensuring redundancy and improved reliability.

## Project Tasks

### Task 0: Double the Number of Webservers
- Configure `web-02` to be identical to `web-01`.
- Add a custom Nginx response header `X-Served-By` to both servers to track which web server is answering HTTP requests.
- Bash script: `0-custom_http_response_header`

### Task 1: Install Your Load Balancer
- Install and configure HAProxy on `lb-01` server.
- Configure HAProxy to distribute requests using a roundrobin algorithm.
- Bash script: `1-install_load_balancer`

### Task 2: Add a Custom HTTP Header with Puppet
- Automate the task of creating a custom HTTP header response using Puppet.
- Puppet manifest: `2-puppet_custom_http_response_header.pp`

## Getting Started

### Prerequisites
- Ubuntu 16.04 LTS
- Basic knowledge of Bash scripting, Nginx, HAProxy, and Puppet.

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/alx-system_engineering-devops.git
    cd alx-system_engineering-devops/0x0F-load_balancer
    ```

2. Run the scripts on the appropriate servers:
    - On `web-01` and `web-02`:
        ```bash
        ./0-custom_http_response_header
        ```
    - On `lb-01`:
        ```bash
        ./1-install_load_balancer
        ```

3. Apply the Puppet manifest:
    - On `web-01` and `web-02`:
        ```bash
        puppet apply 2-puppet_custom_http_response_header.pp
        ```

## Author

**Emmanuel Odenyire Anyira**

- **Email:** eodenyire@gmail.com
- **LinkedIn:** [Emmanuel Odenyire](https://www.linkedin.com/in/emmanuelodenyire/)

Emmanuel Odenyire Anyira is a student at ALX Africa, taking the ALX Software Engineering Program. He is also a Senior Data Analytics Engineer - BI at Safaricom PLC and a Graduate Student at The Cooperative University of Kenya, pursuing a Masters of Science in Data Science.

For collaborations, please contact Emmanuel via email or LinkedIn.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

