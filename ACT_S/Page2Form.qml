import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Dialogs 1.1
import QtQuick.Layouts 1.1
import QtQuick.Window 2.0



Page {
    id: page
    width: 600
    height: 400

    FileDialog {
        id: fileDialog
        visible: fileDialogVisible.checked
        modality: fileDialogModal.checked ? Qt.WindowModal : Qt.NonModal
        title: fileDialogSelectFolder.checked ? "Choose a folder" :
                                                (fileDialogSelectMultiple.checked ? "Choose some files" : "Choose a file")
        selectExisting: fileDialogSelectExisting.checked
        selectMultiple: fileDialogSelectMultiple.checked
        selectFolder: fileDialogSelectFolder.checked
        nameFilters: [ "Image files (*.png *.jpg)", "All files (*)" ]
        selectedNameFilter: "All files (*)"
        sidebarVisible: fileDialogSidebarVisible.checked
        onAccepted: {
            console.log("Accepted: " + fileUrls)
            if (fileDialogOpenFiles.checked)
                for (var i = 0; i < fileUrls.length; ++i)
                    Qt.openUrlExternally(fileUrls[i])
        }
        onRejected: { console.log("Rejected") }
    }


    ScrollView {
        id: scrollView
        width: 600
        height: 355

        GridView {
            id: gridView

            contentHeight: 200
            contentWidth: 200
            cellWidth: 200
            cellHeight: 200
            delegate: Item {

                height: 100
                Column {
                    Rectangle {
                        width: 40
                        height: 40
                        Image {
                            anchors.fill: parent
                            source: "logo.png"
                        }
                        anchors.horizontalCenter: parent.horizontalCenter
                    }

                    Button {
                        text: emotion
                        anchors.verticalCenter: parent.up
                        anchors.horizontalCenter: parent.left
                        onClicked: fileDialog.open()
                    }
                    spacing: 5
                }
            }
            model: ListModel {
                ListElement {
                    name: "Grey"
                    emotion: "Happy"
                }

                ListElement {
                    name: "Red"
                    emotion: "Sad"
                }

                ListElement {
                    name: "Blue"
                    emotion: "Angry"
                }

                ListElement {
                    name: "Green"
                    emotion: "Suprised"
                }
                ListElement {
                    name: "Green"
                    emotion: "fearful"
                }
                ListElement {
                    name: "Green"
                    emotion: "disgusted"
                }


            }

        }
    }




}

/*##^## Designer {
    D{i:22;anchors_height:400;anchors_width:600;anchors_x:0;anchors_y:0}
}
 ##^##*/
