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
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8080, reload=True)
# localhost ip : 0.0.0.0

@app.get("/")
def helloWorld():
    return "Hello World 112"

@app.put("/updateTodo")
def updateTodo():
    print("Update todo called")
    return "updateTodo called"

@app.get("/user")
def helloWorld1():
    return False

@app.get("/list")
def list():
    return [1,2,3]

@app.get("/dict")
def dictionary():
    return {"name": "alisha"}

# Dynamic Path
@app.get("/gettodos/{id}")
def dynamic_path(id):
    print("Dynamic Path called with ID:", id)
    return id


# Self calling function
def sumTwoNumbers(a, b):
    return a + b

sumTwoNumbers(10,20)


# Path Variable
@app.get("/gettodos/{userName}/{rollNo}")
def dynamic_path_name(userName, rollNo):
    print("Dynamic Path called with name and roll no:", userName,id)
    return userName+rollNo

# Type define
@app.get("/gettodos/{userName}/{rollNo}")
def dynamic_path_type(userName: str, rollNo: str):
    print("Dynamic Path called with name and roll no:", userName,id)
    return userName + rollNo


# Query Parameter
@app.get("/getQueryParameter")
def query_Parameter(userName:str, rollNo:str):
    print("Query Parameter called with name and roll no:", userName, rollNo)
    return "Query Parameter called with name and roll no"


students = [{
    "userName": "Alisha",
    "rollNo": 112
},
{
    "userName": "Zarmeen",
    "rollNo": 373
}]

# get students
@app.get("/getStudent")
def getStudent():
    return students

# add student
@app.get("/addStudent")
def addStudent(userName:str, rollNo:str):
    global students
    students.append({"userName": userName, "rollNo": rollNo})
    return students

# Get Single Student (Path Variable)
@app.get("/getSingleStudent/{rollNo}")
def getSingleStudent(rollNo: int):
    global students
    for student in students:
        if student["rollNo"] == rollNo:
            return student
    return {"message": "Student not found"}

# Search Student (Query Parameter)
@app.get("/searchStudent")
def searchStudent(rollNo: int):
    for student in students:
        if student["rollNo"] == rollNo:
            return student

    return {"message": "Student not found"}

# Update Student
@app.put("/updateStudent")
def updateStudent(rollNo: int, userName: str):
    global students
    for student in students:
        if student["rollNo"] == rollNo:
            student["userName"] = userName
            return {
                "message": "Student updated successfully",
                "student": student
            }
    return {"message": "Student not found"}


# Delete Student
@app.delete("/deleteStudent")
def deleteStudent(rollNo: int):
    global students

    for student in students:
        if student["rollNo"] == rollNo:
            students.remove(student)
            return {
                "message": "Student deleted successfully",
                "students": students
            }

    return {"message": "Student not found"}