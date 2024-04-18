#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define V 6 // Number of vertices in the graph

// Function prototypes
void dijkstra(int graph[V][V], int src);
int minDistance(int dist[], int visited[]);

void dijkstra(int graph[V][V], int src) {
    int dist[V]; // Array to store the shortest distance from src to i
    int visited[V]; // Array to keep track of visited vertices

    // Initialize distances as INFINITE and visited array as 0
    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
        visited[i] = 0;
    }

    // Distance of source vertex from itself is always 0
    dist[src] = 0;

    // Find shortest path for all vertices
    for (int count = 0; count < V - 1; count++) {
        // Pick the minimum distance vertex from the set of vertices not yet processed
        int u = minDistance(dist, visited);

        // Mark the picked vertex as visited
        visited[u] = 1;

        // Update dist value of the adjacent vertices of the picked vertex
        for (int v = 0; v < V; v++) {
            // Update dist[v] only if it's not in visited[], there is an edge from u to v, and total weight of path from src to v through u is smaller than current value of dist[v]
            if (!visited[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
        }
    }

    // Print the shortest distances
    printf("Shortest distances from vertex %d to all other vertices:\n", src);
    for (int i = 0; i < V; i++) {
        printf("Vertex %d -> Distance = %d\n", i, dist[i]);
    }
}

// Utility function to find the vertex with minimum distance value from the set of vertices not yet included in shortest path tree
int minDistance(int dist[], int visited[]) {
    int min = INT_MAX, min_index;

    for (int v = 0; v < V; v++)
        if (visited[v] == 0 && dist[v] <= min)
            min = dist[v], min_index = v;

    return min_index;
}

int main() {
    int graph[V][V]; // Weighted graph representation
    int source_vertex; // Source vertex for shortest path calculation

    // Read the weighted graph from user input
    printf("Enter the weighted graph (%d x %d matrix):\n", V, V);
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    // Read the source vertex from user input
    printf("Enter the source vertex (0 to %d): ", V - 1);
    scanf("%d", &source_vertex);

    // Find and print shortest path from source vertex to all other vertices using Dijkstra's algorithm
    dijkstra(graph, source_vertex);

    return 0;
}
