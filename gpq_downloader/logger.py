from qgis.core import Qgis, QgsMessageLog


def log(message: str, level_in: int = 0):
    if level_in == 0:
        level = Qgis.MessageLevel.Info
    elif level_in == 1:
        level = Qgis.MessageLevel.Warning
    elif level_in == 2:
        level = Qgis.MessageLevel.Critical
    else:
        level = Qgis.MessageLevel.Info

    QgsMessageLog.logMessage(str(message), "GeoParquet Downloader", level)
