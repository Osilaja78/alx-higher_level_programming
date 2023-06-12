#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of the liinked list
 *
 * Return: 1 if the list is a palindrome else 0.
 */
int is_palindrome(listint_t **head)
{
	int i, j, buf[2048];
	listint_t *current = *head;

	i = 0;
	j = 0;

	if (*head)
	{
		while (current != NULL)
		{
			buf[i] = current->n;
			current = current->next;
			i++;
		}

		while (j < i / 2)
		{
			if (buf[j] == buf[i - j - 1])
				j++;
			else
				return (0);
		}
	}
	else
		return (1);
	return (1);
}
