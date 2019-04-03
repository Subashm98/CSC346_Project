#! /usr/bin/env python3
import cgi
import cgitb
cgitb.enable()


form = cgi.FieldStorage()


# style the html
def style():
        print("""
        <style>
        body {
                /* background-color: lightgray; */
                /* background-image: url("milkeyWay.jpeg"); */
                /* background-image: url("backgrounds-blank-blue-953214.jpg");
                background-image: url("backgrounds-blank-blue-953214.jpg"); */
                background-image: url("abstract-art-artistic-1020315_C2.jpg");
                margin: 0;
                padding: 0;     
        }



       

        nav{
                width : 100%;
                height: 20%;
                overflow: auto;

        }

        #userImg{
                width : 50px;
                height: 35px;
                margin: 5px 5px 0px 5px;
        }

        .navigation-bar{
                top: 0;
                width: 100%;
                position : fixed; 
        

        
        }



        #logo{
                width : 60px;
                height: 50px;
                margin: 0px 0px 0px 0px;
                padding:0;
        }



        #nav-ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color:#56ABE4;

        }
        
        #nav-ul li {
        /* float: left; */
                margin: 0 0 -10px 0;
        }

        #navLeft{
                float : left;
        }

        #navRight {
        float : right;
        }
        
        #nav-ul li a, label {
                display: block;
                color: white;
                text-align: center;

                padding: 14px 16px;
                text-decoration: none;
        }


        
        /* Change the link color to #111 (black) on hover */
        #nav-ul li a:hover {
                background-color: red;
        }
        </style>
        
        """)


def hNavBar():
        print("""
        <div class="navigation-bar">
                <nav>
                    <ul id = "nav-ul">
                            <li id = "navLeft"><img id = "logo" src="logo.png"></li>
                            <li id = "navLeft"><a href="index.html">Home</a></li>
                            <li id = "navLeft"><a href="news.asp">Add Post</a></li>
                            <li id = "navRight"><img id = "userImg" src="default_logImg.png"></li>
                                       
                             <li id = "navRight">
                                <label for="uname" class="label">Username</label>
                            </li>


                            
                    </ul>
                </nav>
                
        </div>
        """)


def main():
    print("<html>")
    print("<head>")
    print("<title>Discourse</title>")
    style()
    print("</head>")
    print("<body>")
    hNavBar()
    
    #loginDiv()
    #registerDiv()
    print("</body>")
    print("</html>")
print("Content-Type: text/html;charset=utf-8")
print()
main()


