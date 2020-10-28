from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

@app.get("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}
