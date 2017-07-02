
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%
git clone https://github.intel.com/wmt/messenger

cd %proot%\%ver%%pst%\messenger
git checkout -b %ver%.DEVB

rem & C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src_messenger.bat