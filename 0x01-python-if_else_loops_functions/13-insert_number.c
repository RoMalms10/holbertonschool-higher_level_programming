#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *forward;
	listint_t *newnode;

	if (head == NULL)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (*head == NULL)
	{
		*head = newnode;
		newnode->next = NULL;
		return (newnode);
	}
	current = *head;
	if (newnode->n < current->n)
	{
		newnode->next = current;
		*head = newnode;
		return (newnode);
	}
	do {
		forward = current->next;
		if (newnode->n < forward->n)
		{
			newnode->next = forward;
			current->next = newnode;
			return (newnode);
		}
		current = current->next;
	} while (forward != NULL);
	newnode->next = NULL;
	current->next = newnode;
	return (newnode);
}
