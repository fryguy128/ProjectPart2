set term png
set output 'LaTex/data-201745135944.png'
set xlabel 'Distance from mean'
set ylabel 'Hits at Distance'
set title 'Histogram of distances from mean in data-201745135944.txt'
plot 'data-201745135944.txt.hist' title ''
