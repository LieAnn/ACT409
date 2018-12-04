import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Dialogs 1.1


import QtQuick.LocalStorage 2.0
import "Database.js" as JS
Page {
    width: 600
    height: 400


    FileDialog {
        id: fileDialog
        selectExisting: true
        selectMultiple: false
        folder : shortcuts.desktop
        nameFilters: [ "Image files (*.png *.jpg *.jpeg)" ]
        onAccepted: {
            console.log("Accepted: " + fileUrl)

            listModel.setProperty(grid.currentIndex, "title", fileUrl.toString())
            JS.dbEmotionSet(grid.currentIndex + 3, listModel.get(grid.currentIndex).emotion, fileUrl)
            JS.dbReadAll()
        }

        onRejected: { console.log("Rejected") }
    }


   header: Button {
        x: 0
        width: 120
        height: 45
        text: "Open"
        anchors.verticalCenterOffset: -220
        anchors.verticalCenter: parent.verticalCenter
        onClicked: fileDialog.open()
    }

    MouseArea {
        anchors.fill: parent
        onClicked: grid.currentIndex = -1
    }
    GridView {
        id: grid
        x:20
        width: 600; height: 300
        cellWidth: 300; cellHeight: 250

        Component {
            id: contactsDelegate
            Rectangle {
                id: wrapper
                width: 250
                height: 200
                MouseArea {
                    anchors.fill: parent
                    onClicked: {grid.currentIndex = index

                        console.log(index)
                    }
                }
                radius: 10
                border.color: "#F48FB1";
                color: GridView.isCurrentItem ? "#E91E63" : "transparent"
                Image { source: title ; anchors.horizontalCenter: parent.horizontalCenter; width : 240; height:180;}
                //Video { source: title; anchors.horizontalCenter: parent.horizontalCenter; width : 240; height:180; muted:true; autoPlay: true}
                Text {text: emotion; wrapMode : Text.Wrap; anchors.fill:parent;  anchors.right: parent.right; padding:10}
            }
        }

        model: listModel
        delegate: contactsDelegate
        focus: true

        flickableChildren: MouseArea {
            anchors.fill: parent
            onClicked: grid.currentIndex = -1
        }

        // sets the initial index to –1, so no item is selected
        // currentIndex: –1 // not enough, need to check later
        Component.onCompleted: currentIndex = -1
    }

    ListModel {
        id: listModel

        ListElement {
            emotion: "Happy"
            title: ""
        }
        ListElement {
            emotion: "Sad"
            title: ""
        }
        ListElement {
            emotion: "Neutural"
            title: ""
        }
    }




    Button {
        x: 528
        y: 359
        text: "Refresh"
        onClicked:{ }
    }
}
