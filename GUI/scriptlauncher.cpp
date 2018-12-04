#include "scriptlauncher.h"

ScriptLauncher::ScriptLauncher(QObject *parent) :
    QObject(parent)
{
}

void ScriptLauncher::launchScript(QString s, QString t)
{
    setbuf(stdout, NULL);
    QProcess * m_process = new QProcess;
    QStringList args;

    args << "C:/Users/MEI/ACT409/bin/color_transfer_simple.sh";
    printf("s : %s\n", s.toUtf8().data());
    printf("t : %s\n",t.toUtf8().data());
    m_process->start("C:/cmder/vendor/git-for-windows/usr/bin/bash.exe",args);
    if(!m_process->waitForStarted())
        printf("%s\n", m_process->errorString().toLocal8Bit().data());
    m_process->waitForFinished();
    QString output(m_process->readAll().data());
    printf("output : \n%s\n", output.toUtf8().data());
    printf("script end\n");
}
