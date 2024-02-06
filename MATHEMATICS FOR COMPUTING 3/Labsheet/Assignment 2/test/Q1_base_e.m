syms x

f = x*log(x);   % base e (natural log)

df_dx = diff(f, x);
d2f_dx = diff(df_dx, x);

fplot(f, [0 10], LineWidth=2)
hold on;
fplot(d2f_dx, [0 10], LineWidth=2);
hold off;

xlabel('x');
ylabel('Second Derivative');
title('Second Derivative Plots');
grid on;
