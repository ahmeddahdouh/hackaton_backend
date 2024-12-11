
# Project Setup

## 1. Create and Activate a Virtual Environment
Create a virtual environment to isolate your project dependencies:

```bash
python -m venv .venv
```

Then, activate the virtual environment:

- On Windows:
  ```bash
  .\.venv\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

Once activated, your command prompt should show `(.venv)` before the directory name.

## 2. Install Project Dependencies

```bash
pip install -r requirements.txt
```


## 3. Create a `.env` File
Create a `.env` file in the root directory with the following content:

```
DB_USER=<your_db_user>
DB_PASSWORD=<your_db_password>
DB_HOST=<your_db_host>
DB_PORT=<your_db_port>
DB_NAME=<your_db_name>
SECRET_KEY="openssl rand -base64 32"
```

Replace the placeholder values with your actual database information. You can generate the `SECRET_KEY` using the command:

```bash
openssl rand -base64 32
```

## 5. Run Migrations
To apply the database migrations, run the following Alembic command:

```bash
alembic upgrade head
```

This will apply all the database migrations up to the latest revision.

## 6. Run application

```bash
uvicorn main:app --reload --port=your_port_number
```

---

You're all set! You can now run the application.
