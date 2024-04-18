#include <stdio.h>
#include <string.h>

#define MAX_CHAR 256

// Function to preprocess the pattern and generate the shift table
void preProcessShiftTable(char pattern[], int patternLength, int shiftTable[]) {
    for (int i = 0; i < MAX_CHAR; i++) {
        shiftTable[i] = patternLength;
    }
    for (int i = 0; i < patternLength - 1; i++) {
        shiftTable[pattern[i]] = patternLength - 1 - i;
    }
}

// Function to perform string matching using Horspool's algorithm
int horspoolSearch(char text[], char pattern[], int *keyComparisons) {
    int textLength = strlen(text);
    int patternLength = strlen(pattern);

    int shiftTable[MAX_CHAR];
    preProcessShiftTable(pattern, patternLength, shiftTable);

    int i = patternLength - 1;
    while (i < textLength) {
        int k = 0;
        while (k < patternLength && pattern[patternLength - 1 - k] == text[i - k]) {
            k++;
            (*keyComparisons)++;
        }
        if (k == patternLength) {
            return i - patternLength + 1; // Match found
        } else {
            i += shiftTable[text[i]]; // Shift the pattern according to the shift table
            (*keyComparisons)++;
        }
    }
    return -1; // Match not found
}

int main() {
    char text[100], pattern[100];
    int keyComparisons = 0;

    printf("Enter the text: ");
    fgets(text, sizeof(text), stdin);
    printf("Enter the pattern to search for: ");
    fgets(pattern, sizeof(pattern), stdin);

    // Remove newline characters from inputs
    text[strcspn(text, "\n")] = '\0';
    pattern[strcspn(pattern, "\n")] = '\0';

    int successfulMatchIndex = horspoolSearch(text, pattern, &keyComparisons);
    if (successfulMatchIndex != -1) {
        printf("Successful search. Match found at index: %d\n", successfulMatchIndex);
    } else {
        printf("Unsuccessful search. No match found.\n");
    }

    printf("Number of key comparisons: %d\n", keyComparisons);

    return 0;
}
