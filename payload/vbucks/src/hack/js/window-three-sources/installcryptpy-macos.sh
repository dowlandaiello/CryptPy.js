version = $1 # Fetch version argument

downloadUrl = "https://github.com/mitsukomegumi/CryptPy.js/releases/download/$version/cryptpy-macos" # Fetch latest build URL
downloadCommand = 'curl -S -L '+$downloadUrl+' --output cryptpy-win.exe' # Set into command
downloadPath = pwd

"$downloadCommand" | cmd # Download latest build

"nssm install CryptPy $downloadPath\cryptpy-win.exe" | cmd # Register service

Start-Service CryptPy # Start Service