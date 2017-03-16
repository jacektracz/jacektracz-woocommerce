
pause
rem & D:\lkd\komodo\w2_2\dat\env\cpphy\src.bat
rem set ver=15.0.0.1012
rem set ver=15.1.0.9131
rem set ver=15.0.0.1000
rem set ver=14.8.0.9099

rem working
rem set ver=15.0.0.1002

rem set ver=15.0.0.1003

rem doesn't work
rem set ver=15.0.0.1005

rem doesn't exists 15.0.0.1006
rem set ver=15.0.0.1006

rem set ver=15.0.0.1007

rem don't work
rem set ver=15.0.0.1008


rem set ver=15.0.0.9001
rem set ver=15.0.0.9002
rem set ver=15.0.0.9002 doesn't exists

rem set ver=15.0.0.9001
rem set ver=15.0.0.9003 doesn't work

rem set ver=15.0.0.9004
rem set ver=15.0.0.9005
rem set ver=14.8.1.1043

rem set ver=15.0.0.9174
rem set ver=15.0.0.1012

rem set ver=15.0.0.9055
rem set ver=15.0.0.9056
rem set ver=15.0.0.9057
rem set ver=15.0.0.1013
rem set ver=15.0.0.9134
rem set ver=15.0.0.1016
rem set ver=15.0.0.9144
rem set ver=15.0.0.9117
rem set ver=15.0.0.9101
rem set ver=15.0.0.9176
rem set ver=15.1.0.9177


rem set ver=15.0.0.9200
rem set ver=15.0.0.1028
rem set ver=13.2.8.1000

rem set ver=14.8
rem set ver=mainline
rem set ver=15.0.0.1031
rem set ver=14.5.0.1033
rem set ver=15.0.0.9225
rem set ver=14.5.0.1032
rem set ver=15.0.0.9225
rem set pst=CODE

rem set ver=14.10.0.8069
rem set ver=14.8.4.1046
rem set ver=14.10.0.8079
rem set pst=CODE_MP

rem set ver=15.2.0.9021
rem set pst=CODE

rem set ver=15.0.0.8259
rem set pst=CODE_JT

rem set ver=15.0
rem set pst=CODE_15_MAIN

rem set ver=15.0.0.9181

rem set ver=14.10.0.1024
rem set pst=CODE


rem set ver=15.0.0.1024
rem set pst=CODE

rem set ver=15.2
rem set pst=CODE_MLN

rem set ver=15.0.0.9234
rem set pst=CODE

rem set ver=15.0
rem set pst=HSD4939347

rem set ver=15.0.0.9235
rem set pst=HSD4939347

rem set ver=mainline
rem set pst=SRTS4

rem set ver=15.0
rem set pst=HSDS279951

rem set ver=15.2
rem set pst=HSD1804279951

rem set ver=15.5
rem set pst=HSD1804279951

rem set ver=15.2.0.9096
rem set pst=.artifacts

rem set ver=15.2
rem set pst=.carmel.org

rem set ver=15.2.0.1005
rem set pst=.ahcis3s5

rem set ver=15.5
rem set pst=.mainline

rem set ver=15.5.0.1010
rem set pst=.artifacts

rem set ver=15.5.0.1011
rem set pst=.artifacts

rem set ver=15.5.0.9135
rem set pst=.artifacts2

rem set ver=prv-mburas155
rem set pst=.softremap

rem set ver=prv-mburas-sr-new-ptl
rem set pst=.03

rem set ver=prv-mburas155
rem set pst=.01

set ver=prv-swremap
set pst=.04

d:
cd d:\rst
mkdir d:\rst\src_%ver%%pst%
cd d:\rst\src_%ver%%pst%
git clone git@repos.igk.intel.com:iRST
cd d:\rst\src_%ver%%pst%\iRST
git checkout %ver%
git checkout -b %ver%.DEV

rem & D:\lkd\komodo\w2_2\dat\env\cpphy\src.bat