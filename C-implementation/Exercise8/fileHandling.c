#include <stdio.h>

// Function prototypes
void writeToFile(char fileName[20], char text[50]);

int main() {
	// Main function for file handling functions
	char fileName[20] = "greet.txt";
	char text[50] = "Hello world\n";

	writeToFile(fileName, text);

	return 0;
	
}

void writeToFile(char fileName[20], char text[50]){
	// write to the file
	FILE *fptr;

	fptr = fopen(fileName, "w");

	fprintf(fptr, text);

	fclose(fptr);
}
