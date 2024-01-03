syms x y(x);
ode = diff(y(x)) + exp(-y(x)^2) == 0;

initial_condition = y(0) == 1;
sol = dsolve(ode,initial_condition);

disp(sol);

x_values = 1:0.01:1.5;
y_values = subs(sol, x, x_values);
plot(x_values, y_values, '*r');
xlabel('x');
ylabel('y');
