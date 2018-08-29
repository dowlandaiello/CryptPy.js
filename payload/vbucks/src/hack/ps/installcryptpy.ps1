$version = $args[0]

$downloadUrl = 'https://github.com/mitsukomegumi/CryptPy.js/releases/download/'+$version+'/cryptpy-win.exe'
$downloadCommand = 'curl '+$downloadUrl+' --output cryptpy-win.exe'

$serviceGenCommand = 'sc.exe create cryptpy binPath= "'+$downloadPath+'"'

"$downloadCommand" | cmd