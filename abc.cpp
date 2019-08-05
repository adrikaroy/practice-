#include<bits/stdc++.h>
using namespace std;
int main()
{
	int i,j,n;
	char ch;
	cin>>n;
	for(i=0;i<n;i++)
	{
		ch='a';
		for(j=0;j<i+1;j++)
		{
			cout<<ch;
			ch++;
			if (ch==26+'a') ch='a';       //ch>'z'
	    }
	    cout<<"\n";
	}
	
}
