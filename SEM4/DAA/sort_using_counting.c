#include <stdio.h>
#include <stdlib.h>

// Function to perform distribution counting sort
void distributionCountingSort(int arr[], int n) {
    // Find the maximum element in the array
    int max = arr[0];
    for (int i = 1; i < n; ++i) {
        if (arr[i] > max)
            max = arr[i];
    }

    // Create a count array to store the count of each element
    int* count = (int*)calloc(max + 1, sizeof(int));

    // Store the count of each element in the count array
    for (int i = 0; i < n; ++i)
        count[arr[i]]++;

    // Modify the count array to store the position of each element in the sorted array
    for (int i = 1; i <= max; ++i)
        count[i] += count[i - 1];

    // Create a temporary array to store the sorted elements
    int* output = (int*)malloc(n * sizeof(int));

    // Fill the output array using the count array
    for (int i = n - 1; i >= 0; --i) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    // Copy the sorted elements back to the original array
    for (int i = 0; i < n; ++i)
        arr[i] = output[i];

    // Free dynamically allocated memory
    free(count);
    free(output);
}

// Function to print the sorted array
void printArray(int arr[], int n) {
    printf("Sorted array: ");
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    printf("\n");
}

// Main function
int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    // Input elements of the array
    int* arr = (int*)malloc(n * sizeof(int));
    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &arr[i]);

    // Perform distribution counting sort
    distributionCountingSort(arr, n);

    // Print the sorted array
    printArray(arr, n);

    // Free dynamically allocated memory
    free(arr);

    return 0;
}
