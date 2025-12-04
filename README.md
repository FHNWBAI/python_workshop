# Python Workshop - FastAPI Project

## Overview

This is a simple FastAPI application created for a Python workshop. The goal is to learn about Git, GitHub, Docker, Dev Containers, FastAPI, and CI/CD by working together on a shared project.

Each student will add their own endpoint under `/students/{your_name}` and see it live when their Pull Request is merged!

## Getting Started (Local)

1. Clone this repository:
   ```bash
   git clone git@github.com:FHNWBAI/python_workshop.git
   cd python_workshop
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

6. Open your browser and visit:
   ```
   http://127.0.0.1:8000
   ```

You should see a welcome message and information about adding your own endpoint.

## Adding Your Own Endpoint

Follow these steps to add your own endpoint:

1. **Create a new branch:**
   ```bash
   git checkout -b add-student-{your-name}
   ```

2. **Edit `app/students.py`:**
   - Open the file and read the instructions at the top
   - Copy the example endpoint
   - Change `/example` to your own path (e.g., `/alice`)
   - Change the function name
   - Update the returned JSON with your name

3. **(Optional) Add a test:**
   - Copy the test in `tests/test_example_student.py`
   - Create a new test file or add to an existing one
   - Update the path and expected values

4. **Test locally:**
   ```bash
   pytest
   ```

5. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add student endpoint for {your-name}"
   git push origin add-student-{your-name}
   ```

6. **Open a Pull Request:**
   - Go to GitHub and create a Pull Request from your branch to `main`
   - Wait for CI tests to pass
   - Once approved and merged, your endpoint will be live!

7. **Visit your endpoint:**
   - [http://157.230.28.78:8082/](http://157.230.28.78:8082/)

## Using the Dev Container

If you're using VS Code, you can work inside a Docker container:

1. **Open in Dev Container:**
   - Install the "Dev Containers" extension in VS Code
   - Press `F1` or `Cmd+Shift+P` (Mac) / `Ctrl+Shift+P` (Windows/Linux)
   - Select "Dev Containers: Reopen in Container"
   - Wait for the container to build and start

2. **Run the app:**
   - Once the container is ready, go to the Run and Debug panel
   - Select "FastAPI (devcontainer)" from the dropdown
   - Press F5 or click the play button
   - Visit `http://127.0.0.1:8000`

The Dev Container uses the same Dockerfile as production, so you're working in the same environment that will be deployed.

## CI / Deployment

This project uses GitHub Actions for continuous integration and deployment:

- **Tests:** Every time you push code or open a Pull Request, the CI automatically runs all tests using `pytest`. If tests fail, the PR cannot be merged.

- **Deployment:** When changes are merged into the `main` branch, the CI:
  1. Builds a Docker image from the `Dockerfile`
  2. Pushes the image to GitHub Container Registry (GHCR)
  3. In a real project, this would deploy the image to a server

You can see the CI status on the "Actions" tab in GitHub.

## Project Structure

```
python_workshop/
├── app/
│   ├── __init__.py
│   ├── main.py          # Main FastAPI app and root endpoint
│   └── students.py      # Student endpoints (add yours here!)
├── tests/
│   ├── __init__.py
│   ├── test_root.py     # Tests for the root endpoint
│   └── test_example_student.py  # Example test for student endpoints
├── .devcontainer/
│   └── devcontainer.json  # VS Code Dev Container configuration
├── .vscode/
│   └── launch.json       # VS Code debug configurations
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI/CD pipeline
├── Dockerfile            # Docker configuration for the app
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Need Help?

- Check the comments in `app/students.py` for detailed instructions
- Look at the example endpoint and test for reference
- Ask your instructor or classmates!

Happy coding! 🚀

