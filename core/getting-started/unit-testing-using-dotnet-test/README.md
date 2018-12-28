
## Coverlet First run

```
mkdir coverlet-output
coverlet.exe PrimeService.Tests/bin/Debug/netcoreapp2.2/PrimeService.Tests.dll --target dotnet --targetargs "test PrimeService.Tests --no-build" -o coverlet-output/
```

Output:
    Test run for C:\Users\rtimbo\source\repos\samples\core\getting-started\unit-testing-using-dotnet-test\PrimeService.Tests\bin\Debug\netcoreapp2.2\PrimeService.Tests.dll(.NETCoreApp,Version=v2.2)
    Microsoft (R) Test Execution Command Line Tool Version 15.9.0
    Copyright (c) Microsoft Corporation.  All rights reserved.

    Starting test execution, please wait...

    Total tests: 11. Passed: 11. Failed: 0. Skipped: 0.
    Test Run Successful.
    Test execution time: 1.5248 Seconds


    Calculating coverage result...
      Generating report 'coverlet-output\coverage.json'
    +--------------------------------------------------+--------+--------+--------+
    | Module                                           | Line   | Branch | Method |
    +--------------------------------------------------+--------+--------+--------+
    | PrimeService                                     | 100%   | 100%   | 100%   |
    +--------------------------------------------------+--------+--------+--------+
    | xunit.runner.reporters.netcoreapp10              | 1.1%   | 0.5%   | 5.1%   |
    +--------------------------------------------------+--------+--------+--------+
    | xunit.runner.utility.netcoreapp10                | 15.7%  | 9.1%   | 21%    |
    +--------------------------------------------------+--------+--------+--------+
    | xunit.runner.visualstudio.dotnetcore.testadapter | 45.6%  | 35.7%  | 47.8%  |
    +--------------------------------------------------+--------+--------+--------+

    +---------+--------+--------+--------+
    |         | Line   | Branch | Method |
    +---------+--------+--------+--------+
    | Total   | 23.8%  | 18%    | 26.6%  |
    +---------+--------+--------+--------+
    | Average | 5.95%  | 4.5%   | 6.65%  |
    +---------+--------+--------+--------+

Output generated on coverlet-output/coverage.json

## dotnet test First Run

Under samples/core/getting-started/unit-testing-using-dotnet-test

```
$ dotnet restore
$ dotnet test
```

Output of the test was:

    $ dotnet test
    Build started, please wait...
    Skipping running test for project C:\Users\rtimbo\source\repos\samples\core\getting-started\unit-testing-using-dotnet-test\PrimeService\PrimeService.csproj. To run tests with dotnet test add "<IsTestProject>true<IsTestProject>" property to project file.
    Build completed.

    Test run for C:\Users\rtimbo\source\repos\samples\core\getting-started\unit-testing-using-dotnet-test\PrimeService.Tests\bin\Debug\netcoreapp2.2\PrimeService.Tests.dll(.NETCoreApp,Version=v2.2)
    Microsoft (R) Test Execution Command Line Tool Version 15.9.0
    Copyright (c) Microsoft Corporation.  All rights reserved.

    Starting test execution, please wait...

    Total tests: 11. Passed: 11. Failed: 0. Skipped: 0.
    Test Run Successful.
    Test execution time: 1.5296 Seconds

# Original README.MD

# Unit testing using dotnet test sample

This sample is part of the [unit testing tutorial](https://docs.microsoft.com/dotnet/core/testing/unit-testing-with-dotnet-test) for creating applications with unit tests included. See that topic for detailed steps on the code for this sample.

## Key features

This sample demonstrates creating a library and writing effective unit tests that validate the features in that library. The example provides a service that indicates whether a number is prime.

## Restore and test

To run the tests, navigate to the *PrimeService.Tests* directory and type the following commands:

```
dotnet restore
dotnet test
```

`dotnet restore` restores the packages of both projects.
`dotnet test` builds both projects and runs all of the configured tests.

[!INCLUDE[DotNet Restore Note](~/includes/dotnet-restore-note.md)]
