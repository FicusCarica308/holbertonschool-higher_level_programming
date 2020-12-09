#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
size_t find_max_index(const listint_t *h, int num)
{
	const listint_t *temp = h;
	int index_max = 0;

	if (temp == NULL)
		return (0);

	while (temp != NULL)
	{
		if (num > temp->n)
                        index_max++;
		temp = temp->next;
	}

	return (index_max);
}
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *before, *after, *new;
	int max_idx = 0;
	int i = 0;
	(void)before;
	(void)after;
	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	temp = *head;
	max_idx = find_max_index(temp, number);
	for (i = 1; i < max_idx; i++)
	{
		temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;
	return (new);
}
