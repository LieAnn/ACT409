#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include "scriptlauncher.h"
#include <QQmlContext>

int main(int argc, char *argv[])
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    ScriptLauncher launcher;
    QQmlContext *context = engine.rootContext();
    context->setContextProperty("scriptLauncher", &launcher);

    if (engine.rootObjects().isEmpty())
        return -1;

    return app.exec();
}
