# session_manager.py

import time
import uuid


# Store sessions: session_id → (username, expiry_time)
sessions = {}


def create_session(username, ttl=10):
    session_id = str(uuid.uuid4())
    expiry = time.time() + ttl
    sessions[session_id] = (username, expiry)

    print(f"Session created for {username}")
    print("Session ID:", session_id)

    return session_id


def validate_session(session_id):
    if session_id not in sessions:
        return "Invalid session"

    username, expiry = sessions[session_id]

    if time.time() > expiry:
        del sessions[session_id]
        return "Session expired"

    return f"Session valid for user: {username}"


def cleanup_sessions():
    current_time = time.time()
    expired = []

    for sid, (_, expiry) in sessions.items():
        if current_time > expiry:
            expired.append(sid)

    for sid in expired:
        del sessions[sid]

    print(f"Cleaned up {len(expired)} expired sessions")


def simulate():
    sid = create_session("Ravi", ttl=5)

    for i in range(7):
        print(f"\nCheck {i+1}:")
        print(validate_session(sid))
        time.sleep(1)

    cleanup_sessions()


def main():
    simulate()


main()
