from pydantic import BaseModel, EmailStr

class TokenCreate(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    token: str