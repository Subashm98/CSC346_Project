#! /usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

def style():
        print("""
        <style>
        body {
                /* background-color: lightgray; */
                /* background-image: url("milkeyWay.jpeg"); */
                /* background-image: url("backgrounds-blank-blue-953214.jpg");
                background-image: url("backgrounds-blank-blue-953214.jpg"); */
                background-image: url("https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/abstract-art-artistic-1020315_C2.jpg");
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
       /* 
        #FONT
        */
        .font-robo {
            font-family: "Roboto", "Arial", "Helvetica Neue", sans-serif;
        }
        
        .font-poppins {
            font-family: "Poppins", "Arial", "Helvetica Neue", sans-serif;
        }
        
        /* 
            #GRID
        */
        .row {
            display: flex;
            flex-wrap: wrap;
        } 
        html {
            box-sizing: border-box;
        }
        
        * {
            padding: 0;
            margin: 0;
        }
        
        *, *:before, *:after {
            box-sizing: inherit;
        }
        
        body,
        h1, h2, h3, h4, h5, h6,
        blockquote, p, pre,
        dl, dd, ol, ul,
        figure,
        hr,
        fieldset, legend {
            margin: 0;
            padding: 0;
        }
        
        li > ol,
        li > ul {
            margin-bottom: 0;
        }
        
        table {
            border-collapse: collapse;
            border-spacing: 0;
        }
        
        fieldset {
            min-width: 0;
            border: 0;
        }
        
        button {
            margin-top: 5px;
            outline: none;
            background: none;
            border: none;
        }
        
        /* ==========================================================================
            #PAGE WRAPPER
            ========================================================================== */
        .page-wrapper {
            min-height: 100vh;
        }
        
        body {
            font-family: "Poppins", "Arial", "Helvetica Neue", sans-serif;
            font-weight: 400;
            font-size: 14px;
        }
        
        .bg-gra-01 {
            background: linear-gradient(to top, #fbc2eb 0%, #a18cd1 100%); 
        }
        
        .bg-gra-02 {
            background: linear-gradient(to right, #F45C43, #EB3349); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        
            
        } 
            
        /* ==========================================================================
            #WRAPPER
            ========================================================================== */
        .wrapper {
            margin: 0 auto;
        }
        
        .wrapper--w960 {
            max-width: 960px;
        }
        
        .wrapper--w780 {
            max-width: 780px;
        }
        
        .wrapper--w680 {
            max-width: 680px;
        }
        
        /* ==========================================================================
            #BUTTON
            ========================================================================== */
        .btn {
            display: inline-block;
            line-height: 50px;
            padding: 0 50px;
            transition: all 0.4s ease;
            cursor: pointer;
            font-size: 18px;
            color: #fff;
            font-family: "Poppins", "Arial", "Helvetica Neue", sans-serif;
        }
        
        .btn--radius {
            border-radius: 3px;
        }
        
        .btn--radius-2 {
        
            border-radius: 5px;
        }
            
        .btn--blue {
            background: #4272d7;
        }
        
        .btn--blue:hover {
            background: #2859c5;
        }
        
        
        /* 
            #FORM
        */
        input {
            outline: none;
            margin: 0;
            border: none;
            box-shadow: none;
            width: 100%;
            font-size: 14px;
            font-family: inherit;
        }
        
        .input--style-4 {
            line-height: 50px;
            background: #d2d4cb;
        
            box-shadow: inset 0px 1px 3px 0px rgba(0, 0, 0, 0.08);
        
            border-radius: 5px;
            padding: 0 20px;
            font-size: 16px;
            color: #666;
            transition: all 0.4s ease;
        }
        .input--style-5 {
            line-height: 50px;
            background: #d2d4cb;
            height: 100px;
            width: 500px;
            box-shadow: inset 0px 1px 3px 0px rgba(0, 0, 0, 0.08);
        
            border-radius: 5px;
            padding: 0 20px;
            font-size: 16px;
            color: #666;
            transition: all 0.4s ease;
        }
        
        .label {
            font-size: 16px;
            color: #555;
            text-transform: capitalize;
            display: block;
            margin-bottom: 5px;
            margin-top: 5px;
        }
        
        .input-group {
            position: relative;
            margin-bottom: 22px;
        }
        
        .input-group-icon {
            position: relative;
        }
        

        
        /* ==========================================================================
            #TITLE
            ========================================================================== */
        .title {
            font-size: 24px;
            color: #525252;
            font-weight: 400;
            margin-bottom: 40px;
        }
        
        /* 
            #CARD
        */
        .card {
            border-radius: 3px;
            background: #fff;
        }
        
        .card-4 {
            background: #fff;
            border-radius: 10px;
            box-shadow: 0px 8px 20px 0px rgba(0, 0, 0, 0.15);
        }
        
        .card-4 .card-body {
            padding: 57px 65px;
            padding-bottom: 65px;
        } 
	</style>
        
        """)

def hNavBar():
        print("""
        <div class="navigation-bar">
                <nav>
                    <ul id = "nav-ul">
                            <li id = "navLeft"><img id = "logo" src="https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/logo.png"></li>
                            <li id = "navLeft"><a href="index.html">Home</a></li>
                            <li id = "navLeft"><a href="news.asp">Add Post</a></li>
                            <li id = "navRight"><img id = "userImg" src="https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/default_logImg.png"></li>
                                       
                             <li id = "navRight">
                                <label for="uname" class="label">Username</label>
                            </li>


                            
                    </ul>
                </nav>
                
        </div>
        """)

def showPost():
    print("""
    <br>
    <br>
    <div class="wrapper wrapper--w680">
        <div class="card card-4">
            <div class="card-body">
                <h4 class="title">Add a Post hello this is a test to, this is a test, this is a test<h4>
            </div>
        </div>
    </div>
    <br>
    """)


def printPost():
    print("""
    <br>
    <br>
    <div class="page-wrapper bg-gra-02 font-poppins"> 
    """)
    for i in range(10):
    	showPost()

    print("""</div>""")




def main():
    print("<html>")
    print("<head>")
    print("<title>Discourse</title>")
    style()
    print("</head>")
    print("<body>")
    hNavBar()
    printPost()  
 # hNavBar()
    #showPost()
    #loginDiv()
    #registerDiv()
    print("</body>")
    print("</html>")
print("Content-Type: text/html;charset=utf-8")
print()
main()
