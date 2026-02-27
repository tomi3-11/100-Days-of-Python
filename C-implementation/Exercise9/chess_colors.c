#include <stdio.h>

// Function prototypes
char* getChessColor(int col, int row);

int main(){
	// Chess square color functions
	int col, row;

	printf("Column: ");
	scanf("%d", &col);
	printf("Row: ");
	scanf("%d", &row);

	printf("%s", getChessColor(col, row));

	return 0;
}


char* getChessColor(int col, int row){
	if (col > 7){
		return "";
	}
	if (row > 7){
		return "";
	}

	if ((col % 2 != 0 && row % 2 != 0) || (col % 2 == 0 && row % 2 == 0)){
		return "white\n";
	}

	if ((col % 2 != 0 && row % 2 == 0) || (col % 2 == 0 && row % 2 != 0)){
		return "black\n";
	}

}
	
