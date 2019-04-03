def cgi_content(type="text/html"):
	return('Content type: ' + type + '\n\n')

def webpage_start():
	return('<html>')

def webpage_end():
	return('</html>')

def web_title(title):
	return('<head><title>' + title + '</title></head>')

def body_start():
    return('<body>')


def body_end():
    return('</body>')