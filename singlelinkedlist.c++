 class Node
 {
 	int data;
 	Node *next;

 	Node(int d)
 	{
 		this->data=d;

 	}
 };

 Node *start = NULL;

 void insertlast(int d)
 {
 	Node *temp=start;
 	Node *node= new Node(d);
 	node->next=NULL;
 	if(start==NULL)
 	{
 		start=node;
 	}
 	while(temp->next!=NULL)
 	{
 		temp=temp->next;
 	}
 	temp->next=node;
 }

void insertfirst(int d)
{
	Node *temp=start;
	Node *node=new Node(d);
	start=node;
	node->next= temp;
}

void insertmiddle(int d)
{
	Node *temp=start;
	Node *node= new Node();
	if(start==NULL)
	{
		cout<<"empty";
	}
	while(temp->next!=NULL && temp->!=sdata)
	{
		temp=temp->next;
	}
	if(temp->next!=NULL)
	{
		node->next=temp->next;
		temp->next=node;

	}
	else
		cout<<"not found";

}

void main()
{
	int d,sdata;
	
}
























