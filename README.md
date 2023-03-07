# Installation

1. Operating system libs

    ```bash
    sudo apt install python3-venv
    ```

1. Virtual environment

    ```bash
    python3 -m venv venv

    # deactive venv
    . venv/bin/activate

    pip install --upgrade pip --requirement requirements.txt
    ```

# Run

```bash
flask --app app/main.py run --debug --port 5000 --reload
```

# Inspect

[http://localhost:5000/](http://localhost:5000/)
