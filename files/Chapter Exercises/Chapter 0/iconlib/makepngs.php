<?php
function getfiles($dir, $ext="", $fullpath=true){
	$newfiles = array();
	$files = scandir($dir);
	foreach ($files as $file){
		if (substr($file, 0, 1) == ".") continue;
		if ($ext != "" && $ext != "*" && strtolower(file_extension($dir."/".$file)) != strtolower($ext)) continue;
		if ($fullpath){
			$newfiles[] = $dir."/".$file;	
		} else {
			$newfiles[] = $file;
		}
	}
	return $newfiles;

}

function file_extension($filename){
    $filename = explode(".", $filename);
    if (count($filename) == 1){return ""; } else {
		return $filename[count($filename)-1];
    }
}
function file_name($filename){
    return substr($filename, 0, strlen($filename)-4);
}
function imagesizestring($pngfile){
	list($width, $height, $type, $attr) = getimagesize($pngfile);
	return "{$width}x{$height}";
}

foreach (getfiles(".", "ico", false) as $file){
	$foldername = str_replace(".","_", file_name($file));
	if (!is_dir($foldername)){
		mkdir($foldername);
	}
	shell_exec("convert \"$file\" \"".file_name($file).".png\"");
	for ($i = 0; $i < 8; $i++){
		$pngname = file_name($file)."-".imagesizestring(file_name($file)."-$i.png").".png";
		rename(file_name($file)."-$i.png", $foldername."/".$pngname);
		echo "processed $pngname\r\n";
	}
	

}
?>