from fastapi import FastAPI

app = FastAPI()

@app.get("/students")

def say_hello(batch:int, course:str):
    return {"course": course,
            "batch":batch,
            "message": f"showing {course} students batch {batch}"
            }