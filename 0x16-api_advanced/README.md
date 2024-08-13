# 0x16. API Advanced

## Overview

This project involves working with the Reddit API to accomplish various tasks related to querying and processing data. It aims to practice and enhance skills in API interactions, including handling pagination, parsing JSON results, and using recursive functions in Python.

## Tasks

### 0. How Many Subs?

**Function**: `number_of_subscribers(subreddit)`

- **Description**: Queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, it returns 0.
- **Usage**: `python3 0-main.py <subreddit>`

### 1. Top Ten

**Function**: `top_ten(subreddit)`

- **Description**: Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. If the subreddit is invalid, it prints `None`.
- **Usage**: `python3 1-main.py <subreddit>`

### 2. Recurse It!

**Function**: `recurse(subreddit, hot_list=[])`

- **Description**: Recursively queries the Reddit API and returns a list of all hot articles' titles for a given subreddit. If no results are found or the subreddit is invalid, it returns `None`.
- **Usage**: `python3 2-main.py <subreddit>`

### 3. Count It!

**Function**: `count_words(subreddit, word_list)`

- **Description**: Recursively queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords. The count is case-insensitive and sorted by frequency and alphabetically.
- **Usage**: `python3 100-main.py <subreddit> '<keywords>'`

## Requirements

- **Python Version**: 3.4.3
- **Libraries**: Requests
- **Editors**: vi, vim, emacs

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/<your-username>/alx-system_engineering-devops.git
    ```

2. Navigate to the project directory:

    ```bash
    cd alx-system_engineering-devops/0x16-api_advanced
    ```

3. Ensure all Python files are executable:

    ```bash
    chmod +x *.py
    ```

4. Run the desired script with Python 3:

    ```bash
    python3 <script-name>.py
    ```

## Author

Emmanuel Odenyire Anyira  
Student at ALX Africa, taking the ALX Software Engineering Program  
Email: [eodenyire@gmail.com](mailto:eodenyire@gmail.com)  
LinkedIn: [Emmanuel Odenyire](https://www.linkedin.com/in/emmanuelodenyire/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For any collaborations or questions, please feel free to contact me via email or LinkedIn.

