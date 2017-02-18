
pause
rem D:\lkd\komodo\w2_2\src\w2\wdbgc\apptools\env\src.bat
set ver=15.0.0.1014
d:
cd d:\rst
mkdir d:\rst\src_%ver%
cd d:\rst\src_%ver%
git clone git@repos.igk.intel.com:iRST
cd d:\rst\src_%ver%\iRST
git checkout %ver%