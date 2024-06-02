# Slowloris Attack Tool

This tool performs a Slowloris attack on a specified web server. Slowloris is a type of Denial of Service (DoS) attack that aims to keep many connections to the target web server open and hold them open as long as possible. It does this by sending partial HTTP requests, none of which are completed, thereby overwhelming the server and causing it to deny service to legitimate users.

**Note:** This tool is for educational purposes only. Use it responsibly and only in a controlled, ethical environment with explicit permission.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/M0M3NTUM44/slowris.git
    ```

2. Navigate to the project directory:
    ```bash
    cd slowlris
    ```

## Usage

```bash
python3 slowloris.py <website> <port>
