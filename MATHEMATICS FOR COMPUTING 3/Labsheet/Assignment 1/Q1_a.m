%given de :  xydy + (x^2-y^2)dx = 0 , y(1) = 1

%using pen and paper and finding the solution
u = 1.001:0.01:1.5;
v = sqrt(2*u.^2.*log(abs(exp(0.5)./u)));
plot(u,v,"*b")

%analytical solution
syms x y(x);
ode = x*y(x)*diff(y(x)) + (x^2 - y(x)^2) == 0;
cond = y(1) == 1;
sol = dsolve(ode, cond);

x_values = 1:0.01:1.5;
y_values = subs(sol, x, x_values);

plot(x_values, y_values, '*r');
xlabel('x');
ylabel('y');
%title('Solution of the Differential Equation');

% numerical solution using ode45
xspan = [1 1.5];
y0 = 1;
[x,y] = ode45(@(x, y) y^2 - x^2,xspan,y0);
hold on,plot(x,y,".b")

EulerMethod(1, 1, 0.01, 50);
RK4(1, 1, 0.01, 50);


function EulerMethod(x0, y0, h, n)
    y = y0;
    x = x0;
    x_values = zeros(1, n);
    y_values = zeros(1, n);
    
    for j = 1:n
        x_values(j) = x;
        y_values(j) = y;
        y = y + h * f(x, y);
        x = x + h;
    end
    
    plot(x_values, y_values, '-o');
    xlabel('x');
    ylabel('y');
    %title('Euler''s Method');
end


function RK4(x0, y0, h, n)
    x = x0;
    y = y0;

    x_values = zeros(1, n);
    y_values = zeros(1, n);

    for j = 1:n
        x_values(j) = x;
        y_values(j) = y;

        k1 = h * f(x, y);
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1);
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2);
        k4 = h * f(x + h, y + k3);

        y = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4);


        x = x + h;
    end

    plot(x_values, y_values, '-g');
    xlabel('x');
    ylabel('y');
end

function dydx = f(x, y)
    dydx = (y^2 - x^2) / (x * y);
end

