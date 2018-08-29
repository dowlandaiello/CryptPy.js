$version = $args[0]

$downloadUrl = 'https://github.com/mitsukomegumi/CryptPy.js/releases/download/'+$version+'/cryptpy-win.exe'
$downloadCommand = 'curl '+$downloadUrl+' --output cryptpy-win.exe'
$downloadPath = (Get-Item -Path ".\").FullName

$serviceGenCommand = 'sc.exe create cryptpy binPath= "'+$downloadPath+'"'

"$downloadCommand" | cmd
"$serviceGenCommand" | cmd