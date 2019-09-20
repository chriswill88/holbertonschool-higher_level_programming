#include "lists.h"
/**
 * is_palindrome - checks if sigly linked list is a palindrome
 * @head: pointer to the linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *b = *head, *e = b, *mid;

	if (b == NULL || b->next == NULL)
		return (1);

	while (e->next)
		e = e->next;

	while (b != e)
	{
		mid = b;

		while (mid->next != e)
			mid = mid->next;

		if (b->n != e->n)
			return (0);
		if (b == mid)
			break;
		e = mid;
		b = b->next;
	}
	return (1);
}
