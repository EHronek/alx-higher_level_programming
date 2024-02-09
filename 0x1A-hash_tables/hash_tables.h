#ifndef HASH_TABLES_H
#define HASH_TABLES_H

#include <stdlib.h>
#include <stddef.h>

/**
  * struct hash_node_s - Node of a hash table
  * 
  * @key: the key, string
  * the key is unique in the hash table
  * @value: the value corresponding to a key
  * @next: the pointer to the next node of the list
  */
typedef struct hash_node_s
{
	char *key;
	char *value;
	struct hash_node_s *next;
} hash_node_t;

/**
  * struct hash_table_s - hash table data structure
  *
  * @size: the size of the array
  * @array: an array of the size @size
  * Each cell of this array is a pointer to the first node of a linked list,
  * because we want our hashtable to use a chaining collision handling
  */
typedef struct hash_table_s
{
	unsigned long int size;
	hash_node_t **array;
} hash_table_t;

hash_table_t *hash_table_create(unsigned long int size);

#endif
