<?php 
	include("variables.php");
	include("path.php");
	
	
	/* ------------------------------------------------------------------ 
		Find Relative Path
		
		Compares the number of slashes in the page's url to 
		the number of slashes in the root and returns the appropriate
		number of ../
		
		Example: <img src="<?php echo findRelativePath($currentPath);?>images/shared/as-newsletter-snapshot.jpg" alt="Snapshot" height="34" width="59" />
		
		Troubleshooting tip: If this isn't working, try declaring the 
		following: <?PHP global $currentPath; ?>
	   ------------------------------------------------------------------*/
	
	function findRelativePath ($callingPagePath){
	
		global $pathdirnum;
	
		$dirs = split("/", $callingPagePath);
		$dirnum = sizeof($dirs) - $pathdirnum;

		for($i=0; $i<$dirnum; $i++){
			$pathdirs = $pathdirs."../";
		}
		
		return $pathdirs;
		
	}

   	/* ------------------------------------------------------------------ 
		Header Switcher
		
		Uses the array declared in variables.php. If the string
		used for the key matches anything in the url, returns that
		key's value to be used in the file name
		
	   ------------------------------------------------------------------*/
	
	function headerSwitcher($callingPagePath) {
		$set = false;
		
		// Gets the global varaibles that are included in variables.php
		global $headers, $server, $path;
		
		$pathdirs = findRelativePath($callingPagePath);

		
		// Compares URL to headers array until it finds a match
		foreach($headers as $key => $value){
			if ( (strpos($server, $key)) ) { 
				// Includes the correct header file, as specified in the headers array in variables.php
				include($pathdirs."inc/headers/header-" . $value . ".php"); 
				$set = true;
			}
		}
		
		// If no match, set header to a default
		if ($set == false){include($pathdirs."inc/headers/header-main.php");}
	}
		
	
	
	/* ------------------------------------------------------------------ 
		Nav Switcher  -- Needs to be replaced
		
		
	   ------------------------------------------------------------------*/
	
	function navSwitcher(){
		include($path."inc/umc-nav.php"); 
	}
	
	
	
	
	/* ------------------------------------------------------------------ 
		Section Switcher (Page Title)
		
		Uses the array declared in variables.php. If the string
		used for the key matches anything in the url, returns that
		key's value to be used in the file name
		
	   ------------------------------------------------------------------*/
	
	function sectionSwitcher () {
		$set = false;
	
		// Gets the global variables
		global $server, $section;

		foreach($section as $key => $value){
			if ( (strpos($server, $key)) ) { 
				echo ($value); 
				$set = true;
			}
		}
		
		// If no match, set header to a default
		if ($set == false){echo ("Home Page Title");}
	}
	
	
	
	/* ------------------------------------------------------------------ 
		Sidebar Switcher
		
		Uses the array declared in variables.php. If the string
		used for the key matches anything in the url, returns that
		key's value to be used in the file name
		
	   ------------------------------------------------------------------*/
	
	function sidebarSwitcher ($callingPagePath) {
		
		// Gets the global variables
		global $sidebar, $path, $server;
		
		$pathdirs = findRelativePath($callingPagePath);
		
		// Compares URL to headers array until it finds a match
		foreach($sidebar as $key => $value){
			if ( (strpos($server, $key)) ) { 
				// Includes the correct header, as specified in the headers array in variables.php
				include($pathdirs."inc/sidebars/sidebar-" . $value . ".php"); 
				$set = true;
			}
		}
		
		// If no match, set header to a default
		if ($set == false){include($pathdirs."inc/sidebars/sidebar-main.php");}
	}
?>