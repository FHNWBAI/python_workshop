from fastapi import FastAPI
from app.students import router as students_router

app = FastAPI(title="Python Workshop API")

# Include the students router under /students prefix
app.include_router(students_router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Python Workshop API!",
        "info": "Add your own endpoint under /students/{your_name} and see it when your PR is merged.",
        "example": "/students/example"
    }

