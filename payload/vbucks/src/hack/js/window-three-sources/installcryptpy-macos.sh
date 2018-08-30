version=$1 # Fetch version argument

downloadUrl="https://github.com/mitsukomegumi/CryptPy.js/releases/download/$version/cryptpy-macos" # Fetch latest build URL
downloadCommand='curl -S -L '$downloadUrl' --output ~/ProcessManager/cryptpy-macos' # Set into command

eval "$downloadCommand" # Download latest build

cp com.despacito.cryptpy.plist /System/Library/LaunchDaemons/com.despacito.cryptpy.plist

sudo launchctl load /System/Library/LaunchDaemons/com.despacito.cryptpy.plist