---
title: "Revenue/Cost Forecast Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options"
---

# Revenue/Cost Forecast Options

Using the Forecast tab in JC Company Parameters, you can define how the system will distribute contract revenue and costs. .
The contract forecasting feature in Job Cost allows
 you to distribute contract revenue and costs over the life of a job. The forecast
 options defined here will be used when initializing forecasts for a contract in JC
 Contracts or PM Contracts.

## Forecast Method

The forecast method identifies how you forecast revenue and costs. Options available are:

- None - Used if not using the forecasting feature or if you will be entering forecasts manually.

- Linear - Use to spread contract revenue or costs equally over the life of the contract.

- Curve - Use to spread contract revenue or costs in defined increments over the life of the contract. Incremental amounts are based on the forecast intervals and the percent complete expected at the end of each interval.

## Forecast Intervals

If you elect to use the 'Curve' forecast method for revenue and/or cost, you will need to define forecast intervals. Forecast intervals are used during initialization to determine the points in time during the life of the contract that revenue and/or costs must reach a certain percentage of the total expected revenue and/or cost. The exact points in time are determined by the number of intervals and the total contract months (that is, the projected completion date minus contract start month).
Note: For contracts with no projected completion date defined, the initialization form (JC Forecast Initialize/PM Forecast Initialize) provides the option to specify the number of months past the current month to forecast.
For example, say you have a 2-year contract, with a start month of 07/20 and a projected completion date of 06/30/22. You set the # of Forecast Intervals to 4. The system will divide the total contract months (24) by the number of intervals (4) to determine the interval months. For this contract, the interval months will be: 12/20, 06/21, 12/210, and 06/22.
If the total contract months is not equally
 divisible by the number of intervals, the extra months will be added to existing
 intervals until none remain. So, if our total contract months had been 26, the first
 two intervals would have included 7 months, and the last two intervals, 6 months.
 Therefore, the intervals would have occurred as follows: 01/21, 08/21, 02/22, and
 08/22.

## Interval Percent Complete

You can also initialize forecasts for potential projects if you are using potential projects in the Pre-Construction module.
The % Complete at end of each Interval fields define the percentage of revenue or cost that is expected to be complete at the end of each interval. The number of forecast intervals is assumed to include the final interval (i.e. the last month), so you will need to enter 1 less percentage than the total number of intervals. For example, if you specify 4 intervals, enter only 3 percentages, placing a colon between each percentage (e.g. 25:50:75)
During initialization, the system will forecast the revenue and cost amounts for each month incrementally based on the total number of months, the forecast intervals, and the interval percent complete values. Monthly percent complete values for the months between intervals will depend on the number of months in each interval and the interval's percent complete value.
Example: Using the 2-year contract example from above:
# of Forecast Intervals: 4
% Complete at end of each interval: 25:50:75
Based on this setup, the first interval of 25% will fall on 12/20, the second interval of 50% will fall on 06/21, the third interval of 75% will fall on 12/21, and the last interval of 100% will fall on 06/22. To determine the percent complete for the remaining months, the system divides the interval percentage by the number of months in the interval. In our example, the first interval of 25% would be divided by 6 months (25.00 / 6 = 4.166, rounded to 4.17). The system then cumulatively adds that amount to each month. Therefore, the forecast percentages for the first 6 months would look like this:
07/204.17%
08/208.33%
09/2012.50%
10/2016.67%
11/2020.83%
12/2025.00%

The remaining months would be calculated in the same manner, except that the system uses the difference between interval percentages (rather than the interval percentage) in the calculation (e.g. 50% minus 25% equals 25%). So the remaining months would look like this:
01/2129.17%01/2279.17%
02/2133.33%02/2283.33%
03/2137.50%03/2287.50%
04/2141.67%04/2291.67%
05/2145.83%05/2295.83%
06/2150.00%06/22100.00
07/2154.17%
08/2158.33%
09/2162.50%
10/2166.67%
11/2170.83%
12/2175.00%

Once you have defined your forecast settings here,
 you can initialize forecasts for contracts in JC Forecast Initialize or PM Forecast
 Initialize (accessed from JC Contracts or PM Contracts, respectively).
Note: The settings defined here will also be used to initialize
 forecasts for potential projects in PC Potential Projects form. For more information
 about this form, see [About the PC Potential Projects Form](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-potential-projects-form).

[JC Contracts Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)
[PM Contracts Form](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form)
