"""
================================================================================
STUDENT INSTRUCTIONS: Adding Your Own Endpoint
================================================================================

To add your own endpoint to this API:

1. Copy the example endpoint below (the one with @router.get("/example"))

2. Change the path from "/example" to your own unique path, for example:
   - "/alice"
   - "/kutu"
   - "/john"
   - Use your first name or a nickname (keep it simple!)

3. Change the function name from "read_example_student" to something like:
   - "read_alice_student"
   - "read_kutu_student"
   - etc.

4. Change the returned JSON to include YOUR name instead of "Example Student"

5. Keep it simple! No extra dependencies needed, just a plain function that
   returns a dictionary.

6. (Optional) Add a test for your endpoint in tests/test_example_student.py
   - Copy the test_example_student function
   - Change the path to match your endpoint
   - Change the expected name to your name

Example:
    @router.get("/alice")
    def read_alice_student():
        return {"student": "Alice", "message": "Hello from Alice!"}

That's it! Once you're done:
- Run tests locally: pytest
- Commit your changes
- Push to your branch
- Open a Pull Request
- When it's merged, your endpoint will be live!

================================================================================
"""

from fastapi import APIRouter

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/example")
def read_example_student():
    return {
        "student": "Example Student",
        "message": "Replace this with your own endpoint!",
    }


#@router.get("/faruk")
#def read_faruk():
#    return {
#        "student": "Faruk",
#        "message": "Hello amigos - and, welcome on board!",
#    }

@router.get("/kutalmis")
def read_kutalmis():
    return {
        "student": "Kutalmis",
        "message": "This code will be deployed to the production server!",
    }


@router.get("/gokalp")
def read_gokalp():
    return {
        "student": "Gokalp",
        "message": "Welcome!",
    }