import sqlite3
import random
import hashlib

def insecure_sql_query(user_input):
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{user_input}';"
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def hardcoded_secret():
    # Retrieve secret key from environment variable
    secret_key = os.environ.get('SECRET_KEY')
    if secret_key:
        print("Secret key retrieved successfully")
    else:
        print("Secret key not found in environment variables")

def weak_random_number():
    # Use of insecure random number generator
    rand_num = random.randint(0, 100)
    print(f"Insecure random number: {rand_num}")
    return rand_num

def md5_hashing(data):
    # Use of weak hashing algorithm (MD5)
    return hashlib.md5(data.encode()).hexdigest()

if __name__ == "__main__":
    user_input = input("Enter your username: ")
    insecure_sql_query(user_input)
    hardcoded_secret()
    weak_random_number()
    print(md5_hashing("sensitive_data"))