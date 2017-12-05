#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow_ptr;
	listint_t *fast_ptr;

	slow_ptr = fast_ptr = list;
	while (fast_ptr->next != NULL && fast_ptr->next->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (slow_ptr == fast_ptr)
			return (1);
	}
	return (0);
}
