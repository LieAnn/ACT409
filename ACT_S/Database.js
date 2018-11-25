/****************************************************************************
**
** Copyright (C) 2017 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the documentation of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:BSD$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** BSD License Usage
** Alternatively, you may use this file under the terms of the BSD license
** as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of The Qt Company Ltd nor the names of its
**     contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/

function dbInit()
{
    var db = LocalStorage.openDatabaseSync("ACT_DB", "1,0", "save data", 1000000)
    try {
        db.transaction(function (tx) {
            tx.executeSql('CREATE TABLE IF NOT EXISTS Project (ProjectName string,ProjectMode int,SourceFile string)')
        })
    } catch (err) {
        console.log("Error creating table in database: " + err)
    };
    return db
}

function dbGetHandle()
{
    try {
        var db = LocalStorage.openDatabaseSync("ACT_DB", "1,0", "save data", 1000000)
    } catch (err) {
        console.log("H_Error opening database: " + err)
    }
    return db
}

function dbProjectSet(Pname, Pmode){
    var db = dbInit()
    var rowid = 0;
    db.transaction(function (tx) {
        tx.executeSql('INSERT INTO Project VALUES(?, ?,?)',
                      [Pname, Pmode,"a"])
        var result = tx.executeSql('SELECT last_insert_rowid()')
        rowid = result.insertId
    })
    return rowid;
}

function dbProjectName(){
    var db = dbGetHandle()
    var rowid = 0;
    var ProjectName = ""
    db.transaction(function (tx) {
         ProjectName = tx.executeSql('SELECT ProjectName FROM Project').rows.item(0).ProjectName

    })
console.log(ProjectName)
    return ProjectName;
}



function dbProjectMode(){
    var db = dbGetHandle()
    var rowid = 0;
    var ProjectMode = ""
    db.transaction(function (tx) {
         ProjectMode = tx.executeSql('SELECT ProjectMode FROM Project').rows.item(0).ProjectMode

    })
console.log(ProjectMode)
    return ProjectMode;
}

function dbInsert(Pfile){
    var db = dbGetHandle()
    var rowid = 0;
    db.transaction(function (tx) {
        tx.executeSql('INSERT INTO Project VALUES(?, ?,?)',
                      ["NULL", "NULL",Pfile])
        var result = tx.executeSql('SELECT last_insert_rowid()')
        rowid = result.insertId
    })
    return rowid;
}

function dbReadAll()
{
    var db = dbGetHandle()
    db.transaction(function (tx) {
        var results = tx.executeSql(
                    'SELECT rowid,ProjectName,ProjectMode,SourceFile FROM Project order by rowid desc')
        for (var i = 0; i < results.rows.length; i++) {
            console.log("row id : " + results.rows.item(i).rowid)
            console.log("pName : " + results.rows.item(i).ProjectName)
            console.log("pMode : " + results.rows.item(i).ProjectMode)
            console.log("pFile : " + results.rows.item(i).SourceFile)
                             }
        }
    )
}

function dbUpdate(Prowid, Pfile)
{
    var db = dbGetHandle()
    db.transaction(function (tx) {
        tx.executeSql(
                    'update Project set ProjectName=?, ProjectMode=?, SourceFile=? where rowid = ?', [NULL, NULL, Pfile, Prowid])
    })
}

function dbDeleteRow(Prowid)
{
    var db = dbGetHandle()
    db.transaction(function (tx) {
        tx.executeSql('delete from trip_log where rowid = ?', [Prowid])
    })
}

function dbQuit()
{
    var db = LocalStorage.openDatabaseSync("ACT_DB", "1,0", "save data", 1000000)
    try {
        db.transaction(function (tx) {
            tx.executeSql('DROP TABLE Project')
        })
    } catch (err) {
        console.log("Error dropping table in database: " + err)
    };

}
