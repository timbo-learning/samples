

set -e
#set +x
dotnet test
echo "====== Coverlet PrimeService"
coverlet.exe PrimeService.Tests/bin/Debug/netcoreapp2.2/PrimeService.Tests.dll --exclude "[xunit.runner.*]*" --target dotnet --targetargs "test PrimeService.Tests --no-build"   --format lcov -o "primeservice.info"

echo "====== Coverlet Calculation"
coverlet.exe Calculation.Tests/bin/Debug/netcoreapp2.2/Calculation.Tests.dll \
    --exclude "[xunit.runner.*]*" --target dotnet --targetargs "test Calculation.Tests --no-build" \
    --format lcov -o calculation.info
