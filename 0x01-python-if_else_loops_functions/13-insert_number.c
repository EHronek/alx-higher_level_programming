#include "lists.h"
#include <stdlib.h>
/**
  * insert_node - inserts a number into a sirted singly linked list
  * @head: pointer to the head of a node
  * Return: address of the new node, or NULL if it fails
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_h;
	listint_t *new_node;

	node_h = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node)
		return (NULL);
	new_node->n = number;
	if (node_h == NULL || node_h->n >= number)
	{
		new_node->next = node_h;
		*head = new_node;
		return (new_node);
	}
	while (node_h && node_h->next && node_h->next->n < number)
		node_h = node_h->next;
	new_node->next = node_h->next;
	node_h->next = new_node;
	return (new_node);
}
