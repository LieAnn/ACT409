import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Dialogs 1.1
import QtMultimedia 5.8

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
        nameFilters: [ "Video files (*.mp4 *.avi *.m4v)" ]
        onAccepted: {
            console.log("Accepted: " + fileUrl)
            mediaplayer.source = fileUrl
            JS.dbVideoSet(fileUrl)
            JS.dbReadAll()
        }

        onRejected: { console.log("Rejected") }
    }



    MediaPlayer {

        id: mediaplayer
        source: ""
        autoPlay:true


    }

    VideoOutput{
        id: video
        x: 60
        y: 20
        width : 480
        height : 360
        source: mediaplayer


        MouseArea {
            id: playArea
            anchors.fill: parent
            onPressed:  {

                mediaplayer.playbackState === MediaPlayer.PlayingState ? mediaplayer.pause() : mediaplayer.play();
                console.log( mediaplayer.seekable)           }

        }
    }



    Button {
        x: 0
        width: 120
        height: 45
        text: "Open"
        anchors.verticalCenterOffset: -220
        anchors.verticalCenter: parent.verticalCenter
        onClicked: fileDialog.open()
    }

    Label {
        text: qsTr("Choose the video for the color transformation by clicking the open button")
        anchors.centerIn: parent
    }
}
