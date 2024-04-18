#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TABLE_SIZE 10

// Structure for a hash table entry
struct HashEntry {
    int key;
    int data;
};

// Structure for a hash table
struct HashTable {
    int size;
    struct HashEntry *table;
};

// Function to initialize a hash table
void initHashTable(struct HashTable *ht, int size) {
    ht->size = size;
    ht->table = (struct HashEntry *)malloc(sizeof(struct HashEntry) * size);
    for (int i = 0; i < size; ++i) {
        ht->table[i].key = -1; // -1 indicates empty slot
    }
}

// Hash function
int hash(int key, int size) {
    return key % size;
}

// Function to insert a key-value pair into the hash table
void insert(struct HashTable *ht, int key, int data) {
    int index = hash(key, ht->size);
    while (ht->table[index].key != -1) {
        index = (index + 1) % ht->size; // Linear probing
    }
    ht->table[index].key = key;
    ht->table[index].data = data;
}

// Function to search for a key in the hash table
// Returns the number of key comparisons
int search(struct HashTable *ht, int key, bool *success) {
    int index = hash(key, ht->size);
    int comparisons = 1; // Counting the initial comparison
    while (ht->table[index].key != -1) {
        if (ht->table[index].key == key) {
            *success = true;
            return comparisons;
        }
        index = (index + 1) % ht->size; // Linear probing
        comparisons++;
    }
    *success = false;
    return comparisons;
}

int main() {
    struct HashTable ht;
    initHashTable(&ht, TABLE_SIZE);

    // Insert some key-value pairs into the hash table
    insert(&ht, 12, 120);
    insert(&ht, 45, 450);
    insert(&ht, 25, 250);
    insert(&ht, 33, 330);

    // Perform successful search
    bool success;
    int key_to_search = 45;
    int comparisons_success = search(&ht, key_to_search, &success);
    if (success) {
        printf("Key %d found.\n", key_to_search);
        printf("Number of comparisons in successful search: %d\n", comparisons_success);
    } else {
        printf("Key %d not found.\n", key_to_search);
    }

    // Perform unsuccessful search
    key_to_search = 55;
    int comparisons_failure = search(&ht, key_to_search, &success);
    if (success) {
        printf("Key %d found.\n", key_to_search);
    } else {
        printf("Key %d not found.\n", key_to_search);
        printf("Number of comparisons in unsuccessful search: %d\n", comparisons_failure);
    }

    free(ht.table); // Free memory allocated for hash table

    return 0;
}
