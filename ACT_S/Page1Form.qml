import QtMultimedia 5.8
import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.1
import QtQuick.Window 2.0
import QtQuick.LocalStorage 2.0
import QtQuick.Layouts 1.11

import "Database.js" as JS


Video {
    id: video
    width : 400
    height : 300
    source:  "sns.mp4"

    MouseArea {
        anchors.fill: parent
        onClicked: {
            video.play()
        }
    }
}


