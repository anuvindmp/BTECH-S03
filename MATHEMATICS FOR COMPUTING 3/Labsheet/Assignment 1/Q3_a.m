syms x y(x);
ode = diff(y(x)) + (x*y(x) - x*y(x)^3) == 0;
sol = dsolve(ode);
disp(sol)
