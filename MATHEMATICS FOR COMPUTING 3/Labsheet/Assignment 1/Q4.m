    dydx = @(x, y) -(3*exp(x*y)+x)/exp(x);
    xspan = [1 1.5];
    y0 = 1; 
    [xsol, ysol] = ode45(dydx, xspan, y0);
    plot(xsol, ysol);
    xlabel('x');
    ylabel('y');
    title('ODE Solution');