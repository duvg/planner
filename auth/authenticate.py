from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from auth.jwt_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/signin")

async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
  if not token:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="Sign in for acces"
    )

  decoded_token = verify_access_token(token)
  print("dale", decoded_token)
  return decoded_token["user"]