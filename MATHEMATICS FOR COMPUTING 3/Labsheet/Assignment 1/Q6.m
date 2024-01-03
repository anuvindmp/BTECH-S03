decay_constant_C14 = 0.0001212598;
percentage_reduction = input('Enter the percentage of C14 reduction in the fossil: ');
reduction_factor = percentage_reduction / 100;
age = -log(reduction_factor) / decay_constant_C14;
fprintf('The estimated age of the fossil is approximately %.2f years.\n', age);
