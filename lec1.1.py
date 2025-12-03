import streamlit as st
import numpy as np
import random

st.title("🔴 Four in a Row — Human vs Computer")

ROWS = 6
COLS = 7

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = np.zeros((ROWS, COLS), dtype=int)
if "turn" not in st.session_state:
    st.session_state.turn = 1  # 1 = human, 2 = computer
if "winner" not in st.session_state:
    st.session_state.winner = None


def drop_piece(board, col, piece):
    """Place a piece in the selected column."""
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == 0:
            board[r][col] = piece
            return True
    return False


def check_winner(board, piece):
    """Check all win conditions."""
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    return False


def computer_move():
    """Computer picks a random valid column."""
    valid_cols = [c for c in range(COLS) if st.session_state.board[0][c] == 0]
    if valid_cols:
        col = random.choice(valid_cols)
        drop_piece(st.session_state.board, col, 2)


# SHOW BOARD
st.write("Board:")
display = st.sessi
