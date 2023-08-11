#include "lists.h"

/**
 * insert_node - Inserts numbers into some sorted singly_linked_list for this program
 * @head: The linked_list will have a pointer assigned to it's head
 * @number: The number to be inserted.
 *
 * Author: Dtechguru
 * Return: If function promts an error return -NULL
 * Otherwise - a pointer to the new node for the program.
 */

listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *new;
	/* Dtechguru */
        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;

        if (node == NULL || node->n >= number)
        {
                new->next = node;
                *head = new;
                return (new);
        }

        while (node && node->next && node->next->n < number)
                node = node->next;

        new->next = node->next;
        node->next = new;

        return (new);
}

