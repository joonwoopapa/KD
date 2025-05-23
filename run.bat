@echo off
echo [KD Prediction System Launcher]
echo ============================

REM Check if Docker is installed
where docker >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Docker is not installed or not in PATH
    echo Please install Docker Desktop from https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

REM Check if Docker is running
docker info >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Docker is not running
    echo Please start Docker Desktop and try again
    pause
    exit /b 1
)

echo Docker environment check passed!
echo Starting KD Prediction System...
echo.
echo Application will be available at: http://localhost:8501
echo Please copy and paste this URL into your browser
echo.

REM Run docker-compose
docker compose up

REM If docker-compose fails, try docker-compose (hyphenated version)
if %ERRORLEVEL% NEQ 0 (
    echo Trying alternative docker-compose command...
    docker-compose up
)

pause 