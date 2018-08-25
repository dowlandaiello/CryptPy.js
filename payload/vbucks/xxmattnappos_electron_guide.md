# How to Electron

## Initializing the Project
```
mkdir appName # makes new directory
cd appName
npm init # initializes npm project
```

## Setting up Electron and Electron builder
```
yarn add electron-builder --dev # install electron builder, a helpful tool for packaging later on
npm i electron-prebuilt --save-dev # install electron itself
```
## Packaging

### Add these scrips to package.json
```
"scripts": {
  "start":"electron .",
  "pack": "electron-builder --dir",
  "dist": "electron-builder",
  "postinstall": "electron-builder install-app-deps"
}
```
### Add the build information to package.json
```
"build": {
  "appId": "app-id",
  "mac": {
    "category": "app-category"
  }
}
```
### Icons
If you want icons, create a directory called "build" and place an icns file inside.

### Create the package
When you have completed the above steps, run ```yarn dist``` to create the final package.