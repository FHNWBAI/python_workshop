"""
Easter egg: Snake game for Faruk's endpoint
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

# Create a router for the easter egg endpoint
router = APIRouter(prefix="/students", tags=["students"])


def get_snake_game_html():
    """Returns HTML content for a playable snake game."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Faruk's Snake Game 🐍</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Courier New', monospace;
                background: #000000;
                color: #00ff00;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                padding: 20px;
            }
            .container {
                text-align: center;
            }
            h1 {
                margin-bottom: 10px;
                font-size: 1.5em;
            }
            .info {
                margin-bottom: 20px;
                font-size: 0.9em;
                color: #00ff00;
            }
            #gameCanvas {
                border: 2px solid #00ff00;
                background: #000000;
                display: block;
                margin: 0 auto;
            }
            .score {
                margin-top: 15px;
                font-size: 1.2em;
            }
            .controls {
                margin-top: 15px;
                font-size: 0.8em;
                color: #00aa00;
            }
            .start-hint {
                margin-top: 10px;
                font-size: 0.9em;
                color: #00ff00;
                font-style: italic;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐍 Snake Game - Easter Egg!</h1>
            <div class="info">Hello amigos - and, welcome on board!</div>
            <canvas id="gameCanvas" width="400" height="400"></canvas>
            <div class="score">Score: <span id="score">0</span></div>
            <div class="controls">Use Arrow Keys or WASD to play</div>
            <div class="start-hint" id="startHint">Press any arrow key or WASD to start!</div>
        </div>
        <script>
            const canvas = document.getElementById('gameCanvas');
            const ctx = canvas.getContext('2d');
            const scoreElement = document.getElementById('score');
            
            const gridSize = 20;
            const tileCount = canvas.width / gridSize;
            
            let snake = [
                {x: 10, y: 10}
            ];
            let velocity = {x: 0, y: 0};
            let food = {x: 15, y: 15};
            let score = 0;
            let gameRunning = true;
            const startHint = document.getElementById('startHint');
            
            function gameLoop() {
                if (!gameRunning) return;
                
                clearCanvas();
                drawFood();
                updateSnake();
                drawSnake();
                
                setTimeout(gameLoop, 100);
            }
            
            function clearCanvas() {
                ctx.fillStyle = '#000000';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
            }
            
            function drawSnake() {
                ctx.fillStyle = '#00ff00';
                for (let segment of snake) {
                    ctx.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize - 2, gridSize - 2);
                }
            }
            
            function drawFood() {
                ctx.fillStyle = '#ff0000';
                ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
            }
            
            function updateSnake() {
                // Don't update if velocity is zero (game hasn't started)
                if (velocity.x === 0 && velocity.y === 0) {
                    return;
                }
                
                const head = {
                    x: snake[0].x + velocity.x,
                    y: snake[0].y + velocity.y
                };
                
                // Check wall collision
                if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
                    gameOver();
                    return;
                }
                
                // Check self collision (skip the head itself)
                for (let i = 0; i < snake.length; i++) {
                    if (head.x === snake[i].x && head.y === snake[i].y) {
                        gameOver();
                        return;
                    }
                }
                
                snake.unshift(head);
                
                // Check food collision
                if (head.x === food.x && head.y === food.y) {
                    score++;
                    scoreElement.textContent = score;
                    generateFood();
                } else {
                    snake.pop();
                }
            }
            
            function generateFood() {
                food = {
                    x: Math.floor(Math.random() * tileCount),
                    y: Math.floor(Math.random() * tileCount)
                };
                
                // Make sure food doesn't spawn on snake
                for (let segment of snake) {
                    if (food.x === segment.x && food.y === segment.y) {
                        generateFood();
                        return;
                    }
                }
            }
            
            function gameOver() {
                gameRunning = false;
                ctx.fillStyle = '#00ff00';
                ctx.font = '30px Courier New';
                ctx.textAlign = 'center';
                ctx.fillText('Game Over!', canvas.width / 2, canvas.height / 2);
                ctx.font = '16px Courier New';
                ctx.fillText('Refresh to play again', canvas.width / 2, canvas.height / 2 + 30);
            }
            
            document.addEventListener('keydown', (e) => {
                if (!gameRunning) return;
                
                // Prevent default behavior for arrow keys
                if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
                    e.preventDefault();
                }
                
                // Hide start hint once game starts
                if (startHint) {
                    startHint.style.display = 'none';
                }
                
                // Prevent reverse direction
                switch(e.key) {
                    case 'ArrowUp':
                    case 'w':
                    case 'W':
                        if (velocity.y === 0) {
                            velocity = {x: 0, y: -1};
                        }
                        break;
                    case 'ArrowDown':
                    case 's':
                    case 'S':
                        if (velocity.y === 0) {
                            velocity = {x: 0, y: 1};
                        }
                        break;
                    case 'ArrowLeft':
                    case 'a':
                    case 'A':
                        if (velocity.x === 0) {
                            velocity = {x: -1, y: 0};
                        }
                        break;
                    case 'ArrowRight':
                    case 'd':
                    case 'D':
                        if (velocity.x === 0) {
                            velocity = {x: 1, y: 0};
                        }
                        break;
                }
            });
            
            gameLoop();
        </script>
    </body>
    </html>
    """


@router.get("/faruk")
def read_faruk(request: Request, game: bool = False):
    # Check if this is a browser request (not an API call) or game parameter is set
    accept_header = request.headers.get("accept", "").lower()
    is_browser = "text/html" in accept_header and "application/json" not in accept_header
    
    # If game parameter is set or it's a browser request, return the snake game
    if game or is_browser:
        return HTMLResponse(content=get_snake_game_html())
    
    # Otherwise return JSON for the main page table
    return {
        "student": "Faruk",
        "message": "Hello amigos - and, welcome on board!",
    }

