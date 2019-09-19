#include "lists.h"
/**
 * is_palindrome - checks if sigly linked list is a palindrome
 * @head: pointer to the linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *b = *head, *e = b;
	int end = 0, beg = 0, i;

	if (b == NULL || b->next == NULL)
		return (1);

	while (b->next)
	{
		b = b->next;
		end++;
	}
	b = *head;
	while (beg < end)
	{
		e = b;
		i = beg;

		while (i < end)
		{
			e = e->next;
			i++;
		}

		if (e->n != b->n)
			return (0);
		beg++;
		end--;
		b = b->next;
	}
	return (1);
}
