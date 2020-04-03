#include <iostream>
#include <cmath>
#include <string>

using namespace std;

class TicTacToe{
public: 
	TicTacToe();
	~TicTacToe();
	void jouer(int x, int y);
	int nb;

private:
	bool **Board;
	void verification();
	void affich();
	int **table;
	int player;
};

TicTacToe::TicTacToe(){
	nb = 0;
	player = 1;
	Board = new bool*[3];
	table = new int*[3];
	for(int i = 0; i <3; i++){
		Board[i] = new bool[3];
		table[i] = new int[3];
    	for(int j=0;j<3;j++){
      		Board[i][j] = false;
      		table[i][j] = 0;
      }
   }
}

TicTacToe::~TicTacToe(){
	for(int i=0; i < 3; i++){
		delete [] table[i];
		delete [] Board[i];
	}
	delete []table;
	delete []Board;
	cout << endl;
}


void TicTacToe::affich(){
	for(int i=0; i<3; i++){
		for(int j=0; j<3; j++){
			if(Board[i][j] == false)
				cout << "| ";
			else
				if(table[i][j] == 1)
					cout << "|X";
				else
					cout << "|O";
		}
		cout << "|" << endl;
	}
}

void TicTacToe::jouer(int x, int y){
	if(nb == 1)
		cout << "Game already over" << endl;
	if(Board[x-1][y-1] != false){
		cout << "Error, try again" << endl;
		cout << "Player " << player << endl;
	}
	else{
		Board[x-1][y-1] = true;
		if(player == 1){
			cout << "Player 1" <<endl;
			table[x-1][y-1] = 1;
			player = 2;}
		else{
			cout << "Player 2" <<endl;
			table[x-1][y-1] = -1;
			player = 1;}
		}
	affich();
	verification();
	cout << endl;
}

void TicTacToe::verification(){
	int s = 0;
	for(int i = 0; i <3; i++){
		int sum1, sum2, sum3, sum4;
		sum1 = sum2 = sum3 = sum4 = 0;
		for(int j = 0; j<3; j++){
			sum1 += table[i][j];
			sum2 += table[j][i];
			sum3 += table[j][j];
			sum4 += table[j][2-j];
			s += (int)Board[i][j];
		}
		if(sum1 == 3 || sum1 == -3 || sum2 == 3 || sum2 == -3 || sum3 == 3 || sum3 == -3 || sum4 == 3 || sum4 == -3){
			nb = 1;
			if(sum1 == 3 || sum2 == 3 || sum3 == 3 || sum4 == 3){
				cout << "Player 1 wins!" << endl;
				break;
			}
			else{
				cout << "Player 2 wins!" << endl;
				break;
			}
		}
	}
	if(s==9)nb=1;
}



int main(){
	TicTacToe B;
	while(B.nb == 0){
		int x;
		int y; 
		cout << "Donnez les coordonnées x et y:" << endl;
		cin >> x;
		cin >> y;
		cout << endl;
		B.jouer(x,y);
		if(B.nb != 0){
			cout << "*************" << endl;
			cout << " Jeu Terminé " << endl;
			cout << "*************" << endl;
		}
	}
}
