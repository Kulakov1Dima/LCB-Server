import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "hello"
if __name__ == "__main__":
     uvicorn.run("main:app", host="89.111.170.135", reload=True,
                ssl_keyfile=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ibook-daa2557bc9hb3.keenetic.pro-privateKey.key'),
                ssl_certfile=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ibook-daa2557bc9hb3.keenetic.pro.crt'))
    #uvicorn.run("main:app", host="localhost", port=80, reload=True)