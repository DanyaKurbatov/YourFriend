from fastapi import FastAPI
from users.views import users_router

app = FastAPI()

app.include_router(users_router)

# uvicorn.run(
#     'main:app',
#     host=settings.server_host,
#     port=settings.server_port,
#     reload=True
# )
