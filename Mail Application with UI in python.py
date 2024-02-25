# Simple Mail Application

# Data storage for users and SMTP configurations
users = {}
smtp_configs = {}

# Function to register a new user
def register(username, password):
    if username not in users:
        users[username] = password
        return True
    return False

# Function to authenticate a user
def login(username, password):
    if username in users and users[username] == password:
        return True
    return False

# Function to configure SMTP settings
def configure_smtp(username, server, port, smtp_username, smtp_password):
    if username in users:
        smtp_configs[username] = {
            'server': server,
            'port': port,
            'smtp_username': smtp_username,
            'smtp_password': smtp_password
        }
        return True
    return False

# Function to send email
def send_email(username, recipient, subject, body):
    if username in smtp_configs:
        smtp_config = smtp_configs[username]
        print(f"Sending email from {username} to {recipient}:\nSubject: {subject}\nBody: {body}")
        return True
    return False

# Main function to demonstrate usage
def main():
    # Register a new user
    register("user1", "password123")

    # Authenticate the user
    if login("user1", "password123"):
        print("Login successful.")
    else:
        print("Login failed.")

    # Configure SMTP settings for the user
    configure_smtp("user1", "smtp.example.com", 587, "user@example.com", "smtp_password")

    # Send email
    if send_email("user1", "recipient@example.com", "Test Email", "This is a test email."):
        print("Email sent successfully.")
    else:
        print("Failed to send email.")

if __name__ == "__main__":
    main()
