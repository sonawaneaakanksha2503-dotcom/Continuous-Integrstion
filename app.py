from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Game state
board = [""] * 9
current_player = "X"

# Check winner function
def check_winner():
    win_combinations = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    
    for a,b,c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    
    if "" not in board:
        return "Draw"
    
    return None

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Handle move
@app.route('/move', methods=['POST'])
def move():
    global current_player
    
    data = request.get_json()
    index = data['index']
    
    if board[index] == "":
        board[index] = current_player
        winner = check_winner()
        
        if not winner:
            current_player = "O" if current_player == "X" else "X"
        
        return jsonify({
            "board": board,
            "winner": winner,
            "current_player": current_player
        })

    return jsonify({
        "board": board,
        "winner": None,
        "current_player": current_player
    })

# Reset game
@app.route('/reset')
def reset():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    return jsonify({"status": "reset"})

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)