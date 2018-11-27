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
                      [Pname, Pmode,""])
        var result = tx.executeSql('SELECT last_insert_rowid()')
        rowid = result.insertId
    })
    return rowid;
}
function dbVideoSet(Pfile){
    var db = dbInit()
    db.transaction(function (tx) {
        tx.executeSql('update Project set SourceFile=? where rowid = ?', [Pfile, 0])
        var result = tx.executeSql('SELECT last_insert_rowid()')

    })

}

function dbImageSet(Pfile,rowid){
    var db = dbInit()
    var arr =  [' Happy','Sad','Angry','Suprised','Fearful','Disgusted']
    db.transaction(function (tx) {
        tx.executeSql('update Project set ProjectName=? SourceFile=? where rowid = ?', [arr[rowid-1],Pfile, rowid])
        var result = tx.executeSql('SELECT last_insert_rowid()')

    })

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


function dbProjectVideo(){
    var db = dbGetHandle()
    var rowid = 0;
    var ProjectVideo = ""
    db.transaction(function (tx) {
        ProjectVideo = tx.executeSql('SELECT SourceFile FROM Project').rows.item(0).SourceFile

    })
    console.log(ProjectVideo)
    return ProjectVideo;
}



function dbSFile(Prowid)
{
    var db = dbGetHandle()
    var SFile = ""
    try {
        db.transaction(function (tx) {
            var result = tx.executeSql('SELECT SourceFile FROM Project')
            var data = result.rows.item(Prowid)
            SFile = data.SourceFile
        })
    }catch (err) {
        console.log("Error creating table in database: " + err)
    };
    console.log(SFile)
    return SFile;
}



function dbInsert(PEmotion, Pfile){
    var db = dbGetHandle()
    var rowid = 0;
    db.transaction(function (tx) {
        tx.executeSql('INSERT INTO Project VALUES(?, ?,?)',
                      ["NULL", PEmotion,Pfile])
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


function dbFileId()
{
    var db = dbGetHandle()
    db.transaction(function (tx) {
        var results = tx.executeSql(
                    'SELECT rowid,SourceFile FROM Project order by rowid desc')
        listModel.clear();
        for (var i = 0; i < results.rows.length -1; i++) {
            listModel.append({
                                 id: results.rows.item(i).rowid - 1,
                                 title: results.rows.item(i).SourceFile,
                             
                             })
        }
    })
}





function dbDeleteRow(Prowid)
{
    var db = dbGetHandle()

    db.transaction(function (tx) {
        tx.executeSql('delete from Project where rowid = ?', [Prowid])
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
        console.log("Error dropping table Project in database: " + err)
    };

}
