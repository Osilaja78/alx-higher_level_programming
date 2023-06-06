#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts an new node to a lined list.
 * @head: head node of list
 * @number: number to add to list
 *
 * Return: new node created.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current;

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}

