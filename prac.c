/*
#include<stdio.h>
int main(int s, char *a[])
{   int	i,j,c=0;
	for(i=1;i<s;i++)
	{
	
	  j=atoi(a[i]);
	  c+=j;
	}
	printf("%d",c);
	return 0;
}


#include<stdio.h>
int main(int argc, char *argv[])
{
	while(argc--)
		printf("%s\n",argv[argc]);
	return 0;
}

#include<stdio.h>

int main(int argc, char *argv[])

  {

       printf("%s\n",*++argv);

    

     return 0;

  }

#include<stdio.h>
void main()
{
int x,a=10;
x=a==10?printf("hait"):printf("hellon"); 
printf("%d %d",x,a);
}



main()
{
double d = 123.4;
static float f =123.4;
if (d == f)
printf("equal");
else if( f > d )
printf("Float is greater");
else
printf("Double is greater");

printf("\nd=%d f=%d",sizeof(d),sizeof(f));
}


#include<stdio.h>
int main()
{
int a[5] = {5, 1, 15, 20, 25};
int i, j, m;
i = ++a[1];
j = a[1]++;
m = a[i++];
printf("%d, %d, %d", i, j, m);
return 0;
}


#include<stdio.h>
int main(int argc, char ** argv){
char **items;
int j = 3, i;
items = argv;
for(i = 1; (i%4); i++){
int **p = &items[j];
printf("%c", **p);
j--;
}
return 0;
}


#include<stdio.h>
int main(int argc,char**argv)
{
	printf("%s\n",argv[argc-1]);
	return 1;
	
}


#include <stdio.h>

int main()

{

int a=100;

printf("%d\n"+1,a);

printf("Value is = %d"+3,a);

return 0;

}

*/

#include <stdio.h>

int main()

{

float a,b;

a=3.0f;

b=4.0f;

printf("%.0f,%.1f,%.2f",a/b,a/b,a/b);

return 0;

}















































