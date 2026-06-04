# GitHub Secrets Demo 🗝️

A bare minimum project demonstrating how to securely store sensitive tokens/keys in **GitHub Secrets** and access them within a **GitHub Actions** workflow.

---

## How It Works

1. **GitHub Secrets**: You define a secret key-value pair in your repository settings on GitHub.
2. **Workflow Environment**: In `.github/workflows/demo.yml`, we retrieve that secret using `${{ secrets.MY_SECRET_TOKEN }}` and assign it to an environment variable (`MY_SECRET_TOKEN`).
3. **Application Logic**: The Python script (`main.py`) reads the environment variable securely using `os.environ.get("MY_SECRET_TOKEN")` without ever storing or committing the actual secret in the codebase.

---

## Setup Instructions

To see this in action on your GitHub repository, follow these steps:

### 1. Push this Repository to GitHub
If you haven't already, push these files to a GitHub repository:
```bash
git init
git add .
git commit -m "Initialize secrets demo project"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Configure the Secret on GitHub
1. Go to your repository on GitHub.
2. Click on **Settings** (tab at the top).
3. In the left sidebar, expand **Secrets and variables** and click on **Actions**.
4. Click the green **New repository secret** button.
5. Enter the following details:
   - **Name**: `MY_SECRET_TOKEN`
   - **Secret**: *Enter any text/token here (e.g., `SuperSecret12345!`)*
6. Click **Add secret**.

### 3. Run the Workflow
1. Go to the **Actions** tab on your GitHub repository.
2. Under the list of workflows on the left, click **GitHub Secrets Demo**.
3. Click the **Run workflow** dropdown on the right.
4. Select the branch (e.g., `main`) and click the green **Run workflow** button.
5. Refresh the page after a few seconds, click on the running/completed run, and inspect the logs under **Run Demo Script** to verify that it successfully loaded the secret!

---

## File Structure

- [main.py](file:///C:/Users/naive/Desktop/secrets/main.py): The Python script that reads and validates the secret from the environment.
- [.github/workflows/demo.yml](file:///C:/Users/naive/Desktop/secrets/.github/workflows/demo.yml): The GitHub Actions workflow that executes the Python script and securely injects the secret.
