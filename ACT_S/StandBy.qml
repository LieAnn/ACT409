import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.LocalStorage 2.2
import "Database.js" as JS

ApplicationWindow {
    id: window
    visible: true
    width: 640
    height: 480
    title: JS.dbProjectName()

    BusyIndicator {
        id: busyIndicator
        x: 220
        y: 140
        width: 200
        height: 200
    }





}
