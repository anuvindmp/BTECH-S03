syms x y(x);
ode = diff(y(x))-(cos(x)-cos(y(x))-y(x))/(x-x*sin(y(x)))==0;
cond = y(1) == 1;
%sol = dsolve(ode, cond);

x_values = 1:0.01:1.5;
%y_values = subs(sol, x, x_values);

%plot(x_values, y_values, '*r');
xlabel('x');
ylabel('y');

%ode45

initial_cond = 1;
[x,y] = ode45(@(x,y) (cos(x) - cos(y) - y) / (x - x*sin(y)),x_values,initial_cond);
hold on; plot(x,y,"*k");

%RK4
RK4(1,1,0.01,50);

%EulersMethod
EulerMethod(1,1,0.01,50);

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
end


function dydx = f(x, y)
    dydx = (cos(x)-cos(y)-y)/(x-x*sin(y));
end

