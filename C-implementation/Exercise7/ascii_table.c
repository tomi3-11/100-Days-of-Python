#include <stdio.h>

int main(){
	int start = 32;
	int stop = 126;


	for (int i = start; i <=stop; ++i){
		// Print the ascii table
		char character = (char)i;
		printf("%d %c\n", i, character);
	}
	return 0;
}
