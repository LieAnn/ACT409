
import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.11

import QtQuick.Dialogs 1.1


import QtQuick.LocalStorage 2.0
import "Database.js" as JS



ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: JS.dbProjectName() + JS.dbProjectMode()

    function saveFile(fileUrl, text) {
        var request = new XMLHttpRequest();
        request.open("PUT", fileUrl, false);
        request.send(text);
        return request.status;
    }




    header: Button{
        id: end_setting
        x: 510
        width: 120
        height: 45
        text: qsTr("end setting")
        property string src : "";
        property variant win;
        onClicked: {


            JS.dbReadAll()
            JS.dbProjectVideo()
            textEdit.text =   '{"ProjectName":"'+JS.dbProjectName()
                    +'","ProjectMode":"'+JS.dbProjectMode()
                    +'","SourceFile":['+JS.dbFileId()
                    +']'
                    +',"VideoFile":"'+JS.dbProjectVideo()
                    +'"}'

            var component = Qt.createComponent("StandBy.qml");

            win = component.createObject()
            win.show();
        }

    }



    Label {
        id: textEdit
        anchors.fill: parent
        text:""

        visible: false
    }



    SwipeView {
        id: swipeView
        anchors.fill: parent
        currentIndex: tabBar.currentIndex

        // TODO: Move position bindings from the component to the Loader.
        //       Check all uses of 'parent' inside the root element of the component.
        Component {
            id: component_Page1Form
            Page1Form {
            }
        }
        Loader {
            id: loader_Page1Form
            sourceComponent: component_Page1Form
        }




    }

    footer: TabBar {
        id: tabBar
        currentIndex: swipeView.currentIndex

        TabButton {
            text: qsTr("Import Video")
        }

    }
}

