# Clean up after remark mangling quotes inside shortcodes.
# TODO: figure out a better way to handle this. https://github.com/wooorm/remark/issues/253
s/\{\{% figure “([^”]*)” %\}\}/{{% figure "\1" %}}/g

# Ensure that there is always a non-breaking space between a digit and a letter.
# This prevents line breaks between a number and its unit, e.g. "3 V".
# There can be false positives, e.g. in "-1.0 to 1.0", but this seems worthwhile nonetheless.
s/([[:digit:]]) ([[:alpha:]])/\1\xc2\xa0\2/g
