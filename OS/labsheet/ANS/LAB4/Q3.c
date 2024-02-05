#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#define PI 3.14159

// Function to calculate the area of a circle
double calculateCircleArea(double radius) {
return PI * radius * radius;
}

// Function to calculate the perimeter of a circle
double calculateCirclePerimeter(double radius) {
return 2 * PI * radius;
}

// Function to calculate the area of a square
double calculateSquareArea(double side) {
return side * side;
}

// Function to calculate the perimeter of a square
double calculateSquarePerimeter(double side) {
return 4 * side;
}

int main() {
double radius, side;

printf("Enter the radius of the circle: ");
scanf("%lf", &radius);

printf("Enter the side of the square: ");
scanf("%lf", &side);

// Fork a new process for circle calculations
pid_t circle_pid = fork();

if (circle_pid == 0) {
// Child process for circle calculations
double circle_area = calculateCircleArea(radius);
double circle_perimeter = calculateCirclePerimeter(radius);

printf("Circle Area: %.2lf\n", circle_area);
printf("Circle Perimeter: %.2lf\n", circle_perimeter);

// Exit the child process
exit(0);
} else if (circle_pid > 0) {
// Parent process

// Wait for the child process to finish
wait(NULL);
} else {
// Error in forking
perror("Error in forking");
exit(EXIT_FAILURE);
}

// Fork a new process for square calculations
pid_t square_pid = fork();

if (square_pid == 0) {
// Child process for square calculations
double square_area = calculateSquareArea(side);
double square_perimeter = calculateSquarePerimeter(side);

printf("Square Area: %.2lf\n", square_area);
printf("Square Perimeter: %.2lf\n", square_perimeter);

// Exit the child process
exit(0);
} else if (square_pid > 0) {
// Parent process

// Wait for the child process to finish
wait(NULL);
} else {
// Error in forking
perror("Error in forking");
exit(EXIT_FAILURE);
}

return 0;
}