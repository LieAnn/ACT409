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
