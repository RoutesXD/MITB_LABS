#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Structure to represent an edge in the graph
struct Edge {
    int src, dest, weight;
};

// Structure to represent a subset for union-find
struct Subset {
    int parent;
    int rank;
};

// Function prototypes
int find(struct Subset subsets[], int i);
void Union(struct Subset subsets[], int x, int y);
int compare(const void* a, const void* b);
void KruskalMST(struct Edge* edges, int V, int E);
void printMST(struct Edge* result, int e);

// Find set of an element i
int find(struct Subset subsets[], int i) {
    if (subsets[i].parent != i)
        subsets[i].parent = find(subsets, subsets[i].parent);

    return subsets[i].parent;
}

// Perform union of two sets
void Union(struct Subset subsets[], int x, int y) {
    int xroot = find(subsets, x);
    int yroot = find(subsets, y);

    if (subsets[xroot].rank < subsets[yroot].rank)
        subsets[xroot].parent = yroot;
    else if (subsets[xroot].rank > subsets[yroot].rank)
        subsets[yroot].parent = xroot;
    else {
        subsets[yroot].parent = xroot;
        subsets[xroot].rank++;
    }
}

// Compare function used by qsort to sort edges based on their weights
int compare(const void* a, const void* b) {
    struct Edge* edge1 = (struct Edge*)a;
    struct Edge* edge2 = (struct Edge*)b;
    return edge1->weight - edge2->weight;
}

// Function to find Minimum Spanning Tree using Kruskal's algorithm
void KruskalMST(struct Edge* edges, int V, int E) {
    struct Edge result[V];
    int e = 0;
    int i = 0;

    // Sort all the edges in non-decreasing order of their weight
    qsort(edges, E, sizeof(edges[0]), compare);

    // Allocate memory for creating V subsets
    struct Subset* subsets = (struct Subset*)malloc(V * sizeof(struct Subset));

    // Create V subsets with single elements
    for (int v = 0; v < V; ++v) {
        subsets[v].parent = v;
        subsets[v].rank = 0;
    }

    // Keep adding edges until V-1 edges are added or there are no more edges
    while (e < V - 1 && i < E) {
        // Pick the smallest edge
        struct Edge next_edge = edges[i++];

        int x = find(subsets, next_edge.src);
        int y = find(subsets, next_edge.dest);

        // If including this edge doesn't cause a cycle, add it to the result
        if (x != y) {
            result[e++] = next_edge;
            Union(subsets, x, y);
        }
    }

    // Print the constructed MST
    printMST(result, e);

    free(subsets);
}

// Print the MST
void printMST(struct Edge* result, int e) {
    printf("Following are the edges in the constructed MST:\n");
    for (int i = 0; i < e; ++i)
        printf("%d -- %d == %d\n", result[i].src + 1, result[i].dest + 1, result[i].weight);
}

int main() {
    int V, E;
    printf("Enter the number of vertices and edges: ");
    scanf("%d %d", &V, &E);

    // Array of edges with their source, destination, and weight
    struct Edge* edges = (struct Edge*)malloc(E * sizeof(struct Edge));

    printf("Enter the details of each edge (source, destination, weight):\n");
    for (int i = 0; i < E; ++i) {
        scanf("%d %d %d", &edges[i].src, &edges[i].dest, &edges[i].weight);
        // Adjust indices to match array indexing (starting from 0)
        edges[i].src--;
        edges[i].dest--;
    }

    clock_t start_time = clock(); // Measure start time

    KruskalMST(edges, V, E);

    clock_t end_time = clock(); // Measure end time
    double execution_time = (double)(end_time - start_time) / CLOCKS_PER_SEC; // Calculate execution time

    printf("Execution time: %.6f seconds\n", execution_time);

    free(edges);

    return 0;
}
