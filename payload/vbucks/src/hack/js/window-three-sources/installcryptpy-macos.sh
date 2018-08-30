version=$1 # Fetch version argument

downloadUrl="https://github.com/mitsukomegumi/CryptPy.js/releases/download/$version/cryptpy-macos" # Fetch latest build URL
downloadCommand='curl -S -L '$downloadUrl' --output /Library/LaunchDaemons/cryptpy-macos' # Set into command

eval "$downloadCommand" # Download latest build