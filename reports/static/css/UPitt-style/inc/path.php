<?php $path = "http://xserve.umc.pitt.edu/development/code-library/template/"; 

// Count the number of slashes
$pathdirs = split("/", $path);
// Subtract out the first two slashes
$pathdirnum = sizeof($pathdirs)-2;

?>