#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Function prototypes
char* findAndReplace(char* text, char* oldText, char* newText);

int main(){
	// find and replace function
	char text[100];
	char oldText[100];
	char newText[100];

	printf("Text: ");
	scanf("%s", text);
	printf("Old Text: ");
	scanf("%s", oldText);
	printf("New text: ");
	scanf("%s", newText);

	char* result = findAndReplace(text, oldText, newText);
	printf("%s\n", result);

	return 0;
}

char* slice(const char* str, size_t start, size_t end){
	char* subString = (char*)malloc(end - start+2);
	int index = 0;
	for (int i = start; i<end; i++){
		subString[index++] = str[i];	
	}
	subString[index] = '\0';
	printf("%s\n", subString);
	return subString;
}

char* findAndReplace(char* text, char* oldText, char* newText){
	char* reversedText = (char*) malloc(200);
	int index = 0;

	int size = strlen(text);
	int oldsize = strlen(oldText);

	for (int i = 0; i < size; i++){
		if (!strcmp(slice(text, i, i+oldsize), oldText)) {
			for(int k = 0; k < strlen(newText); k++){
				reversedText[index++] = newText[k];	
			}
			i += oldsize - 1;
		}else {
			reversedText[index++] = text[i];
		}	
	}
	reversedText[index] = '\0';
	return reversedText;

}
