---
title: "About Contract Forecasts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/contracts/about-contract-forecasts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/contracts/about-contract-forecasts"
---

# About Contract Forecasts

Set up the cost and revenue forecast for a contract using
 Forecast tab in PM Contract.
The forecast for a contract defines, by month, the
 expected revenue, cost, and profit over the life of the contract. You can enter a
 forecast manually or initialize a forecast using JC Forecast Initialize (File > Forecast
 Initialize). Initialization will generate the forecast based on the forecast options
 you defined in JC Company Parameters and the contract's original and estimate amounts.
For example:
In JC Company Parameters, you set up the forecast
 options as shown below:

You then set up a contract with the following
 information:
Start Month: 01/21
Complete Date: 12/31/21
Original Contract: 3,580,000
Original Estimate: 1,350,000
Once initialized, the Forecast grid is
 populated with the entries as shown in the example below.
 In our example, note that the revenue forecast
 differs from the cost forecast. Since the revenue forecast uses the 'Curve' method,
 initialization generated revenue entries (highlighted area) based on the intervals and
 percentages defined for revenue in JC Company Parameters. The cost forecast is based on
 the 'Linear' method; therefore initialization distributed the contract's estimated costs
 equally over the life of the contract.
For additional information about how initialization
 utilizes the forecast options, see [Revenue/Cost Forecast Options](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options).
