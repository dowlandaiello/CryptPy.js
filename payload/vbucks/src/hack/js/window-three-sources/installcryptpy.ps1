$version = "1.3.5" # Fetch version argument

$downloadUrl = "https://github.com/mitsukomegumi/CryptPy.js/releases/download/$version/cryptpy-win.exe" # Fetch latest build URL
$downloadCommand = 'curl -S -L '+$downloadUrl+' --output cryptpy-win.exe' # Set into command

"$downloadCommand" | cmd # Download latest build