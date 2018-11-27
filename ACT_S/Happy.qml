import QtMultimedia 5.8
import QtQuick 2.2
import QtQuick.Controls 2.2
import QtQuick.Dialogs 1.1
import QtQuick.Window 2.0
import QtQuick.LocalStorage 2.0
import QtQuick.Layouts 1.11

import "Database.js" as JS

Page{
    FileDialog {
        id: fileDialog
        selectExisting: true
        selectMultiple: false
        folder : shortcuts.desktop
        nameFilters: [ "Image files (*.png *.jpg *.jpeg)" ]
        onAccepted: {
            console.log("Accepted: " + fileUrl)
            JS.dbImageSet(fileUrl,1)
            image.source=fileUrl}

        onRejected: { console.log("Rejected") }
    }



    Button {
        x: 0
        text: "Open"
        anchors.verticalCenterOffset: -220
        anchors.verticalCenter: parent.verticalCenter
        onClicked: fileDialog.open()
    }

    Image {
        id: image
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        width: 600
        height: 400
        source: ""
    }

}

/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
