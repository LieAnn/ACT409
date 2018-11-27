
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

    header: Button{
        id: end_setting
        x: 510
        width: 120
        height: 45
        text: qsTr("end setting")
        onClicked: {
            if(JS.dbProjectMode()===1){
                var component = Qt.createComponent("SetColor.qml");
            }
            else
                component = Qt.createComponent("StandBy.qml");
            win = component.createObject()
            win.show();

        }

    }
    StackLayout  {
        id: swipeView
        anchors.fill: parent
        currentIndex: tabBar.currentIndex

        Page1Form {}


    }

    footer: TabBar {
        id: tabBar
        currentIndex: swipeView.currentIndex

                     TabButton {
                         text: qsTr("Import video")
                     }



    }
}
