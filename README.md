# Leave is now automated

This is a basic Python script that automates the process of applying for leave using Selenium.

## Setup Instructions (for Linux)

### Step 1: Install Firefox GeckoDriver
- Download GeckoDriver from [here](https://github.com/mozilla/geckodriver/releases).
- Choose the appropriate version, preferably `geckodriver-v0.34.0-linux64.tar.gz`.

### Step 2: Extract GeckoDriver
1. Open a terminal and navigate to the directory containing the downloaded `.tar.gz` file.
2. Use the following command to extract the file:
    ```bash
    tar xvfz geckodriver-v0.34.0-linux64.tar.gz
    ```

### Step 3: Move GeckoDriver to $PATH
1. After extraction, you'll find a folder called `geckodriver`.
2. Move that folder to your `$PATH` using the following command:
    ```bash
    mv geckodriver /usr/local/bin
    ```

### Step 4: Ready to Use
Now you're all set to use the script! 

Run the script using (make sure you have Python 3 installed on your system!):

```bash
python3 leave_applier.py
```

## Usage
- Ensure you have Python installed.
- Install Selenium using `pip install selenium`.
- Run the provided Python script to automate the leave application process.

## Note
This setup is specifically for Linux. 
