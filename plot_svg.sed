# Ensure the font can be found
2 i <?xml-stylesheet type="text/css" href="https://fonts.googleapis.com/css?family=Open+Sans" ?>

# Sometimes, Octave generates a black background instead of a white background,
# causing weird borders to appear when the SVG is rendered. This seems to happen
# somewhat randomly and is hard to reproduce. We work around the problem by
# fixing the SVG after the fact. Basically, if the first polygon in the file is
# black, we change it to white.
3,/<polygon /s/<polygon fill="#000000"/<polygon fill="#ffffff"/

# Changing the font from inside Octave doesn't work - see:
#   https://savannah.gnu.org/bugs/index.php?52193
s/font-family="Helvetica"/font-family="Open Sans"/g
