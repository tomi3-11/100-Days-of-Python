#include <stdio.h>

// Function prototypes
void writeToFile(char fileName[20], char text[50]);
void readFromfile(char fileName[20]);
void appendToFile(char fileName[20], char text[50]);

int main() {
	// Main function for file handling functions
	char fileName[20] = "greet.txt";
	char text[50] = "Hello world\n";

	writeToFile(fileName, text);
	appendToFile(fileName, text);
	readFromfile(fileName);

	return 0;
	
}

void writeToFile(char fileName[20], char text[50]){
	// write to the file
	FILE *fptr;

	fptr = fopen(fileName, "w");

	fprintf(fptr, text);

	fclose(fptr);
}

void appendToFile(char fileName[20], char text[50]){
	FILE *fptr;
	fptr = fopen(fileName, "a");
	fprintf(fptr, text);
	fclose(fptr);
}

void readFromfile(char fileName[20]){
	FILE *fptr;
	fptr = fopen(fileName, "r");
	char output[100];
	fgets(output, 100, fptr);
	printf("%s", output);
	fclose(fptr);
}
	
