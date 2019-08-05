#include<iostream>
using namespace std;
main()
{
	int i,j,t;
	int n,m,a[100][100];
	cin>>n>>m;
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
			cin>>a[100][100];
	}
	for(i=0;i<n;i++)
	{ 
		for(j=m;j>=0;j--)
		{	
			cout<<a[i][j];
			t=i;
			i=j;
			j=t;
			cout<<a[i][j];
		
			
		}
	}
}
