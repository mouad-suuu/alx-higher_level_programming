#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head;
    listint_t *slow = *head;
    listint_t *prev = NULL;
    listint_t *halfReversed = NULL;
    
    if (*head == NULL || (*head)->next == NULL)
        return (1);
    
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
        slow = slow->next;

    prev->next = NULL;

    while (slow != NULL)
    {
        listint_t *temp = slow->next;
        slow->next = halfReversed;
        halfReversed = slow;
        slow = temp;
    }

    while (halfReversed != NULL)
    {
        if ((*head)->n != halfReversed->n)
            return (0);
        
        *head = (*head)->next;
        halfReversed = halfReversed->next;
    }

    return (1);
}

