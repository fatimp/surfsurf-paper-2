#!/bin/sh

arrow_head="path 'M 0,0 l -15,-5  +5,+5  -5,+5  +15,-5 z'"

#montage ../images/fss-disk-3x3.png ../images/fss-disk-3x3-inset.png -tile 2x1 -geometry +0+0 tmp.png
#convert tmp.png -stroke black -strokewidth 3 -fill none -gravity center \
#        -draw "rectangle 900,750 1600,830" \
#        -draw "line 1600,830 2700,1200" \
#        -draw "line 1600,750 2700,100" \
#        -draw "fill black translate 2700,1200 rotate 20 scale 2,2 $arrow_head" \
#        -draw "fill black translate 2700,100 rotate -30 scale 2,2 $arrow_head" \
#        ../images/fss-disk-3x3-final.png

#montage ../images/fss-disk-7x7.png ../images/fss-disk-7x7-inset.png -tile 2x1 -geometry +0+0 tmp.png
#convert tmp.png -stroke black -strokewidth 3 -fill none -gravity center \
#        -draw "rectangle 900,750 1600,830" \
#        -draw "line 1600,830 2700,1200" \
#        -draw "line 1600,750 2700,100" \
#        -draw "fill black translate 2700,1200 rotate 20 scale 2,2 $arrow_head" \
#        -draw "fill black translate 2700,100 rotate -30 scale 2,2 $arrow_head" \
#        ../images/fss-disk-7x7-final.png

montage ../images/fss-blob-7x7.png ../images/fss-blob-7x7-inset.png -tile 2x1 -geometry +0+0 tmp.png
convert tmp.png -stroke black -strokewidth 3 -fill none -gravity center \
        -draw "rectangle 1350,1050 2350,1150" \
        -draw "line 2350,1150 2700,1200" \
        -draw "line 2350,1050 2700,100" \
        -draw "fill black translate 2700,1200 rotate 10 scale 2,2 $arrow_head" \
        -draw "fill black translate 2700,100 rotate -70 scale 2,2 $arrow_head" \
        ../images/fss-blob-7x7-final.png

montage ../images/fss-blob-3x3.png ../images/fss-blob-3x3-inset.png -tile 2x1 -geometry +0+0 tmp.png
convert tmp.png -stroke black -strokewidth 3 -fill none -gravity center \
        -draw "rectangle 1350,1050 2350,1150" \
        -draw "line 2350,1150 2700,1200" \
        -draw "line 2350,1050 2700,100" \
        -draw "fill black translate 2700,1200 rotate 10 scale 2,2 $arrow_head" \
        -draw "fill black translate 2700,100 rotate -70 scale 2,2 $arrow_head" \
        ../images/fss-blob-3x3-final.png
