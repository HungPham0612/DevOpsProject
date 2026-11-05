from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/hello")            # <- the PATH is "/hello"
def say_hello():
    return {"greeting": "hi"} # <- the RETURN VALUE