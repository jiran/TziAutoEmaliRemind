@echo off
set SCRIPT_NAME=TziAutoEmaliRemind.py

set OUTPUT_DIR=dist

set TITLE=TziAutoEmailRemind

pyinstaller --onefile --distpath %OUTPUT_DIR% --workpath build --specpath spec --name %TITLE% %SCRIPT_NAME%

if %ERRORLEVEL% EQU 0 (
    echo 打包成功! 生成的文件位于 %OUTPUT_DIR% 目录中.
) else (
    echo 打包失败! 请检查你的代码和 PyInstaller 配置.
)

pause
