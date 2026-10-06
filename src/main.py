from fastapi import FastAPI

from .orders.router import router  as orders
from .users.router  import router as users


app = FastAPI()

app.include_router(orders)
app.include_router(users)
sadfasdfsdf
sdfasdfasfasfd
