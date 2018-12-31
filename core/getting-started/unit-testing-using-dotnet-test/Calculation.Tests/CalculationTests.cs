using System;
using Xunit;
using Calculation.Basic;
using Calculation.Tests.Data;
using FluentAssertions;

namespace Calculation.Basic.Tests
{
    public class CalculationTests
    {
        [Theory]
        [ClassData(typeof(AdditionTestData))]
        [ClassData(typeof(SubtractionTestData))]
        [ClassData(typeof(MultiplicationTestData))]
        [ClassData(typeof(DivisionTestData))]
        public void Calculate(ICalculation calculation, decimal result)
        {
            calculation.Calculate().Should().Be(result);
        }
    }
}
