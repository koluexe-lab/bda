import redis

# Connect to the REAL Redis server running on your laptop
# Added protocol=2 to fix the 'unknown command HELLO' error for Windows Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True, protocol=2)

def record_failed_login(username):
    key = f"login_attempts:{username}"
    current_count = r.incr(key)  # Adds 1 to the counter
    return current_count

def reset_login_attempts(username):
    key = f"login_attempts:{username}"
    r.delete(key)  # Completely erases the counter

def get_failed_attempts(username):
    key = f"login_attempts:{username}"
    value = r.get(key)
    if value is None:
        return 0
    return int(value)

if __name__ == "__main__":
    my_user = "student_bro"
    
    print("=== STARTING THE REAL REDIS PRACTICAL ===")
    print(f"1. Initial failed attempts for {my_user}: {get_failed_attempts(my_user)}")
    
    print("\n[Action] Simulating 3 wrong password attempts...")
    print(f"   -> Attempt 1 failed! Current Counter: {record_failed_login(my_user)}")
    print(f"   -> Attempt 2 failed! Current Counter: {record_failed_login(my_user)}")
    print(f"   -> Attempt 3 failed! Current Counter: {record_failed_login(my_user)}")
    
    print(f"\n2. Verified count stored in Redis: {get_failed_attempts(my_user)} failed tries.")
    
    print(f"\n[Action] Success! User logged in. Resetting counter...")
    reset_login_attempts(my_user)
    
    print(f"3. Final count in Redis after success: {get_failed_attempts(my_user)}")
    print("=========================================")
