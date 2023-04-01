const template = document.createElement('template');
template.innerHTML = 
`
  <link rel="stylesheet" href="../static/header.css"/>
  <header>
    <nav>
      <a href="home.html"id="header-logo"><img src="../images/vector.svg"></a>
      <a class="header-link" id="about" href="about.html">About</a>
      <a class="header-link" id="sign-up" href="signup.html">Sign up</a>
      <a class="header-link" id="sign-in" href="signin.html">Sign in</a>
    </nav>
  </header>
`
document.body.appendChild(template.content);