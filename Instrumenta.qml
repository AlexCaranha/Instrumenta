import QtQuick 2.0
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import QtQuick.Window 2.0
import QtQuick.Dialogs 1.2
import QtQuick.Controls.Styles 1.1

ApplicationWindow {
id: root
width: Screen.width / 4
height: Screen.width / 8
title: "Instrumenta"
x: Screen.width / 2 - width / 2
y: Screen.height / 2 - height / 2

TextField {
id: txtSearch
x: 0
y: 0
placeholderText: "Search..."
width: parent.width
anchors.top: parent.y
focus: true
}

TableView {
id: table
x: 0
y: 25
width: parent.width
height: parent.height - txtSearch.height
anchors.bottomMargin: 0
anchors.bottom: parent.bottom

TableViewColumn { role: "options"; title: "Options"; width: table.width - 5; visible: false}
}
}
