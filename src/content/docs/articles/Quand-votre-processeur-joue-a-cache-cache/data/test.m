% Sample data
x = [1978, 1993, 1997, 1999, 2000, 2003, 2007, 2008, 2011, 2013, 2015, 2018, 2019, 2022, 2024];
y = [0.005, 0.05, 0.25, 1, 2, 2.5, 2.6, 3.2, 4, 4, 4.5, 4.7, 5, 5.3, 5.6];

% Create a scatter or line plot
scatter(x, y, 'filled');
hold on;

% Define text labels for each point
labels = {'Intel 8086', 'Intel Pentium', 'Intel Pentium 2', ...
    'AMD Athlon XP', 'Intel Pentium 4', 'AMD Athlon 64', 'AMD Phenom', ...
    'Intel Core i7 (Nehalem)', 'AMD Bulldozer', 'Intel Core I7 (Haswell)', ...
    'AMD Ryzen 3000', 'Intel Core i7 (Coffee Lake)', 'AMD Ryzen 7000', ...
    'Intel Core i7 (Alder Lake)', 'Intel Core i7 (Raptor Lake)'};

% Add text with a small offset so it does not overlap the marker
dx = 0.1; 
dy = 1.3;
hold on;
semilogy(x, y);
set(gca, 'YScale', 'log');
text(x + dx, y / dy, labels, 'Rotation', -90);
format bank;

ticks_val = [0.005, 0.01, 0.05, 0.1, 0.5, 1, 2, 3, 4, 5, 6];
ticks_str = {'0.005', '0.01', '0.05', '0.1', '0.5', '1', '2', '3', '4', '5', '6'};
yticks(ticks_val);
yticklabels(ticks_str);

grid on;
xlabel('Année');
ylabel('Fréquence (GHz)');
ylim([0.001, 10]);