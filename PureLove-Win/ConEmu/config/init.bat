:: Init Script for cmd.exe
:: Init Script for powershell.exe
:: Sets some nice defaults
:: Created as part of PureLove project


:: Find root dir
@if not defined purelove_ROOT (
    for /f %%i in ("%ConEmuDir%\..\..") do @set purelove_ROOT=%%~fi
)

:: Change the prompt style
@prompt $E[1;32;40m$P$S{git}$S$_$E[1;30;40m{lamb}$S$E[0m

:: Pick right version of clink
@if "%PROCESSOR_ARCHITECTURE%"=="x86" (
    set architecture=86
) else (
    set architecture=64
)

:: Run clink
@"%purelove_ROOT%\base\clink\clink_x%architecture%.exe" inject --quiet --profile "%purelove_ROOT%\ConEmu\config"

:: Prepare for msysgit

:: I do not even know, copypasted from their .bat
@set PLINK_PROTOCOL=ssh
@if not defined TERM set TERM=cygwin

:: Enhance Path
@set git_install_root=%purelove_ROOT%\base\PortableGit
@set PATH=%purelove_ROOT%\bin;%git_install_root%\bin;%git_install_root%\mingw32\bin;%git_install_root%\usr\bin;%git_install_root%\cmd;%git_install_root%\share\vim\vim74;%PATH%
@set PYTHONPATH=%purelove_ROOT%\base\python\Lib\site-packages


:: Add aliases
@doskey /macrofile="%purelove_ROOT%\ConEmu\config\aliases"
