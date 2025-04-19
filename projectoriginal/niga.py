import bcrypt

def migrate_passwords():
    try:
        with open("projectoriginal/data/passwords.txt", "r") as infile, \
             open("projectoriginal/data/passwords_hashed.txt", "w") as outfile:
            for line in infile:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue
                username, plain_password, role = parts
                hashed_password = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt()).decode()
                outfile.write(f"{username},{hashed_password},{role}\n")

        print("✅ Password migration complete. Check passwords_hashed.txt")
    except Exception as e:
        print(f"Migration error: {e}")

migrate_passwords()
