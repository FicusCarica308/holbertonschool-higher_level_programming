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
    int cnt = 0;
    int list_lgt = 0;
    listint_t *temp = *head;

    array = malloc(sizeof(int*));
    while (temp != NULL)
    {
        array[cnt] = temp->n;
        list_lgt++;
        cnt++;
        temp = temp->next;
    }

    if (list_lgt == 0)
        return (1);

    if (check_array(array, list_lgt - 1) == 1)
		return (1);
    free(array);
    return (0);
}