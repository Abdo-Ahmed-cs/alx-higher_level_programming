#include "lists.h"

/**
 * is_palindrome - checksif a singly linked list is a palidrome
 * @head: the head of the linked list
 *
 * Return: 0 if not palindorome otherwise 1
 */


int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int *numbers;
	int i, j, k = 0;

	numbers = malloc(sizeof(int));
	temp = malloc(sizeof(listint_t));
	if (!temp || !number)
		return (NULL);
	if (*head == NULL)
		return (1);
	temp = *head;
	for (i = 0; temp; i++)
	{
		numbers[i] = temp->n;
		temp = temp->next;
	}
	for (k = 0; k < (i / 2); k++)
	{
		if (numbers[k] != numbers[i - 1 - k])
		{
			return (0);
		}
	}
	temp = NULL;
	free(temp);
	free(numbers);
	return (1);
}
