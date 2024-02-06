#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
     pid_t pid = getpid();
     pid_t ppid = getppid();
     printf("Label -> CIRCLE PID -> %d PPID -> %d\n" , getpid() , getppid());
     
     int r;
     float Carea, Cperimeter;

     printf("Enter the radius of the circle: ");
     scanf("%d" , &r);

     Carea = 3.14 * r * r;
     Cperimeter = 2 * 3.14 * r;
     printf("The area of circle is %f and perimeter is %f\n", Carea, Cperimeter);

     if(!fork()){
         printf("Label -> SQUARE PID -> %d PPID -> %d\n", getpid(), getppid());
         int a;
         printf("Enter the side of the square: ");
         scanf("%d" ,&a);
         printf("Area of square is %d and perimeter is %d\n", (a*a), (4 * a));
      }else{
        wait(NULL);
      }
     
      return 0;
} 
