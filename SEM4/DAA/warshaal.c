#include <stdio.h>
#include <stdbool.h>

#define MAX_VERTICES 100

int graph[MAX_VERTICES][MAX_VERTICES];
int transitiveClosure[MAX_VERTICES][MAX_VERTICES];

int max(int a, int b) {
    return (a > b) ? a : b;
}

void warshall(int vertices) {
    int i, j, k;

    // Initialize transitive closure matrix with the graph matrix
    for (i = 0; i < vertices; i++) {
        for (j = 0; j < vertices; j++) {
            transitiveClosure[i][j] = graph[i][j];
        }
    }

    // Warshall's algorithm
    for (k = 0; k < vertices; k++) {
        for (i = 0; i < vertices; i++) {
            for (j = 0; j < vertices; j++) {
                transitiveClosure[i][j] = max(transitiveClosure[i][j], transitiveClosure[i][k] && transitiveClosure[k][j]);
            }
        }
    }
}

void displayTransitiveClosure(int vertices) {
    printf("Transitive Closure:\n");
    for (int i = 0; i < vertices; i++) {
        for (int j = 0; j < vertices; j++) {
            printf("%d ", transitiveClosure[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int vertices, i, j;

    printf("Enter the number of vertices in the graph: ");
    scanf("%d", &vertices);

    printf("Enter the adjacency matrix of the graph:\n");
    for (i = 0; i < vertices; i++) {
        for (j = 0; j < vertices; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    warshall(vertices);
    displayTransitiveClosure(vertices);

    return 0;
}
