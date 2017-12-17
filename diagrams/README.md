This directory contains the source files for diagrams in Microsoft Visio 2016 format. When modifying these files, make sure to keep them in sync with the contents of the `hugo/static/diagrams` repository by exporting the diagrams in PNG *and* SVG formats from Visio. (This is not done automatically because, well, that's hard.)

When exporting Visio diagrams as SVG:

- Uncheck the "Include Visio data" checkbox.
- Make sure that there are *no* margins. Margins will be removed when exporting to PNG, but are kinda-sorta preserved when exporting to SVG, resulting in inconsistencies between the two formats. This is especially subtle because (for some reason) the problem only shows up after postprocessing (intrinsic placeholder processing, specifically). **TODO**: investigate more and maybe try to cache this in an automated way.
- Manually edit the resulting file to add the proper `<?xml-stylesheet` font declaration.
