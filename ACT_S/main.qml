import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.LocalStorage 2.0
import QtQuick.Layouts 1.11

import "Database.js" as JS


ApplicationWindow {
    id: window
    visible: true
    width: 640
    height: 480
    title: qsTr("ACT")

    property alias textField: textField


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
        onClicked: {
            JS.dbQuit()
            JS.dbProjectSet(textField.text,
                            comboBox.currentIndex)
            JS.dbReadAll()
            var component = Qt.createComponent("HomeForm.qml");
            win = component.createObject()
            win.show();
        }


    }

}
