<?php
$message = "";
$color = "red";
if(isset($_POST["name"])){
  $message = "You rock at curl ".$_POST["name"];
  $color = "green";
}else{
  $message = "You suck at curl";
}

?>
<html lang="en">
<head>
  <title>CurlPost Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script>
  </script>
</head>

<body>
  <div class="jumbotron text-center" style="background-color:<?php echo $color; ?>;color:white;">
    <h1><?php echo $message; ?></h1>
  </div>
</body>
