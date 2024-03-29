# Leave is now automated

This is a basic Python script that automates the process of applying for leave using Selenium.

## --> Setup Instructions (for Linux)

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
This setup is specifically for Linux. <br>
ALso please ensure that you have a stable internet connection.

----------------------------------------------------------------------------------------------

## --> Setup Instructions (for Windows)

### Step 1: Download GeckoDriver for Windows
- Download GeckoDriver for Windows from [here](https://github.com/mozilla/geckodriver/releases).
- Choose the appropriate version, preferably `geckodriver-v0.34.0-win32.zip`.

### Step 2: Extract GeckoDriver
1. Extract the downloaded `.zip` file.
2. You'll find `geckodriver.exe` inside the extracted folder.

### Step 3: Set Up GeckoDriver Path
1. Move `geckodriver.exe` to any directory of your choice.
2. Add the directory path to your system environment variables:
    - Go to Control Panel > System and Security > System.
    - Click on "Advanced system settings" on the left panel.
    - In the System Properties window, click on the "Environment Variables" button.
    - Under "System variables", find the "Path" variable and click "Edit".
    - Add the directory path containing `geckodriver.exe` to the list of paths.
  
## DONT FORGET TO READ THE SCRIPT (windows.py) FOR IMP INSTRUCTIONS!

### Step 4: Ready to Use
Now you're all set to use the script!

Run the script using (make sure you have Python installed on your system!):

```bash
python windows.py
```
## Usage
- Ensure you have Python installed.
- Install Selenium using `pip install selenium`.
- Run the provided Python script to automate the leave application process.


## Note
This setup is specifically for Windows. 
ALso please ensure that you have a stable internet connection.

## --> Setup fot the GUI version

<center><img src="gui.png" width="550" height="600"></center>


### Steps to follow for the GUI version:
1. Install tkinter and customtkinter libraries using the following command on the terminal
   ```bash
   pip3 install tk
   ```
   ```bash
   pip3 install customtkinter
   ```
2. Make sure you have followed the above steps for your system, and then simply run the 'leave_gui.py' file
    ```bash
    python3 leave_gui.py
    ```

### Again please make sure that you have a good internet connection
