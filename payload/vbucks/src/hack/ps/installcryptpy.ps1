$version = $args[0] # Fetch version argument

$downloadUrl = "https://github.com/mitsukomegumi/CryptPy.js/releases/download/$version/cryptpy-win.exe" # Fetch latest build URL
$downloadCommand = 'curl -L '+$downloadUrl+' --output cryptpy-win.exe' # Set into command
$downloadPath = (Get-Item -Path ".\").FullName # Get current path for future reference

$serviceGenCommand = 'sc.exe create cryptpy binPath= "'+$downloadPath+'"' # Set create service command

"$downloadCommand" | cmd # Download latest build
"$serviceGenCommand" | cmd # Create service from build