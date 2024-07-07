# Attack is the Best Defense

## Description
This project is part of the ALX Software Engineering Program and focuses on advanced network security concepts, including ARP spoofing, network sniffing, and dictionary attacks. The project is 100% optional and aims to provide hands-on experience with these security techniques. Successfully completing any part of this project will add a project grade of over 100% to your average.

## Concepts Covered
- Network basics
- Docker
- Network sniffing
- ARP spoofing
- Dictionary attack

## Resources
- [Network sniffing](https://www.comparitech.com/net-admin/network-packet-sniffing/)
- [ARP spoofing](https://www.veracode.com/security/arp-spoofing)
- [Connect to SendGrid’s SMTP relay using telnet](https://sendgrid.com/docs/for-developers/sending-email/getting-started-smtp/)
- [What is Docker and why is it popular?](https://www.docker.com/resources/what-container)
- [Dictionary attack](https://www.imperva.com/learn/application-security/dictionary-attack/)
- man or help:
  - `tcpdump`
  - `hydra`
  - `telnet`
  - `docker`

## Tasks

### 0. ARP spoofing and sniffing unencrypted traffic
Security is a vast topic, and network security is an important part of it. In this task, we will start by sniffing unencrypted traffic and extracting information from it.

- Download and run the `user_authenticating_into_server` script locally on your Ubuntu machine.
- Use `tcpdump` to sniff the network and find the password used during authentication.

**File:** `0-sniffing`

### 1. Dictionary attack
Password-based authentication systems can be easily broken using a dictionary attack. In this task, you will use Docker and `hydra` to perform a dictionary attack on an SSH account.

- Install Docker on your Ubuntu machine.
- Pull and run the Docker image `sylvainkalache/264-1` with the command `docker run -p 2222:22 -d -ti sylvainkalache/264-1`.
- Find a password dictionary and use `hydra` to brute force the account `sylvain` via SSH on the Docker container.
- The password is 11 characters long.

**File:** `1-dictionary_attack`

## Author
**Emmanuel Odenyire Anyira**

- Senior Data Analytics Engineer - BI at Safaricom PLC
- Graduate Student at The Cooperative University of Kenya, pursuing a Masters of Science in Data Science
- Student at ALX Africa, taking the ALX Software Engineering Program

For collaborations, please contact me via email at eodenyire@gmail.com or through my LinkedIn profile: [Emmanuel Odenyire](https://www.linkedin.com/in/emmanuelodenyire/).

## Repository
[GitHub Repository: alx-system_engineering-devops](https://github.com/eodenyire/alx-system_engineering-devops)

Directory: `attack_is_the_best_defense`

Files:
- `0-sniffing`
- `1-dictionary_attack`
