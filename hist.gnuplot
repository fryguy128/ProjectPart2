set term png
set output 'LaTex/histogram.png'
set xlabel "Distance from mean"
set ylabel "Hits at Distance"
set title "Histogram of distances from mean"
plot 'histData.txt' title ""
