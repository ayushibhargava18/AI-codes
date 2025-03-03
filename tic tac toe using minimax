#include <stdio.h>
#include <stdbool.h>
char board[3][3];
char player='X', computer='O';

void initializeBoard() {
    for (int i=0; i<3; i++)
        for (int j=0; j<3; j++) board[i][j]='_';
}

void printBoard() {
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) printf("%c ", board[i][j]);
        printf("\n");
    }
}

int evaluate() {
    for (int i=0; i<3; i++)
        if (board[i][0]==board[i][1]&&board[i][1]==board[i][2]) {
            if (board[i][0]==player) return -10;
            else if (board[i][0]==computer) return 10;
            else return 0;
        }
    for (int i=0; i<3; i++)
        if (board[0][i]==board[1][i]&&board[1][i]==board[2][i]) {
            if (board[0][i]==player) return -10;
            else if (board[0][i]==computer) return 10;
            else return 0;
        }
    if (board[0][0]==board[1][1]&&board[1][1]==board[2][2]) {
        if (board[0][0]==player) return -10;
        else if (board[0][0]==computer) return 10;
        else return 0;
    }
    if (board[0][2]==board[1][1]&&board[1][1]==board[2][0]) {
        if (board[0][2]==player) return -10;
        else if (board[0][2]==computer) return 10;
        else return 0;
    }
    return 0;
}

bool isMovesLeft() {
    for (int i=0; i<3; i++)
        for (int j=0; j<3; j++)
            if (board[i][j]=='_') return true;
    return false;
}

int minimax(int depth, bool isMax) {
    int score=evaluate();
    if (score!=0 || !isMovesLeft()) return score;
    int best;
    if (isMax) best=-1000;
    else best=1000;
    for (int i=0; i<3; i++)
        for (int j=0; j<3; j++)
            if (board[i][j]=='_') {
                if (isMax) board[i][j]=computer;
                else board[i][j]=player;
                best=isMax?(best>minimax(depth+1, !isMax)?best:minimax(depth+1, !isMax)):(best<minimax(depth+1, !isMax)?best:minimax(depth+1, !isMax));
                board[i][j]='_';
            }
    return best;
}

void findBestMove() {
    int bestVal=-1000, row=-1, col=-1;
    for (int i=0; i<3; i++)
        for (int j=0; j<3; j++)
            if (board[i][j]=='_') {
                board[i][j]=computer;
                int moveVal=minimax(0, false);
                board[i][j]='_';
                if (moveVal>bestVal) {
                    row=i;
                    col=j;
                    bestVal=moveVal;
                }
            }
    board[row][col]=computer;
}

void playerMove() {
    int row, col;
    printf("Enter row and column (0, 1, or 2) for your move (X): ");
    scanf("%d %d", &row, &col);
    if (board[row][col]=='_') board[row][col]=player;
    else {
        printf("Invalid move! Try again.\n");
        playerMove();
    }
}

int main() {
    initializeBoard();
    printBoard();
    while (true) {
        playerMove();
        printBoard();
        int score=evaluate();
        if (score==10) { printf("Computer wins!\n"); break; }
        if (score==-10) { printf("Player wins!\n"); break; }
        if (!isMovesLeft()) { printf("It's a tie!\n"); break; }
        printf("Computer's move (O):\n");
        findBestMove();
        printBoard();
        score=evaluate();
        if (score==10) { printf("Computer wins!\n"); break; }
        if (score==-10) { printf("Player wins!\n"); break; }
        if (!isMovesLeft()) { printf("It's a tie!\n"); break; }
    }
    return 0;}
