#include "lists.h"

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: the double pointer to the beginning of the list
  * Return: 0 if not a palindrome, 1 if it is
  */
int is_palindrome(listint_t **head)
{
	listint_t *upper;
	listint_t *lower;
	listint_t *reverse;
	int count;
	int i;
	int move;

	if (head == NULL || *head == NULL)
		return (0);
	reverse = *head;
	for (count = 1; reverse->next != NULL; count++)
		reverse = reverse->next;
	upper = lower = *head;
	if (count % 2 == 0)
		move = (count / 2) - 1;
	else
		move = count / 2;
	for (i = 0; i < move; i++)
	{
		upper = upper->next;
		if (i == 0 && count % 2 == 0)
			lower = lower->next; /*needs to move 1 extra time*/
		lower = lower->next;
	}
	while (lower != NULL)
	{
		reverse = *head;
		printf("Upper is: %d and Lower is: %d\n", upper->n, lower->n);
		if (lower->n != upper->n)
			return (0);
		while (reverse->next != upper && upper != *head)
			reverse = reverse->next;
		upper = reverse;
		lower = lower->next;
	}
	return (1);
}
