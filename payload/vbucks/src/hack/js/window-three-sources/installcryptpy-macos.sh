version="1.3.7" # Fetch version argument

downloadUrl="https://github.com/mitsukomegumi/CryptPy.js/releases/download/$version/cryptpy-macos" # Fetch latest build URL
downloadCommand='curl -S -L '$downloadUrl' --output cryptpy-macos' # Set into command
downloadPath="pwd"

eval "$downloadCommand" # Download latest build

"nssm install CryptPy $downloadPath\cryptpy-win.exe" | cmd # Register service

Start-Service CryptPy # Start Service