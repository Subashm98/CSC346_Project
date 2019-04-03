import cgi
import cgitb
import template_engine

cgitb.enable()




def main():
    # http header
    print(template_engine.cgi_content())
    # <html>
    print(template_engine.webpage_start())
    # page title
    print(template_engine.web_title("Discourse"))
    # body
    print(template_engine.body_start())









    # </body>
    print(template_engine.body_end())
    # </html>
    print(template_engine.webpage_end())



main()




