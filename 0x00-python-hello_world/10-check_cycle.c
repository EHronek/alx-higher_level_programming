#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - it should check if the silinked list contains a cycle
 * @list: a singly linked list
 * Return: 0 if no cycle detected , 1 if there is a cycle in the list
 */
int check_cycle(listint_t *list)
{
	listint_t *back_p, *front_p;

	if (list == NULL || list->next == NULL)
		return (0);
	back_p = list->next;
	front_p = list->next->next;
	while (back_p && front_p && front_p->next)
	{
		if (back_p == front_p)
			return (1);
		back_p = back_p->next;
		front_p = front_p->next->next;
	}
	return (0);
}
