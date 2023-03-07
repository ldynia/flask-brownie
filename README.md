# Installation

1. Operating System Libs

    ```bash
    sudo apt install python3-venv
    ```
1. Virtual environment

    ```bash
    python3 -m venv venv

    # deactive venv
    . venv/bin/activate

    pip install --upgrade pip --requirement app/requirements.txt
    ```

# Run Program

```bash
flask --app app/main.py run --debug --port 5000 --reload
```