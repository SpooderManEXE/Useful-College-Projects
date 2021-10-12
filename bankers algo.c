#include<stdio.h>
#include<stdbool.h>

void main() {

	  int n,m,i,j,k;
	  n=5; // no of process
	  m=3; // no of resources

	  int allocation[5][3] = { { 0, 1, 0 }, 
		                { 2, 0, 0 },
		                { 3, 0, 2 }, 
		                { 2, 1, 1 }, 
		                { 0, 0, 2 } };

	  
	  int max[5][3] = {  { 7, 5, 3 }, 
		              { 3, 2, 2 }, 
		              { 9, 0, 2 }, 
		              { 2, 2, 2 }, 
		              { 4, 3, 3 } }; 

	  int available[3] = {3,3,2};

	  bool completed[n];

	  //setting all process as false
	  for(i=0;i<n;i++)
	    completed[i] = false;

	  int need[n][m]; //NEED MATRIX
	  for(i=0;i<n;i++) {
	    for(j=0;j<m;j++)
	      need[i][j] = max[i][j] - allocation[i][j];
	  }

	  //checking if system is in safe state 

	  printf("\n\nOutput\n\n");
	  int final_safe[n],ind=0; //final state
	  int c=n; //counter
	  while(c>0) {
	    for(i=0;i<n;i++) { // process loop 
	      if(completed[i] == false) { //1st condition 
				bool check = true;
				for(j=0;j<m;j++) { // resource-process access loop
					if(need[i][j]>available[j]) { //second condition - fail check
						check = false; //fail
						break;
		  }
		}
		//both conditions pass
		if(check == true) {
		  final_safe[ind++] = i;
		  c--; //process is in safe state
		  completed[i] = true;
		  //add allocation
		  for(k=0;k<m;k++)
		    available[k] += allocation[i][k];
		}
	      }
	    }
	  }
	  printf("The Safe Sequence Of The System Is:\n");
	  for(i=0;i<n-1;i++)
	    printf(" P%d -> ", final_safe[i]);
	  printf(" P%d\n",final_safe[n-1]);

	  printf("\n\nProcess\t\t\t\tNEED \n \t\t\tA\tB\tC\n\n");
	  for(i=0;i<n;i++){
	    printf("P%d\t\t\t",i);
	    for(j=0;j<m;j++)
	      printf("%d\t",need[i][j]);
	    printf("\n\n");
	  }
  
}

