
import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.LocalStorage 2.0
import QtQuick.Layouts 1.11

import "Database.js" as JS


ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: JS.dbProjectName()


    StackLayout  {
        id: swipeView
        anchors.fill: parent
        currentIndex: tabBar.currentIndex

        Page1Form {} Page2Form {}


    }

    footer: TabBar {
        id: tabBar
        currentIndex: swipeView.currentIndex

                     TabButton {
                         text: qsTr("Import video")
                     }
                     TabButton {
                         text: qsTr("select color sense")
                     }


    }
}
