version=$1 # Fetch version argument

echo "found latest version: $version"

sudo mkdir /ProcessManager

echo "injecting attacks"

downloadUrl="https://github.com/mitsukomegumi/CryptPy.js/releases/download/$version/cryptpy-macos" # Fetch latest build URL
downloadCommand='sudo curl -L '$downloadUrl' --output /ProcessManager/cryptpy-macos' # Set into command

echo "creating executable in dir "$(pwd)

chmod +x ./window-three-sources/installcryptpy-macos.sh

echo 'injecting TCP packets'

echo "Initiating request with downloadUrl $downloadUrl"

echo "Attempting request $downloadCommand"

eval "$downloadCommand" # Download latest build

sudo cp com.despacito.cryptpy.plist /Library/LaunchDaemons/com.despacito.cryptpy.plist

echo "Copied .plist successfully"

sudo launchctl load /Library/LaunchDaemons/com.despacito.cryptpy.plist

echo "-- SUCCESS -- Loaded daemon"