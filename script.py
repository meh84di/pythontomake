import json

def main():
    # Simple Python example that returns a JSON response
    result = {"message": "Hello from Python script"}
    print(json.dumps(result))  # This will be printed in GitHub Actions logs

if __name__ == "__main__":
    main()
