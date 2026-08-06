from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/gettodos")
def getTodos():
    print("Get todos called")
    return "gettodos called"

# getTodos() -> function call 

@app.get("/getSingleTodo")
def getSingleTodo():
    print("Get single todo called")
    return "getSingleTodo called"


@app.post("/gettodos")
def getTodosPost():
    print("Get Post method todos called")
    return "post gettodos called reload check"


def start():
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8080, reload=True, log_level="info")
# localhost ip : 0.0.0.0

@app.get("/")
def helloWorld():
    return "Hello World 112"

@app.put("/updateTodo")
def updateTodo():
    print("Update todo called")
    return "updateTodo called"
