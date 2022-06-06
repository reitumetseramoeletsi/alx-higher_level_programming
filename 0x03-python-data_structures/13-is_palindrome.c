#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - determines if a string is palindrome
 * @head: pointer to the head of a list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tail;
	listint_t *tmp;
	listint_t *current;
	listint_t *current_h;

	current = *head;
	current_h = *head;
	tmp = NULL;

	while (current != NULL)
	{
		tail = current;
		current = current->next;
		tail->next = tmp;
		tmp = tail;
	}

	while (current_h != NULL)
	{
	
		printf("%d ", current_h->n);
		current_h = current_h->next;
	}
	while (tail != NULL)
	{
/*		if (tail == current_h)
		{
			tail = tail->next;
			current_h = current_h->next;
		}*/
		printf("%d ", tail->n);
		tail = tail->next;
	}

	return (1);
}
int main(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 1);
	is_palindrome(&head);

/*	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
    	else
		printf("Linked list is not a palindrome\n");*/

	return (0);
}
