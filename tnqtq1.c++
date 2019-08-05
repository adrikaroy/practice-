#include<iostream>
using namespace std;
main()
{
	int i,j;
	int n1,n2;
	cin>>n1>>n2;
	for(i=0;i<n1;i++)
	{
		for(j=0;j<n2;j++)
		{
				if (i==0 || i==(n1-1) || j==0 || j==(n2-1))
					cout<<1<<" ";	
				else
					cout<<0<<" ";
		}cout<<"\n";
 	} 
 		
}
