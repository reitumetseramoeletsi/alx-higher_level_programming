#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Checks weather or no the list has a cycle in it
 * @list: The given list for a check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	int *buf;
	int size;
	int i;
	int j;

	size = print_listint(list);
	buf = malloc(sizeof(int) * size);

	if (buf == NULL)
		exit(1);

	for (i = 0; i < size; i++)
	{
		buf[i] = list->n;
		list = list->next;
		for (j = i; j >= 0; j--)
		{
			if (list->n == buf[j - 1])
				return (1);
		}
	}
	return (0);
}
