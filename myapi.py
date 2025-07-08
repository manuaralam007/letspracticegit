from fastapi import FastAPI

app = FastAPI()

students = {
    1:  {
        "name": "manu",
        "age": 27,
        "qualification": "Masters"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student-id}")
def get_student(student_id: int):
    return students[student_id]