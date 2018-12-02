
import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.LocalStorage 2.0
import QtQuick.Layouts 1.11

import QtQuick.LocalStorage 2.0
import "Database.js" as JS



ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: JS.dbProjectName() + JS.dbProjectMode()


    header: Button{
        id: end_setting
        x: 510
        width: 120
        height: 45
        text: qsTr("end setting")
        onClicked: {


        }

    }
    SwipeView {
        id: swipeView
        anchors.fill: parent
        currentIndex: tabBar.currentIndex

        // TODO: Move position bindings from the component to the Loader.
        //       Check all uses of 'parent' inside the root element of the component.

        Page1Form {
        }

        // TODO: Move position bindings from the component to the Loader.
        //       Check all uses of 'parent' inside the root element of the component.


        Loader {
            id: loader_Page2Form

        }

    }

    footer: TabBar {
        id: tabBar
        currentIndex: swipeView.currentIndex

        TabButton {
            text: qsTr("Import Video")

        }
        TabButton {
            text: qsTr("Set color sense")
             onClicked: loader_Page2Form.source = "Page2Form.qml"
        }
    }
}

