:: Windows Batch Script for generating example results
:: Identical in structure to reproduce_results.sh version for linux
@echo off

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
set f=evm

:: S=Source, R=Results, MCR=MatlabCompilerRuntime
set SDIR=./data
set MCR=C:\Program Files\MATLAB\MATLAB Compiler Runtime\v80\runtime\win64

:: MCR path is preceded by any other path in system Path 
:: this prevents from other matlab or MCR installation from getting in the way
set PATH=%MCR%;%PATH%

set verNum=v80
set RDIR=Results

mkdir %RDIR%
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::----------------------------------------------------------
rem :: baby2.mp4 video with ideal_filter
rem set inFile=%SDIR%/baby2.mp4
rem call:printFun

rem %f% %inFile% %RDIR% 30 color 140/60 160/60 150 ideal 1 6

rem ::------------------------------------------------------------
rem :: camera.mp4, with butterworth filter
rem set inFile=%SDIR%/camera.mp4
rem call:printFun

rem %f%  %inFile% %RDIR% 300 motion 45 100 150 butter 0 20

rem ::------------------------------------------------------------
rem ::subway.mp4, with butterworth filter
rem set inFile=%SDIR%/subway.mp4
rem call:printFun

rem %f%  %inFile% %RDIR% 30 motion 3.6 6.2 60 butter 0.3 90

rem ::------------------------------------------------------------
rem :: shadow.mp4, with motion butterworth
rem set inFile=%SDIR%/shadow.mp4
rem call:printFun

rem %f%  %inFile% %RDIR% 30 motion 0.5 10 5 butter 0 48

rem ::------------------------------------------------------------
rem :: guitar.mp4, with two ideal filters
rem :: beware, ideal filters require at least 5GB of RAM
rem set inFile=%SDIR%/guitar.mp4
rem call:printFun

rem :: amplify E
rem %f%  %inFile% %RDIR% 600 motion 72 92 50 ideal 0 10

rem :: amplify A
rem %f%  %inFile% %RDIR% 600 motion 100 120 100 ideal 0 10


::------------------------------------------------------------
:: face.mp4, with ideal color filter
set inFile=%SDIR%/output.avi
rem call:printFun

%f%  %inFile% %RDIR% 30 color 40/60 120/60 50 ideal 1 4

rem ::------------------------------------------------------------
rem ::face2.mp4, with butterworth motion filter and color
rem set inFile=%SDIR%/face2.mp4
rem call:printFun

rem :: Motion
rem %f%  %inFile% %RDIR% 30 motion 0.5 10 20 butter 0 80

rem :: Color
rem %f%  %inFile% %RDIR% 30 color 50/60 60/60 50 ideal 1 6


:: printing helper Function, should NOT come before all others
rem :printFun
rem    echo Processing %inFile%
rem    echo.
goto:eof


:: MCR verNum:v80
:: MCR defaultPath: C:\Program Files\MATLAB\MATLAB Compiler Runtime\v80
