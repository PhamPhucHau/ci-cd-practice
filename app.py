cat > app.py << 'EOF'
def get_hello_message(version=1):
    return f"Hello World version {version}"

def add(a, b):
    return a + b

# --- TESTS ---
def test_hello():
    # Test our new versioned Hello World function
    assert get_hello_message(2) == "Hello World version 1"

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0

if __name__ == "__main__":
    test_hello()
    test_add()
    print(f"{get_hello_message(2)} - All tests passed!")
EOF