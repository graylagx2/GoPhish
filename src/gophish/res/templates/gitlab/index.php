<?php
session_start();

if (!$_SESSION['loaded'])
{
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
    	$ip = $_SERVER['HTTP_CLIENT_IP'];
	} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
	    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
	} else {
	    $ip = $_SERVER['REMOTE_ADDR'];
	}

	file_put_contents('ip.txt', $ip);
}

$_SESSION['loaded'] = true;
header('Location: gitlab.html');
exit
?>
