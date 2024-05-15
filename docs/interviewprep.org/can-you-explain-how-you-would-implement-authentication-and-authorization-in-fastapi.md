FastAPI provides a security module to implement authentication and authorization. For authentication, OAuth2PasswordBearer is used which requires a URL that the client will use for token retrieval. The get_current_user function uses Depends to inject dependencies, where it decodes the token and fetches user data. If invalid, HTTPException is raised.

For authorization, FastAPI offers Security Scopes. Each route can have a list of scopes as dependencies. When a request comes in, FastAPI checks if the current user has required scopes. If not, an error is returned.

Here’s a code snippet:
```python
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    # decode token and fetch user data here
    raise HTTPException(status_code=403, detail="Not authenticated")

app = FastAPI()

@app.get("/items/", dependencies=[Depends(Security(get_current_user, scopes=["items:read"]))])
async def read_items():
    return [{"item": "Foo", "value": "Bar"}]
```
