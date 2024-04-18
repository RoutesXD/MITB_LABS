#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define CHAR_SET_SIZE 256

// Function to preprocess the pattern and calculate the bad character heuristic array
void badCharHeuristic(char *pattern, int pattern_length, int bad_char[CHAR_SET_SIZE]) {
    for (int i = 0; i < CHAR_SET_SIZE; i++) {
        bad_char[i] = -1;
    }

    for (int i = 0; i < pattern_length; i++) {
        bad_char[(int) pattern[i]] = i;
    }
}

// Function to implement Boyer-Moore algorithm for string matching
int boyerMooreSearch(char *text, char *pattern, int *comparisons) {
    int text_length = strlen(text);
    int pattern_length = strlen(pattern);

    int bad_char[CHAR_SET_SIZE];
    badCharHeuristic(pattern, pattern_length, bad_char);

    int shift = 0;
    int j;
    int occurrences = 0;

    while (shift <= (text_length - pattern_length)) {
        j = pattern_length - 1;

        while (j >= 0 && pattern[j] == text[shift + j]) {
            j--;
            (*comparisons)++;
        }

        if (j < 0) {
            occurrences++;
            shift += (shift + pattern_length < text_length) ? pattern_length - bad_char[text[shift + pattern_length]] : 1;
        } else {
            shift += (j - bad_char[text[shift + j]] > 0) ? j - bad_char[text[shift + j]] : 1;
        }
    }

    return occurrences;
}

int main() {
    char text[] = "ABAAABCD";
    char pattern[] = "ABC";

    int comparisons_success = 0, comparisons_failure = 0;

    int occurrences = boyerMooreSearch(text, pattern, &comparisons_success);

    printf("Pattern found %d times.\n", occurrences);
    printf("Number of comparisons in successful search: %d\n", comparisons_success);

    // Unsuccessful search
    char pattern2[] = "XYZ";
    int occurrences2 = boyerMooreSearch(text, pattern2, &comparisons_failure);

    printf("Pattern not found.\n");
    printf("Number of comparisons in unsuccessful search: %d\n", comparisons_failure);

    return 0;
}
