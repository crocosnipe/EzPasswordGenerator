# Import the required libraries
import fastapi
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import random
import string

def generate_password(length: int = 20, letters: bool = True, digits: bool = True, special: bool = True):
    if length > 20:     
        length = 20
    elif length < 6:
        length = 6
    
    characters = ""
    # Determine which characters to use
    if letters:
        characters += string.ascii_letters
    if digits:
        characters += string.digits
    if special:
        characters += "!+.?"
    if not (letters or digits or special):
        characters = string.ascii_letters + string.digits + "!+.?"

            
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    # If a word is provided, insert it into the password
    # Return the password
    return password

# Create an instance of the FastAPI class
app = fastapi.FastAPI()

# Add CORS (Cross-Origin Resource Sharing) middleware to the FastAPI app
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the password endpoint
@app.get("/password/")
async def get_password(length: int = 20, letters: bool = True, digits: bool = True, special: bool = True):
    # Return the generated password
    return {"password": generate_password(length, letters, digits, special)}

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000) # For running the server locally
    # uvicorn.run(app, host="0.0.0.0", port=8000) # For running the server publicly