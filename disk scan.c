mahe
#include<stdio.h>
#include<stdlib.h>
int main()
{
int n,h,distance=0,head,temp,track,i,j;
printf("Enter the no of requests\n");
scanf("%d",&n);
printf("Enter the request order\n");
int req[n];
for(i=0;i<n;i++)
scanf("%d",&req[i]);
printf("Enter head position\n");
scanf("%d",&h); head=h;
printf("Enter the total no of tracks\n");
scanf("%d",&track);
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(req[i]<req[j])
{temp=req[j];
req[j]=req[i];
req[i]=temp;}
}
}
int position;
for(i=0;i<n;i++)
{
if(req[i]>h)
{
position=i;break;
}
}
distance=(((track-1)-head)+((track-1)-req[0]));
printf("Service Order:");
printf("%d->",head);
for(i=position;i<n;i++){
if(req[i]!=head)
printf("%d->",req[i]);}
printf("%d->",track-1);
for(i=position-1;i>=1;i--)
printf("%d->",req[i]);
printf("%d",req[0]);
printf("\nTotal seek time=%d",distance);
printf("\nAverage seek time=%f",((float)distance/n));
}
