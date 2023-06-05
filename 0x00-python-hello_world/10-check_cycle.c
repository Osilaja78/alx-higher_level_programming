#include <stdbool.h>
#include "lists.h"

/**
 * check_cycle - cheks for a cycle in a linked list.
 * @list: head of the liked list to check
 *
 * Return: 0 if there'd no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_node, *fast_node;

	if (list == NULL || list->next == NULL)
		return (0);

	slow_node = list;
	fast_node = list;

	while (fast_node != NULL && fast_node->next != NULL)
	{
		slow_node = slow_node->next;
		fast_node = fast_node->next->next;

		if (slow_node == fast_node)
			return (1);
	}
	return (0);
}
