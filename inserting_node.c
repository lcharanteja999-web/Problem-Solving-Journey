

#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};

struct node *createlist()
{
    struct node *head = NULL, *temp = NULL, *new_node = NULL;

    int choice = 1;

    while(choice ==1)
    {
        new_node = (struct node *)malloc(sizeof(struct node));

        if(new_node == NULL)
        {
            printf("list is empty\n");
            return NULL;                              
                //  So you must return a pointer, not integer. thats why u cant write return 0
        }

        new_node -> next = NULL;

        printf("enter data:\n");
        scanf("%d",&new_node ->data);

        if(head ==  NULL)
        {
            head = temp = new_node;
        }
        else{
            temp -> next = new_node;
            temp = new_node;
        }
        

        printf("press 1 to continue and 0 to stop\n");
        scanf("%d",&choice);

         
    }

    return head;
  
}

void result(struct node *r)          // printing result
{
    while(r != NULL)
    {
        printf("%d -> ",r ->data);
        r= r ->next;

    }

    printf("NULL\n");
}
int count(struct node *c)    //counting number of nodes
{
    int count = 0;
    struct node *temp = c;
    while(temp -> next!= NULL)
    {
        count++;
        temp = temp ->next;
    }
    return count;
}

struct node *insert(struct node *f){        // inserting at beginniing
    struct node *new_node = NULL;

    new_node = (struct node*)malloc(sizeof(struct node));

    if(new_node == NULL)
    {
        printf("list is empty\n");
        return NULL;
    }

    printf("enter data to insert at first node\n");
    scanf("%d",&new_node->data);

    new_node -> next = f;
    f= new_node;
    return f;
}
struct node *insert_last(struct node *last){     //insert at last
    struct node *new_node, *temp;

    new_node = (struct node*)malloc(sizeof(struct node));


    printf("enter data to insert at last node\n");
    scanf("%d",&new_node->data);

    new_node->next = NULL;

    temp = last;
    while(temp->next != NULL)
    {
        temp = temp->next;
    }

    temp->next = new_node;

    return last;
}

struct node *insert_position(struct node *head, int pos){     // insert at position
    struct node *new_node, *temp;

    new_node = (struct node*)malloc(sizeof(struct node));

    new_node ->next = NULL;
    printf("enter data to insert at position\n");
    scanf("%d",&new_node ->data);


    temp = head;

    for(int i =1; i <pos -1; i++)
    {
        temp = temp ->next;
    }
    new_node -> next = temp ->next;
    temp -> next = new_node;

    return head;
}
int main()  //main function
{
    struct node *p;
  
    p = createlist();
  
    printf("original list is\n");
    result(p);
 
   p =  insert(p);
    printf("after insertion at first node the list is\n");
    result(p);

 p = insert_last(p);
    printf("after insertion at last node the list is\n");
    result(p);

    int pos ;
    printf("enter position to insert\n");
    scanf("%d",&pos);

    p = insert_position(p,pos);
    printf("after insertion at  specific position the list is\n");
    result(p); 

   int total = count(p);

    printf("count is  %d ",total);
}