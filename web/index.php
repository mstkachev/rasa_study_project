<!doctype html>
<html>
<head>
  <link rel="stylesheet" href="https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@master/dist/Chatroom.css" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial;}

/* Style the tab */
.tab {
    overflow: hidden;
    border: 1px solid #ccc;
    background-color: #f1f1f1;
}

/* Style the buttons inside the tab */
.tab button {
    background-color: inherit;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    transition: 0.3s;
    font-size: 17px;
}

/* Change background color of buttons on hover */
.tab button:hover {
    background-color: #ddd;
}

/* Create an active/current tablink class */
.tab button.active {
    background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
    display: none;
    padding: 6px 12px;
    border: 1px solid #ccc;
    border-top: none;
}
</style>
</head>
<body>
<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'Math')">Math</button>
  <button class="tablinks" onclick="openCity(event, 'Physics')">Physics</button>
  <button class="tablinks" onclick="openCity(event, 'IT')">IT</button>
</div>

<div id="Math" class="tabcontent"></div>
<div id="Physics" class="tabcontent"></div>
<div id="IT" class="tabcontent"></div>
<script language="javascript" type="text/javascript">

var timeout = setInterval(reloadTable, 500);    
function reloadTable () {

     $('#Math').load('one.php');
     $('#Physics').load('two.php');
     $('#IT').load('three.php');
}
</script>
<script>
function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
</script>
  <div class="chat-container"></div>

  <script src="https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@master/dist/Chatroom.js"/></script>
  <script type="text/javascript">
    var chatroom = new window.Chatroom({
      host: "http://34.78.63.207:5005",
      title: "Запись на сдачу",
      container: document.querySelector(".chat-container"),
      welcomeMessage: "Привет! Я - бот для записи на сдачи!"
    });
    chatroom.openChat();
  </script>
</body>
</html>



