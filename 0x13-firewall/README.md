# 0x13. Firewall

## Overview

This repository contains solutions for the `0x13. Firewall` project of the ALX Systems Engineering DevOps curriculum. The project involves setting up and configuring a firewall on a web server to enhance its security by controlling incoming and outgoing traffic.

## Table of Contents

- [Background Context](#background-context)
- [Resources](#resources)
- [Tasks](#tasks)
  - [0. Block all incoming traffic but](#0-block-all-incoming-traffic-but)
  - [1. Port forwarding](#1-port-forwarding)
- [Credits](#credits)
- [Contact](#contact)

## Background Context

The tasks in this project aim to provide hands-on experience with setting up and managing a firewall using `ufw` (Uncomplicated Firewall) on a web server. Proper firewall configuration is critical in protecting servers from unauthorized access and potential attacks.

## Resources

Read or watch:
- [What is a firewall](https://www.cloudflare.com/learning/security/glossary/what-is-a-firewall/)

## Tasks

### 0. Block all incoming traffic but

**Objective:** Configure the `ufw` firewall to block all incoming traffic except for the following TCP ports:
- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS)

**Commands:**

```bash
sudo apt-get update
sudo apt-get install ufw -y
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
sudo ufw status

File: 0-block_all_incoming_traffic_but

1. Port forwarding
Objective: Configure the firewall to redirect port 8080/TCP to port 80/TCP.

Steps:

Edit the ufw before rules configuration file:

bash
sudo vi /etc/ufw/before.rules
Add the following lines before the *filter line:

bash
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
Restart ufw to apply the changes:

bash
sudo ufw disable
sudo ufw enable
File: 100-port_forwarding

Credits
This repository is maintained by Emmanuel Odenyire Anyira, a student at ALX Africa, taking the ALX Software Engineering Program. Emmanuel is currently a Senior Data Analytics Engineer at Safaricom PLC and has extensive experience working with various organizations in technical support and ICT roles.

Contact
For collaborations or inquiries, please contact Emmanuel Odenyire Anyira via:

Email: eodenyire@gmail.com
LinkedIn: Emmanuel Odenyire
Emmanuel Odenyire Anyira is currently pursuing a Masters of Science in Data Science at the Cooperative University of Kenya. He holds a Bachelor of Science degree in Informatics from Moi University.
