#include "hash_tables.h"
/**
  * hash_table_create - check a hash table
  * @size: the size of the array
  *
  * Return: NULL if an error occurs otherwise a pointer to new hash ttable
  */
hash_table_t *hash_table_create(unsigned long int size)
{
	unsigned long int i;
	hash_table_t *ht;

	/* allocating memory for hash table structure */	
	ht = (hash_table_t *) malloc(sizeof(hash_table_t));
	/* check if the memory was allocated successfully*/
	if (ht == NULL)
		return (NULL);
	ht->size = size;
	ht->array = malloc(sizeof(hash_node_t *) * size);
	if (ht->array == NULL)
		return (NULL);
	for (i = 0; i < size; i++)
		ht->array[i] = NULL;
	return (ht);
}
