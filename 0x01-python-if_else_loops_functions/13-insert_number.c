#include "lists.h"

/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	temp = malloc(sizeof(listint_t));
	if (new == NULL || temp == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
	} else if ((*head)->n > new->n)
	{
		temp = *head, new->next = temp;
		*head = new;
	} else
	{
		temp = *head;
		while (1)
		{
			if (temp->next == NULL)
			{
				temp->next = new;
				break;
			} else if (temp->next->n < new->n)
			{
				temp = temp->next;
			} else
			{
				new->next = temp->next, temp->next = new;
				break;
			}
		}
	}
	return (new);
}
