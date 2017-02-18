#!/bin/bash
#rm /home/szyzyrek/CMR_tabs.temp;
guake -n 1032 -r KGRServer -e "bash -c \"cd $KREDITNETHOME/etc; ./startjms; java -Xrunjdwp:transport=dt_socket,address=8338,server=y,suspend=n -Dkgr.configuration.kgrserver=/home/szyzyrek/kgrserver.properties -jar ../gui/libs/internal/kgr-server.jar\""
guake -n NEW_TAB -r KGRWeb -e      "bash -c \"cd $KREDITNETHOME/etc; ./startKGRWeb; tail -f $KREDITNETHOME/data/log/KGRWebServer.log -f $KREDITNETHOME/data/log/catalina.out\""

