#include<stdio.h>
#include<stdlib.h>
int main()
{ int n,h,distance=0,head;
printf("Enter the no of requests\n");
scanf("%d",&n);
printf("Enter the request order\n");
int req[n];
for(int i=0;i<n;i++)
{
scanf("%d",&req[i]);
}
printf("Enter the head position\n");
scanf("%d",&h); head=h;
for(int i=0;i<n;i++)
{
distance=distance+abs(req[i]-h);
h=req[i];
}
printf("Service Order:");
printf("%d->",head);
for(int i=0;i<n-1;i++){
if(req[i]!=h)
printf("%d->",req[i]);}
printf("%d",req[n-1]);
printf("\nTotal seek time=%d",distance);
printf("\nAverage seek time=%f",((float)distance/n));
}
