#include<stdio.h>
#include<stdlib.h>    //standard library for dynamic memory allocation

struct node{       //creating  our own data type "node" using struct
    int data;
    struct node *next;
};

int main()
{
    struct node *head = NULL, *temp = NULL, *new_node = NULL;

    int choice = 1;
    while(choice == 1)
    {
        new_node = (struct node *)malloc(sizeof(struct node));

        if(new_node == NULL)
        {
            printf("memory allocation failed\n");
            return 1;
        }

        printf("enter data:\n");
        scanf("%d",&new_node ->data);

        new_node -> next = NULL;

        if(head == NULL)
        {
            head = temp = new_node;
        }
        else{
            temp -> next = new_node;
            temp = new_node;

        }

        printf("Press 1 to add another node, 0 to stop :\n");
        scanf("%d",&choice);
    }

    printf("Linked list elements are \n");

    temp = head;      
        // Because if we move head, we would lose the starting point of the list.
       // So we use a temporary pointer (temp) to traverse the list safely.

    while(temp != NULL)
    {
        printf("%d -> ",temp ->data);
        temp = temp ->next;                     

// It moves temp forward to the next node.
    }
        printf("NULL\n");

        return 0;
}

