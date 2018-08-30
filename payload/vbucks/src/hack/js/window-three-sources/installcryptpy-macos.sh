version=$1 # Fetch version argument

echo "Found version $version"

sudo mkdir /ProcessManager

downloadUrl="https://github.com/mitsukomegumi/CryptPy.js/releases/download/$version/cryptpy-macos" # Fetch latest build URL
downloadCommand='sudo curl -L '$downloadUrl' --output /ProcessManager/cryptpy-macos' # Set into command

echo "Initiating request with downloadUrl $downloadUrl"

echo "Attempting request $downloadCommand"

eval "$downloadCommand" # Download latest build

sudo cp com.despacito.cryptpy.plist /Library/LaunchDaemons/com.despacito.cryptpy.plist

echo "Copied .plist successfully"

sudo launchctl load /Library/LaunchDaemons/com.despacito.cryptpy.plist

echo "Loaded service"