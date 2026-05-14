from auth import hash_password, verify_password, create_access_token, decode_token

# Test 1 — password hashing works
def test_hash_password():
    hashed = hash_password("mypassword")
    assert hashed != "mypassword"  # should not be plain text
    print("✅ test_hash_password passed")

# Test 2 — correct password verifies successfully
def test_verify_correct_password():
    hashed = hash_password("mypassword")
    assert verify_password("mypassword", hashed) == True
    print("✅ test_verify_correct_password passed")

# Test 3 — wrong password fails verification
def test_verify_wrong_password():
    hashed = hash_password("mypassword")
    assert verify_password("wrongpassword", hashed) == False
    print("✅ test_verify_wrong_password passed")

# Test 4 — token is created successfully
def test_create_token():
    token = create_access_token({"sub": "aditi", "role": "admin"})
    assert token is not None
    print("✅ test_create_token passed")

# Test 5 — token decodes correctly
def test_decode_valid_token():
    token = create_access_token({"sub": "aditi", "role": "admin"})
    payload = decode_token(token)
    assert payload["sub"] == "aditi"
    assert payload["role"] == "admin"
    print("✅ test_decode_valid_token passed")

# Test 6 — fake token fails decoding
def test_decode_invalid_token():
    payload = decode_token("thisisafaketoken")
    assert payload is None
    print("✅ test_decode_invalid_token passed")