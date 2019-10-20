def svg_contents(svg_link: str) -> str:
    '''
    A simple function to return the contents of an SVG file in a str format to
    be inserted into an HTML template

    Returns: str
    '''
    return ''.join([line for line in open(svg_link, 'r')])
