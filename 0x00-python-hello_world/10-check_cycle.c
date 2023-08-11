#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle connection in the program
 * @list: linked list to check
 *
 * Author: Dtechguru
 * Return: 1 is to be returned if list has a ircle, 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	/*Dtechguru*/
	listint_t *slow = list;
	listint_t *fast = list;

	/*Dtechguru*/
	if (!list)
		return (0);

	/*Dtechguru*/
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
