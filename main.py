from checkers.board import *
from checkers.game import Game
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys


FPS = 144




def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col
global input_log, input_pass, xor

app = QApplication(sys.argv)


def open_main():
    global main_window
    global main_ui




open_main()



def opengame(AI):

    main(AI)

def main(AI):
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Шашки 10х10')
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE and AI:
            value, new_board = game.minimax(game.get_board(), 4, True)
            game.ai_move(new_board)

        if game.winner() == RED:
            run = False
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Окончание партии")
            msgBox.setText("Игра окончена: Победа чёрных")
            msgBox.exec()

        if game.winner() == WHITE:
            run = False
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Окончание партии")
            msgBox.setText("Игра окончена: Победа белых")
            msgBox.exec()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)


        game.update()

    pygame.quit()

opengame(False)
app.exec()

