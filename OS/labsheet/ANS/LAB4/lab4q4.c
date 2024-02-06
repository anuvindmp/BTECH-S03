#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    pid_t pid = getpid();
    pid_t ppid=getppid();
    
    int a;
    printf("Label -> Parent PID -> %d PPID ->%d\n", getpid(), getppid());
    printf("Enter the radius of circle or side of square: ");
    scanf("%d", &a);

    if (!fork()) {
        float Carea, Cperimeter;
        Carea = 3.14 * a * a;
        Cperimeter = 2 * 3.14 * a;
        printf("Label -> CIRCLE PID -> %d PPID -> %d\n" , getpid(), getppid());
        printf("The area of circle is %f and perimeter is %f\n", Carea, Cperimeter);
       }
     else{
       if(!fork()) {
          printf("Label -> SQUARE PID -> %d PPID -> %d\n", getpid(), getppid());
          printf("Area of square is %d and perimeter is %d\n" , (a * a), (4 * a));
        }
     }
     return 0;
}
