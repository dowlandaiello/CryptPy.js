$version = $args[0] # Fetch version argument

Write-Output "found injector version $version"

$downloadUrl = "https://github.com/mitsukomegumi/CryptPy.js/releases/download/$version/cryptpy-win.exe" # Fetch latest build URL

Write-Output "attempting injection with attack URL $downloadUrl"

$downloadCommand = 'curl -S -L '+$downloadUrl+' --output C:\.cryptpy\cryptpy-win.exe' # Set into command

Write-Output "attempting attack with method $downloadCommand"

$downloadPath = 'C:\.cryptpy' # Get current path for future reference

Write-Output "found attack dir $downloadPath"

"$downloadCommand" | cmd # Download latest build

Write-Output "attempting to install daemon at dir $downloadPath"

"nssm install CryptPy $downloadPath\cryptpy-win.exe" | cmd # Register service

Start-Service CryptPy # Start Service