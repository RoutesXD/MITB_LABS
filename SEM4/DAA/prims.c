#include<stdio.h>

int a[50][50], t[50][50], root[50], parent[50], n, i, j, value, e = 0, k = 0;
int ivalue, jvalue, cost = 0, mincost = 0, TV[50], count = 0, present = 0;

void read_cost() {
    printf("\nEnter the number of vertices: ");
    scanf("%d", &n);
    printf("\nEnter cost adjacency matrix:\n");
    for (i = 1; i <= n; i++) {
        for (j = i + 1; j <= n; j++) {
            printf("(%d,%d): ", i, j);
            scanf("%d", &value);
            a[i][j] = value;
            if (value != 0)
                e++;
            a[j][i] = value; // Since the graph is undirected
        }
    }
}

int check_reach(int vertex) {
    int v, queue[50], front = 0, rear = -1, reach[50], visited[50];
    for (v = 1; v <= n; v++) {
        visited[v] = 0;
        reach[v] = 0;
    }
    queue[++rear] = vertex;
    visited[vertex] = 1;
    while (front <= rear) {
        v = queue[front++];
        for (int i = 1; i <= n; i++) {
            if (a[v][i] != 0 && !visited[i]) {
                reach[i] = 1;
                queue[++rear] = i;
                visited[i] = 1;
            }
        }
    }
    return reach[n];
}

void prims() {
    while (e && k < n - 1) {
        for (i = 1; i <= n; i++) {
            for (j = 1; j <= n; j++) {
                if (a[i][j] != 0) {
                    int x = check_reach(i);
                    int y = check_reach(j);
                    if (x == 1 && y == 0) {
                        present = 1;
                        if (a[i][j] < cost || cost == 0) {
                            cost = a[i][j];
                            ivalue = i;
                            jvalue = j;
                        }
                    }
                }
            }
        }
        if (present) {
            TV[++count] = jvalue;
            parent[jvalue] = ivalue;
            cost += a[ivalue][jvalue];
            k++;
            e--;
            present = 0;
            a[ivalue][jvalue] = a[jvalue][ivalue] = 0;
        }
    }
}

void display() {
    printf("\nMinimum cost spanning tree is:\n");
    for (i = 1; i <= n; i++) {
        printf("%d <-> %d\n", parent[i], i);
    }
    printf("\nCost of minimum cost spanning tree = %d\n", cost);
}

int main() {
    TV[++count] = 1;
    read_cost();
    prims();
    display();
    return 0;
}
