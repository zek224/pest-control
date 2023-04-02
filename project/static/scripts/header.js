const template = document.createElement('template');
template.innerHTML = 
`
  <link rel="stylesheet" href="../static/header.css"/>
  <header>
    <nav>
      <a href="/"id="header-logo"><img src="../static/images/vector.svg"></a>
      <a class="header-link" id="about" href="about">About</a>
      <a class="header-link" id="sign-in" href="signin">Sign in</a>
    </nav>
  </header>
`
document.body.appendChild(template.content);