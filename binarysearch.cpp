#include<iostream>
using namespace std;
int binarysearch(int a[], int n, int x)
{
	int low=0,high=n-1;
	while(low<=high)
	{
		int mid= (low+high)/2;
		if (x==a[mid]) return mid;
		else if (x<a[mid]) high=mid-1;
		else low=mid+1;
				
	} return -1;
	
}
int main()
{
	int x;
	int a[]= {1,2,3,4,5,6};
	cin>>x;
	int index= binarysearch(a,6,x);
	if (index!=-1) cout<<"element found at"<<index;
	else cout<<"not found";
	
}

