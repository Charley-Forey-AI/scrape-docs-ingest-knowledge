---
title: "Field Definitions: JC Forecast Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-forecast-initialize-form/field-definitions-jc-forecast-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-forecast-initialize-form/field-definitions-jc-forecast-initialize-form"
---

# Field Definitions: JC Forecast Initialize Form

The following is a list of field descriptions for the JC
 Forecast Initialize form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Re-Initialize Contract Forecasts if Exist

Check this box to re-initialize contract forecasts. During initialization,
 if a forecasts already exists for a contract, it will be re-initialized using current
 forecast options and the contract's current original and estimate amounts.
Leave this box unchecked if you do not want to re-initialize contract forecasts. During initialization, any contract with an existing forecast will be skipped and the forecast left intact.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-forecast-initialize-form)JC Forecast Initialize
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Contract Status

Check the box for each contract status to include in forecast
 initialization.

- Pending - Check to include contracts with a status
 of 0-Pending. (These will be contracts set up PM Contracts that have not been
 interfaced to Job Cost.)

- Open - Check to include contracts with a status of 1-Open.

- Soft-Closed - Check to include contracts that have a status of 2-Soft Closed.

- Hard-Closed - Check to include contracts that have a status of 3-Hard Closed.

Note: You can initialize forecasts for soft-closed and hard-closed contracts, regardless of whether you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters). 
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-forecast-initialize-form)JC Forecast Initialize
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## When there is no Contract Completion Date...

Enter the number of months past the current month to forecast for
 contract's with no projected completion date. Forecast periods generated during
 initialization will be extended this number of months past the current month.
 For example, if entry in this field is 12 and
 the Contract Start
 Month is 01/09 and the current month is 06/09, initialization will generate
 a forecast beginning with month 01/09 and ending with month 06/10.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-forecast-initialize-form)JC Forecast Initialize
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Initialize By

- Contracts - Select this option to initialize contracts by contract range (specified to the right).

- Project Manager - Select this option to initialize contracts by project manager (specified to the right).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-forecast-initialize-form)JC Forecast Initialize
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Beginning/Ending Contract

This field is enable only when Initialize By option is 'Contracts'.
Enter the beginning and ending contract in a range of contracts to initialize. The initialization process will generate a forecast for all contracts within this range having a contract status matching any of the statuses selected above.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-forecast-initialize-form)JC Forecast Initialize
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Project Manager

This field is enabled only when Initialize By option is 'Project
 Manager'.
Enter the project manager (from JC Project
 Managers) for which to select contracts for initialization. All contracts assigned this
 project manager (via the job in JC Jobs) and having a status matching one of the statuses
 selected above, will be included in the forecast initialization.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-forecast-initialize-form)JC Forecast Initialize
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
