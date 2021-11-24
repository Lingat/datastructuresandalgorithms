#include <stdio.h>
#include <stdlib.h>

int main () {
   FILE * fp;
    
   fp = fopen ("file.txt", "w+");
   fprintf(fp, "%s %s %s %d", "We", "are", "in", 2012);
   
   fclose(fp);
   
   return(0);
}'

https://teams.microsoft.com/l/team/19%3a47a699d195c44ee89b2d450c113f6236%40thread.tacv2/conversations?groupId=dc6b2e1e-57f5-4294-b984-47d3bd8badaf&tenantId=05a0e69a-418a-47c1-9c25-9387261bf991'