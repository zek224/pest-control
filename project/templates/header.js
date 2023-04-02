const template = document.createElement('template');
template.innerHTML = 
`
  <link rel="stylesheet" href="../static/header.css"/>
  <header>
    <nav>
      <button onclick="home.html"id="header-logo"><img src="../images/vector.svg"></button>
      <button class="header-link" id="about" onclick="parent.location='about.html'">About</button>
    </nav>
  </header>
`
document.body.appendChild(template.content);