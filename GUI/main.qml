import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.4


import QtQuick.LocalStorage 2.0
import "Database.js" as JS


Window {
    id : pWindow
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")


    Label {
        id: l_newProject
        x: 100
        y: 103
        width: 75
        height: 25
        text: "New project"
    }


    TextField {
        id: textField
        x: 100
        y: 128
        width: 200
        height: 50
        focus : true
        placeholderText: "Enter Project Name"
    }

    Label {
        id: l_chooseIdol
        x: 100
        y: 188
        width: 75
        height: 25
        text: "Choose mode"
    }


    ComboBox {
        id: comboBox
        x: 100
        y: 213
        model: [ "Auto", "custom"]
        width: 400
        height: 50
    }


    Button {
        id: b_create
        x: 360
        y: 281
        width: 140
        height: 45
        text: qsTr("Create Project")
        property variant win;
        onClicked: { console.log("pressed")
            JS.dbQuit()
            JS.dbProjectSet(textField.text,
                            comboBox.currentIndex)
            JS.dbReadAll()

            if(JS.dbProjectMode() === 0){
                var component = Qt.createComponent("Form_Auto.qml");
                console.log("AUTO");
            }
            else{
                component = Qt.createComponent("Form_Custom.qml");
                console.log("else");
            }

            win = component.createObject()
            win.show();
        }
    }
}
