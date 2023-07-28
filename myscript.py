import jwt

# Define a secret key (should be kept secret and securely stored)
secret_key = "mysecretkey"

# Define payload with claims
payload = {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
}

# Generate JWT
jwt_token = jwt.encode(payload, secret_key, algorithm="HS256")

# Print the generated JWT
print("Generated JWT:", jwt_token)

# Verify JWT
try:
    decoded_token = jwt.decode(jwt_token, secret_key, algorithms=["HS256"])
    print("Decoded JWT:", decoded_token)
except jwt.InvalidTokenError:
    print("Invalid JWT")