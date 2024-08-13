# ALX Software Engineering Program - Web Stack Debugging #3

## Project Overview

This project is part of the ALX Software Engineering Program's Systems Engineering DevOps curriculum. The focus of this project is on web stack debugging, specifically addressing issues with a WordPress site running on a LAMP stack (Linux, Apache, MySQL, PHP). 

## Tasks

### Task 0: Strace is Your Friend

- **Objective**: Using `strace`, identify why Apache is returning a 500 Internal Server Error. Once the issue is found, fix it and automate the solution using Puppet.
- **Details**: 
  - `strace` is used to trace system calls and signals.
  - The fix should be implemented using Puppet instead of Bash.
  - Puppet manifests should follow specific guidelines and be compatible with Puppet v3.4.
- **File**: `0-strace_is_your_friend.pp`

## Requirements

- The project should be executed on Ubuntu 14.04 LTS.
- All files should end with a new line.
- A `README.md` file is mandatory.
- Puppet manifests must:
  - Pass `puppet-lint` version 2.1.1 without errors.
  - Run without errors.
  - Begin with a comment explaining the manifest's purpose.
  - Have a `.pp` extension.

## Installation and Usage

1. **Install Puppet and Puppet Lint**:
    ```bash
    sudo apt-get install -y ruby
    sudo gem install puppet-lint -v 2.1.1
    ```

2. **Run the Puppet Manifest**:
    ```bash
    puppet apply 0-strace_is_your_friend.pp
    ```

3. **Verify the Fix**:
    ```bash
    curl -sI 127.0.0.1
    curl -s 127.0.0.1:80 | grep Holberton
    ```

## Contact

For collaborations or any inquiries, please contact:

- **Emmanuel Odenyire Anyira**
  - Email: [eodenyire@gmail.com](mailto:eodenyire@gmail.com)
  - LinkedIn: [Emmanuel Odenyire](https://www.linkedin.com/in/emmanuelodenyire/)

## Acknowledgements

This project is part of the ALX Software Engineering Program's curriculum. Special thanks to the ALX team and instructors for their guidance and support.

---

*Note: Ensure that all tasks and requirements are completed as per the guidelines provided. For any issues, refer to the official documentation or reach out for assistance.*

