#include "lists.h"

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: the double pointer to the beginning of the list
  * Return: 0 if not a palindrome, 1 if it is
  */
int is_palindrome(listint_t **head)
{
	listint_t *length;
	listint_t *reversed_head;
	unsigned int count;

	if (head == NULL || *head == NULL)
		return (1);
	length = *head;
	for (count = 0; length != NULL; count++)
		length = length->next;
	if (count == 1)
		return (1); /*List of 1 is palindrome*/
	reversed_head = reverse_list(*head, count);
	if (is_pal(*head, reversed_head) == 1)
		return (1);
	else
		return (0);
}

/**
  *
  *
  *
  *
  */
listint_t *reverse_list(listint_t *head, unsigned int count)
{
	listint_t *upper;
	listint_t *middle;
	listint_t *lower;

	if (count % 2 == 0)
		count = (count / 2) - 1;
	else
		count = count / 2;
	upper = head;
	for (; count > 0; count--)
		upper = upper->next;
	middle = upper->next; /*before next loop because need to make NULL*/
	lower = middle->next;
	upper->next = NULL;
	middle->next = NULL;
	upper = middle;
	middle = lower;
	while (middle != NULL)
	{
		lower = lower->next;
		middle->next = upper;
		upper = middle;
		middle = lower;
	}
	return (upper);
}

/**
  *
  *
  *
  */
int is_pal(listint_t *head, listint_t *reversed_head)
{
	while (reversed_head != NULL)
	{
		if (head->n != reversed_head->n)
			return (0);
		head = head->next;
		reversed_head = reversed_head->next;
	}
	return (1);
}
