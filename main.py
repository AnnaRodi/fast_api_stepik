# https://stepik.org/lesson/1044666/step/3?unit=1053240
# Быстрый старт в FastAPI Python
import uvicorn
from fastapi import FastAPI
from models import User

user = User(name='John Doe', id=1)
app = FastAPI()

@app.get("/users", response_model=User)
def user_root():
    return user

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True, workers=3)
