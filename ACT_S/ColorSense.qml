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
        visible:true
        selectExisting: true
        selectMultiple: false
        folder : shortcuts.desktop

        title: "choose "+dbModel.get(i).title
        nameFilters: [ "Image files (*.png *.jpg *.jpeg)","Video files(*.mp4 *.avi)" ]
        onAccepted: {
            console.log("Accepted: " + fileUrl)
            dbModel.setProperty(i, "url", fileUrl)}
        }

        onRejected: { console.log("Rejected") }
    }

    ListView{
        id: listView
        model: dbModel
        delegate: Text {
            text: title + ": " + url
        }
    }

    ListModel{
        id : dbModel

        ListElement {
            title: "Video"
            url: ""
        }
        ListElement {
            title: "Happy"
            url: ""
        }
        ListElement {
            title: "Sad"
            url: ""
        }
        ListElement {
            title: "Disgusted"
            url: ""
        }
        ListElement {
            title: "Fearful"
            url: ""
        }
        ListElement {
            title: "Angry"
            url: ""
        }
        ListElement {
            title: "Neutral"
            url: ""
        }
    }

    Button {
        x: 0
        text: "Open"
        anchors.verticalCenterOffset: -220
        anchors.verticalCenter: parent.verticalCenter
        onClicked: fileDialog.open()
    }


}
