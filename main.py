import os

def main():
    # Read the secret token from the environment variable.
    # In GitHub Actions, secrets are securely injected into environment variables.
    secret_token = os.environ.get("MY_SECRET_TOKEN")
    
    if not secret_token:
        print("❌ Error: MY_SECRET_TOKEN environment variable is not set or is empty!")
        print("Please configure 'MY_SECRET_TOKEN' in your GitHub Repository Secrets.")
        return

    print("✅ Successfully loaded MY_SECRET_TOKEN from GitHub Secrets!")
    
    # We print the length of the secret to demonstrate we have received it, 
    # without exposing the actual sensitive content in the logs.
    print(f"Token length: {len(secret_token)} characters")
    
    # Showcase safe display (GitHub also automatically masks secrets in workflow logs if they are printed directly,
    # but it is best practice not to print them at all).
    if len(secret_token) > 4:
        print(f"Token preview: {secret_token[:2]}...{secret_token[-2:]}")
    else:
        print("Token is too short for a preview.")

if __name__ == "__main__":
    main()
