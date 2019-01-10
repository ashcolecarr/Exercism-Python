import re


def parse_markdown(markdown):
    lines = markdown.splitlines()
    line_list = []
    in_list = False
    # Giving loop variable a more meaningful name.
    for line in lines:
        # Bundling the header matching into a single regex.
        line = re.sub('^(#+)\s(.*)', header_replace, line)

        list_match = re.match(r'\* (.*)', line)
        if list_match:
            # Removing unnecessary boolean variables and repeated code.
            line = '<li>{0}</li>'.format(list_match.group(1))
            if not in_list:
                in_list = True
                line = '<ul>' + line
        else:
            if in_list:
                line = '</ul>'
                in_list = False

        m = re.match('<h|<ul|<p|<li', line)
        if not m:
            line = '<p>{0}</p>'.format(line)

        # Using regex replace instead of matching.
        line = re.sub(r'(.*)__(.*)__(.*)', r'\1<strong>\2</strong>\3', line)
        line = re.sub(r'(.*)_(.*)_(.*)', r'\1<em>\2</em>\3', line)
        line_list.append(line)

    if in_list:
        line_list.append('</ul>')

    res = ''.join(line_list)
    return res


def header_replace(match):
    return '<h{0}>{1}</h{0}>'.format(len(match.group(1)), match.group(2))
