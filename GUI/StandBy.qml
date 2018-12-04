
import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.11

import QtQuick.Dialogs 1.1


import QtQuick.LocalStorage 2.0
import "Database.js" as JS


 ApplicationWindow{
     visible: true
     width: 640
     height: 480
     title: JS.dbProjectName() + JS.dbProjectMode()

     Button {
         x: 270
         y: 220
         text: "!!!CLICK ME!!!!"
         onClicked:  {
             console.log('File :' + JS.dbFileId())
             scriptLauncher.launchScript(JS.dbFileId(), JS.dbProjectVideo())
         }
     }


}
