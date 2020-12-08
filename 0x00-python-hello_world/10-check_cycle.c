#include "lists.h"
#include <stdio.h>
/**
 *check_cycle - checks if a cycle exists within a linked list
 *@list: the head to our given linked list
 *Return: returns 0 if there is no cycle and 1 if there is
 */
int check_cycle(listint_t *list)
{
	/*declars two seperate temp lists*/
	listint_t *temp1;
	listint_t *temp2;
	/*checks if the head we are given is NULL*/
	if (list == NULL)
		return (0);
	/*makes temp1 one index ahead of temp2 so they dont always colide*/
	temp1 = list->next;
	temp2 = list;
	/*will loop through both temp lists until or if they equal NULL*/
	while (temp1 != NULL && temp2 != NULL)
	{
		/*checks if the index of temp1 (which is ahead) is = to temp2*/
		if (temp1 == temp2)
			/*this indicates a loop so it returns 1*/
			return (1);
		/*here we check if temp1 is equal to NULL*/
		if (temp1->next == NULL)
			/*breaks the loop to avoid seg fault since temp1 is ahead*/
			break;
		/*increases temp1 by two to stay ahead of temp2*/
		temp1 = temp1->next;
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	/*if the loop completes without a return then return 0*/
	return (0);
}
