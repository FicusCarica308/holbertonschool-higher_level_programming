#include "lists.h"
/**
 *check_array - checks if the array is a palandrome
 *@array: the array to be checked
 *@lgt: the lenght of the array (max index)
 *Return: returns 0 if not palindrome and 1 if it is
 */
int check_array(int *array, int lgt)
{
    int count = 0;
    while (count <= lgt)
    {
	if (array[count] != array[lgt - count])
		return (0);
    count++;
    }
	return (1);
}
int is_palindrome(listint_t **head)
{
    int *array;
    int i = 0;
    int list_lgt = 0;
    listint_t *temp = *head;

    for (list_lgt = 0; temp != NULL; list_lgt++)
        temp = temp->next;

    if (list_lgt == 0)
        return (1);

    array = malloc(sizeof(int) * list_lgt);
    temp = *head;
    for (i = 0; i < list_lgt; i++)
        {
            array[i] = temp->n;
            temp = temp->next;
        }
    if (check_array(array, list_lgt - 1) == 1)
		return (1);
    free(array);
    return (0);
}