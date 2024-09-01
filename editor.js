let check = [true, true, true];
let htmlCode = document.getElementById("codeArea");
let cssCode = document.getElementById("codeAreaCSS");
let jsCode = document.getElementById("codeAreaJS");
let head = document.getElementById("head");

head.textContent = "HTML";
cssCode.style.display = "none";
jsCode.style.display = "none";
htmlCode.style.display ="block";
alert(`alt + z => deafult html syntax

shift + alt => render
  
control + enter => html/js switch
  
control + alt + enter => split display switch
    `);

function render() {
  let display = document.querySelector("#displayHTML");
  display.innerHTML =
    htmlCode.value.trim() +
    //`<script>${jsCode.value.trim()}</script>` +
    `<style>${cssCode.value.trim()}</style>`;

    let script = document.createElement("script");
    script.textContent = jsCode.value.trim();
    display.appendChild(script);
}

document.addEventListener("keydown", function (event) {
  if (event.shiftKey && event.altKey) {
    // Function for Shift + Enter
    render();
  } 
  else if (event.ctrlKey && event.code === "Enter" && !event.altKey && htmlCode.className === "codeArea") {
    console.dir(htmlCode);
    if (htmlCode.style.display === "block") {
      js();
      head.textContent = "JS";
    } else {
      html();
      head.textContent = "HTML";
    }
  }
  else if(event.ctrlKey && event.altKey && event.code === 'Enter')
    {
      if(htmlCode.className === "codeArea")
        {
          htmlCode.className = "splitDisplay";
          jsCode.className = "splitDisplay";
          htmlCode.style.display = "block";
          jsCode.style.display = "block";
          let br = document.querySelector("#splitDisplayBr");
          br.style.display = "block";
          htmlCode.rows = 11;
          jsCode.rows = 11;
          head.textContent = "HTML and JS";
        }
        else
        {
          reDoing();
          htmlCode.style.display = "block";
          jsCode.style.display = "none";
          let br = document.querySelector("#splitDisplayBr");
          br.style.display = "none";
          head.textContent = "HTML";
        }
    }
    else if(event.altKey && event.code === "KeyZ")
      {
        htmlCode.textContent = `<html>
   <head>
       <title></title>
   </head>
   <body>
   </body>
</html>`;
      }

});



htmlCode.addEventListener("click", function () {
  if (check[0] === true) {
    this.selectionStart = 0;
    this.selectionEnd = 0;
    check[0] = false;
  }
});
cssCode.addEventListener("click", function () {
  if (check[1] === true) {
    this.selectionStart = 0;
    this.selectionEnd = 0;
    check[1] = false;
  }
});
jsCode.addEventListener("click", function () {
  if (check[2] === true) {
    this.selectionStart = 0;
    this.selectionEnd = 0;
    check[2] = false;
  }
});


function css() {
  cssCode.style.display = "block";
  jsCode.style.display = "none";
  htmlCode.style.display = "none";
  head.textContent = "CSS";
  reDoing();
}

function html() {
  cssCode.style.display = "none";
  jsCode.style.display = "none";
  htmlCode.style.display = "block";
  head.textContent = "HTML";
  reDoing();
}

function js() {
  cssCode.style.display = "none";
  jsCode.style.display = "block";
  htmlCode.style.display = "none";
  head.textContent = "JS";
  reDoing();
}

function reDoing()
{
  htmlCode.className = "codeArea";
  jsCode.className = "codeArea";
  htmlCode.rows = 24;
  jsCode.rows = 24;
};