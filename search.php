
<html>

<head>

<body>
	<h1> Market Prediction Data </h1>

<?php

$searchterm = $_GET["search"];

// Connect to the database
$host = "localhost";
$username = "root";
$user_pass = "usbw";
$database_in_use = "test";

$mysqli = new mysqli($host, $username, $user_pass, $database_in_use);

if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

// Print all rows of the database
// $sql = "SELECT ID, ticker, growth, financial_returns, multiple, integrated_factor FROM stocks";
// $result = $mysqli->query($sql);
//
// if ($result->num_rows > 0) {
//
// 	while($row = $result->fetch_assoc()) {
// 		echo "ID: " . $row["ID"]. " Ticker: " . $row["ticker"]. " Growth: " . $row["growth"]. " Financial Returns: " . $row["financial_returns"]. " Multiple: " . $row["multiple"]. " Integrated factor: " . $row["integrated_factor"]."<br>";
// 	}
// }
// else {
// 	echo "0 results";
// }

// Search the database for a Ticker
echo "<h2> Find the stock info with matching ticker: ".$searchterm." </h2>";
$sql = "SELECT date, g, f, m, i, p, ticker FROM stocks2 WHERE ticker LIKE '%".$searchterm."%'";
$result = $mysqli->query($sql);

if ($result->num_rows > 0) {

	while($row = $result->fetch_assoc()) {
		echo "ID: " . $row["date"]. " Ticker: " . $row["ticker"]. " Closing Price: " . $row["p"]." Growth: " . $row["g"]. " Financial Returns: " . $row["f"]. " Multiple: " . $row["m"]. " Integrated factor: " . $row["i"]."<br>";
	}
}
else {
	echo "0 results";
}

$mysqli->close();
?>

</body>

</head>

</html>
