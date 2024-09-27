# YanTheCoachPRO

## Requirements

- Python 3.x installed on your machine
- Pip (Python package manager)
- PyInstaller (for converting the script to an executable)

## Installation

### 1. Download the Script

To download the script, use the following command in your terminal or command prompt:

```bash
curl -O https://raw.githubusercontent.com/simplyYan/YanTheCoachPRO/refs/heads/main/main.py
```

Alternatively, you can download the file manually from the GitHub repository.

### 2. Install Python (if not already installed)

Ensure you have Python installed on your system. You can check by running:

```bash
python --version
```

If Python is not installed, download it from the [official website](https://www.python.org/downloads/).

### 3. Install PyInstaller

Install PyInstaller via pip:

```bash
pip install pyinstaller
```

## Creating Executable

### Windows

1. Open the Command Prompt or PowerShell.
2. Navigate to the directory where `main.py` is located.
3. Run the following command to create the executable:

    ```bash
    pyinstaller --onefile main.py
    ```

4. After the build process completes, you will find the executable in the `dist` folder.

### Linux

1. Open your terminal.
2. Navigate to the directory where `main.py` is located.
3. Run the following command:

    ```bash
    pyinstaller --onefile main.py
    ```

4. The executable will be created in the `dist` directory. Ensure it has execution permissions:

    ```bash
    chmod +x dist/main
    ```

5. You can now run the executable:

    ```bash
    ./dist/main
    ```

### macOS

1. Open your terminal.
2. Navigate to the directory where `main.py` is located.
3. Run the following command:

    ```bash
    pyinstaller --onefile main.py
    ```

4. The executable will be located in the `dist` directory. If you encounter any permission issues, grant the executable the appropriate permissions:

    ```bash
    chmod +x dist/main
    ```

5. You can now run the executable:

    ```bash
    ./dist/main
    ```

## Usage

Once you've created the executable, you can run it directly from the terminal (on Linux/macOS) or by double-clicking (on Windows). For Linux/macOS, ensure the executable has the proper execution permissions.
