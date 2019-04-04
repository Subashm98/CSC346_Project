#! /usr/bin/env python3
import cgi
import cgitb

cgitb.enable()


def style():
    print("""
    <style>
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
        
        .row-space {
            justify-content: space-between;
        }
        
        .col-2 {
            width: calc((100% - 30px) / 2);
        }
        
        html {
            box-sizing: border-box;
        }
        
        * {
            padding: 0;
            margin: 0;
        }
        
        *, *:before, *:after {
            -webkit-box-sizing: inherit;
            -moz-box-sizing: inherit;
            box-sizing: inherit;
        }
        
        /* ==========================================================================
            #RESET
            ========================================================================== */
        /**
        * A very simple reset that sits on top of Normalize.css.
        */
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
        
        /**
        * Remove trailing margins from nested lists.
        */
        li > ol,
        li > ul {
            margin-bottom: 0;
        }
        
        /**
        * Remove default table spacing.
        */
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
        
        .bg-blue {
            background: #2c6ed5;
        }
        
        .bg-red {
            background: #fa4251;
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
        
        .label {
            font-size: 16px;
            color: #555;
            text-transform: capitalize;
            display: block;
            margin-bottom: 5px;
            margin-top: 5px;
        }
        
        .radio-container {
            display: inline-block;
            position: relative;
            padding-left: 30px;
            cursor: pointer;
            font-size: 16px;
            color: #666;
            user-select: none;
        }
        
        .radio-container input {
            position: absolute;
            opacity: 0;
            cursor: pointer;
        }
        
        .radio-container input:checked ~ .checkmark {
            background-color: #e5e5e5;
        }
        
        .radio-container input:checked ~ .checkmark:after {
            display: block;
        }
        
        .radio-container .checkmark:after {
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #ca3c23;
        }
        
        .checkmark {
            position: absolute;
            top: 50%;
            transform: translateY(-50%); 
            left: 0;
            height: 20px;
            width: 20px;
            background-color: #e5e5e5;
            border-radius: 50%;
        }
        
        .checkmark:after {
            content: "";
            position: absolute;
            display: none;
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
        

        /* ====================================================================
            Login div
            ====================================================================*/ 
        .imgcontainer {
            text-align: center;
            margin: 24px 0 12px 0;
        }
        
        img.avatar {
            width: 40%;
            border-radius: 50%;
        }
        
        .container {
            padding: 16px;
        }
        
        span.psw {
            float: right;
            padding-top: 16px;
        }
    
    
    
    </style>
    """)





def registerDiv():
    print("""
    <div class="wrapper wrapper--w680">
        <div class="card card-4">
            <div class="card-body">
                <h2 class="title">Become A Member</h2>
                <form method="POST" action=auth.py>
                    <div class="row row-space">
                        <div class="col-2">
                            <div class="input-group">
                                <label class="label">username</label>
                                <input class="input--style-4" type="text" name="user_name" required>
                            </div>
                        </div>
                        <div class="col-2">
                            <div class="input-group">
                                <label class="label">full name</label>
                                <input class="input--style-4" type="text" name="full_name" required>
                            </div>
                        </div>
                    </div>
                    <div class="row row-space">
                        <div class="col-2">
                            <div class="input-group">
                                <label class="label">Password</label>
                                <div class="input-group-icon">
                                    <input class="input--style-4 js-datepicker" type="password" name="password" required>
                                </div>
                            </div>
                        </div>
                        <div class="col-2">
                            <div class="input-group">
                                <label class="label">Gender</label>
                                <div class="p-t-10">
                                    <label class="radio-container m-r-45">Male
                                        <input type="radio" checked="checked" name="gender" required>
                                        <span class="checkmark"></span>
                                    </label>
                                    <label class="radio-container">Female
                                        <input type="radio" name="gender">
                                        <span class="checkmark"></span>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row row-space">
                        <div class="col-2">
                            <div class="input-group">
                                <label class="label">Email</label>
                                <input class="input--style-4" type="email" name="email" required>
                            </div>
                        </div>
                        <div class="col-2">
                            <div class="input-group">
                                <label class="label">Phone Number</label>
                                <input class="input--style-4" type="tel" placeholder = "xxx-xxx-xxxx" name="phone"  pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
                            </div>
                        </div>
                    </div>
                    <div class="p-t-15">
                        <button class="btn btn--radius-2 btn--blue" type="submit" name="regbtn">Register</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <br>

    """)

def loginDiv():
    print("""
    <br>
    <div class="wrapper wrapper--w680">
        <div class="card card-4">
            <div class="card-body">
                <h2 class="title">Login</h2>
                <form method="POST">          <!-- <form action="/action_page.php"> -->
                    <div class="imgcontainer">
                        <img src="https://raw.githubusercontent.com/Subashm98/CSC346_Project/master/pyScripts/selfcare_login_pic.png" alt="Avatar" class="avatar">
                    </div>
                
                    <div class="container">
                        <label for="uname" class="label">Username</label>
                        
                        <input type="text" class = "input--style-4" placeholder="Enter Username" name="uname" required>
                
                        <label for="psw" class="label">Password</label>
                        <input type="password" class = "input--style-4" placeholder="Enter Password" name="psw" required>
                        <button class="btn btn--radius-2 btn--blue" type="submit" name="logbtn">Login</button>
                    </div>
            
                </form>
            </div>
        </div>
    </div>
    <br>
    <br>
    """)


def loginPage():
    print("""
    <br>
    <br>
    <div class="page-wrapper bg-gra-02 font-poppins"> 
    """)

    loginDiv()
    registerDiv()


    print("""</div>""")


def main():
    print("<html>")
    print("<head>")
    print("<title>Discourse</title>")
    style()
    print("</head>")
    print("<body>")
    
    loginPage()
    #loginDiv()
    #registerDiv()
    print("</body>")
    print("</html>")
print("Content-Type: text/html;charset=utf-8")
print()
main()




