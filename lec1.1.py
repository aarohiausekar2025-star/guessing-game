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
display = st.session_state.board.astype(str)
display = np.where(display == "0", "⚪", display)
display = np.where(display == "1", "🔴", display)
display = np.where(display == "2", "🟡", display)

for row in display:
    st.write(" ".join(row))

st.write("---")

# HUMAN TURN
if st.session_state.winner is None and st.session_state.turn == 1:
    col_choice = st.selectbox("Choose a column (0-6):", list(range(COLS)))
    if st.button("Drop Piece"):
        if drop_piece(st.session_state.board, col_choice, 1):
            if check_winner(st.session_state.board, 1):
                st.session_state.winner = "🎉 Human Wins!"
            else:
                st.session_state.turn = 2
        else:
            st.warning("Column is full. Try another.")


# COMPUTER TURN
if st.session_state.winner is None and st.session_state.turn == 2:
    st.write("Computer is thinking...")
    computer_move()

    if check_winner(st.session_state.board, 2):
        st.session_state.winner = "🤖 Computer Wins!"
    else:
        st.session_state.turn = 1

    st.rerun()


# RESULT
if st.session_state.winner:
    st.header(st.session_state.winner)

# RESET BUTTON
if st.button("Reset Game"):
    st.session_state.board = np.zeros((ROWS, COLS), dtype=int)
    st.session_state.turn = 1
    st.session_state.winner = None
    st.rerun()
