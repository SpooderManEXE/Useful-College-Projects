#include<stdio.h>
#include<unistd.h>
int main()
{
  int p,i,j;
  p=fork();
  if(p==0)
  {
    for(i=1;i<=10;i++)
    {
      printf("%d\n",i);
    }
  }
  else
  {
    sleep(3);
    for(j=20;j<=30;j++)
    {
      printf("%d\n",j);
    }
  }
}
