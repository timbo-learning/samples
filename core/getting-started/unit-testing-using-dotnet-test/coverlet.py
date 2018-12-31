import os

os.system("dotnet test")

primeFolder = "PrimeService.Tests"
calculationFolder = "Calculation.Tests"

primeBin = os.path.join(primeFolder   , 'bin', 'Debug', 'netcoreapp2.2', 'PrimeService.Tests.dll')
calculationBin  = os.path.join(calculationFolder , 'bin', 'Debug', 'netcoreapp2.2', 'Calculation.Tests.dll')

cmd = "coverlet %(bin)s" \
        + ' --exclude "[xunit.runner.*]*" ' \
        + '--target dotnet --targetargs "test %(folder)s --no-build" ' \
        + '--format lcov -o %(output)s'

print(cmd)
os.system(cmd % {
    'bin': primeBin,
    'folder': primeFolder,
    'output': 'prime.info'
    } )

os.system(cmd % {
    'bin': calculationBin,
    'folder': calculationFolder,
    'output': 'calculation.info'
    } )
