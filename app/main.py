from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient
from app.students import router as students_router
from app._hidden.christmascookie import router as christmascookie_router

app = FastAPI(title="Python Workshop API")

app.include_router(students_router)
app.include_router(christmascookie_router)


@app.get("/", response_class=HTMLResponse)
def read_root():
    # Get all student endpoints and their data
    client = TestClient(app)
    students_data = []
    
    # Find all routes that start with /students/
    for route in app.routes:
        if hasattr(route, 'path') and route.path.startswith('/students/') and route.path != '/students':
            try:
                # Call the endpoint to get the data, explicitly requesting JSON
                response = client.get(route.path, headers={"Accept": "application/json"})
                if response.status_code == 200:
                    # Check if response is JSON (not HTML)
                    content_type = response.headers.get("content-type", "")
                    if "application/json" in content_type:
                        data = response.json()
                        # Extract student and message if they exist
                        students_data.append({
                            "student": data.get("student", "Unknown"),
                            "message": data.get("message", ""),
                            "endpoint": route.path
                        })
            except Exception:
                # Skip endpoints that fail
                continue
    
    # Generate HTML table rows
    table_rows = ""
    for student in students_data:
        student_name = student.get("student", "Unknown")
        message = student.get("message", "")
        endpoint = student.get("endpoint", "")
        # Escape HTML characters for safety
        student_name = student_name.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        message = message.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        endpoint = endpoint.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        table_rows += f"""
            <tr>
                <td>{student_name}</td>
                <td>{message}</td>
                <td style="text-align: center;"><a href="{endpoint}" style="color: #00ff00; text-decoration: none;">🔗</a></td>
            </tr>
        """
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Workshop API</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                font-family: 'Courier New', 'Monaco', 'Consolas', 'Lucida Console', monospace;
                background: #000000;
                min-height: 100vh;
                padding: 20px;
                color: #00ff00;
            }}
            .container {{
                max-width: 1000px;
                margin: 0 auto;
            }}
            .header {{
                padding: 20px 0;
                text-align: center;
                border-bottom: 1px solid #00ff00;
                margin-bottom: 20px;
            }}
            .header h1 {{
                font-size: 1.8em;
                font-weight: normal;
                color: #00ff00;
            }}
            .description {{
                font-size: 0.9em;
                line-height: 1.5;
                color: #00ff00;
                margin-bottom: 20px;
                text-align: center;
            }}
            .table-container {{
                overflow-x: auto;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                border: 1px solid #00ff00;
            }}
            thead {{
                border-bottom: 2px solid #00ff00;
            }}
            th {{
                padding: 10px 15px;
                text-align: left;
                font-weight: normal;
                font-size: 0.9em;
                color: #00ff00;
                text-transform: uppercase;
            }}
            td {{
                padding: 8px 15px;
                border-bottom: 1px solid #003300;
            }}
            tbody tr:hover {{
                background-color: #001100;
            }}
            tbody tr:last-child td {{
                border-bottom: none;
            }}
            a {{
                color: #00ff00;
                text-decoration: none;
                transition: opacity 0.2s;
            }}
            a:hover {{
                opacity: 0.7;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🐍 Python Workshop API</h1>
            </div>
            <div class="description">
                Collaborative FastAPI project. Students add endpoints at /students/{{name}}
            </div>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Student</th>
                            <th>Message</th>
                            <th style="text-align: center;">Link</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_rows if table_rows else '<tr><td colspan="3" style="text-align: center; padding: 20px; color: #00ff00;">No students found.</td></tr>'}
                    </tbody>
                </table>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HTMLResponse(content=html_content)

