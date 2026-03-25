---
title: "About Contract Forecasts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-contract-forecasts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-contract-forecasts"
---

# About Contract Forecasts

You can set up the forecast for a contract using the Forecast
 tab in JC Contracts.
The forecast defines, by month, the expected
 revenue, cost, and profit over the life of the contract. You can enter a forecast
 manually or initialize a forecast using JC Forecast Initialize (File  >  Forecast
 Initialize). Initialization will generate the forecast based on the forecast options
 you defined in JC Company Parameters and the contract's original and estimate
 amounts.
 For example:
In JC Company Parameters, you set up the forecast
 options as shown below:
You then set up a contract with the following
 information:
Start Date: 01/01/21
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
Note: You can use the JC Backlog Forecast Drilldown report to
 show forecasted revenue, cost, and profit for up to 12 future months, allowing you to
 analyze and manage future backlog.
