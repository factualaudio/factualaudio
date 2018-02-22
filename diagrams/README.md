This directory contains the source files for diagrams. When modifying these files, make sure to keep them in sync with the contents of the `hugo/static/diagrams` repository by exporting the diagrams in PNG *and* SVG formats from Visio. (This is not done automatically because, well, that’s hard.) Currently, diagrams are drawn in two separate formats:

# Visio diagrams (.vsdx)

These diagrams are in Microsoft Visio 2016 format. When exporting Visio diagrams as SVG:

-   Uncheck the “Include Visio data” checkbox.
-   Make sure that there are *no* margins. Margins will be removed when exporting to PNG, but are kinda-sorta preserved when exporting to SVG, resulting in inconsistencies between the two formats. This is especially subtle because (for some reason) the problem only shows up after postprocessing (intrinsic placeholder processing, specifically). **TODO**: investigate more and maybe try to catch this in an automated way.
-   Manually edit the resulting file to add the proper `<?xml-stylesheet` font declaration.

# SketchUp diagrams (.skp)

These are 3D models in SketchUp 2017 format. To export a diagram:

1.  Open it in SketchUp.
2.  Hide/unhide elements depending on the specific diagram you wish to generate.
3.  Orient the camera to get the desired angle.
4.  Resize the window to achieve the desired aspect ratio.
5.  Export as PNG using the following options:
    -   Width: 2000 pixels
    -   Anti-alias enabled
    -   Transparent background enabled

Note that these diagrams are not exported in SVG because SketchUp is [too limited](https://help.sketchup.com/en/article/3000167#export-vector) when it comes to exporting in vector format.
