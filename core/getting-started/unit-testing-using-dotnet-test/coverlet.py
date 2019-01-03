#!/usr/bin/python3
import os

primeFolder = "PrimeService.Tests"
calculationFolder = "Calculation.Tests"

primeBin = os.path.join(primeFolder   , 'bin', 'Debug', 'netcoreapp2.2', 'PrimeService.Tests.dll')
calculationBin  = os.path.join(calculationFolder , 'bin', 'Debug', 'netcoreapp2.2', 'Calculation.Tests.dll')

cmd = "coverlet %(bin)s" \
        + ' --exclude "[xunit.runner.*]*" ' \
        + ' --target dotnet --targetargs "test %(folder)s --no-build" ' \
        + ' -o %(output)s' \
        + ' --format %(format)s' \
        # lcov to show lines on Visual Studio Code

os.system("dotnet test")

PrimeCmd = cmd % {
    'bin': primeBin,
    'folder': primeFolder,
    'output': 'prime.opencover.xml',
    'format': 'opencover'
    } 
print(">>>>" + PrimeCmd)
os.system(PrimeCmd)

CalculationCmd = cmd % {
    'bin': calculationBin,
    'folder': calculationFolder,
    'output': 'calculation.opencover.xml',
    'format': 'opencover'
    }
print(">>>>" + CalculationCmd)
os.system(CalculationCmd)
