---
title: "PM Forecast Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/contracts/pm-forecast-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/contracts/pm-forecast-initialize-form"
---

# PM Forecast Initialize Form

This form is used to initialize revenue and cost forecasts for
 a contract, and can be accessed by selecting File > Forecast
 Initialize from PM Contracts.

- Contract Status - This section allows you to specify the contracts to include in initialization based on their current status. Contracts with a pending status are those set up in PM Contracts that have not been interfaced to Job Cost. Open contracts are those set up directly in Job Cost or set up in PM and interfaced to Job Cost. Contracts with a soft-closed for hard-closed status may be initialized regardless of how you have set the 'post to closed jobs' options in JC Company Parameters.

- Additional Months to Forecast - If you are initializing forecasts for
 contracts that do not have a projected completion date, use the When there is
 no Contract Completion Date... field to indicate the number of
 months past the current month to initialize the forecast. For example, say the
 contract's start month is 01/09. The current month is 06/09 and you enter '12'
 in this field. Initialization generate a forecast beginning with 01/09 and
 ending with month 06/10.

- Initialize By - Use this section to select contracts for initialization. You can initialize by contract range or initialize all contracts assigned to a specific project manager. The system will initialize all contracts within the specified contract range or for the project manager that match the selected contract status(es).

- Re-Initialize Contract Forecasts - Use this option to re-initialize forecasts
 for contracts within the specified range. During initialization, if a forecast
 exists for a contract, the forecast will be re-initialized using the current
 forecast options. You will typically only use this option if the forecast
 options have changed or when the original or estimate amounts for a contract
 have changed. When you have finished entering criteria, click the Initialize button. The initialization process will generate
 forecasts for each contract based on the forecast options defined in [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form), the contract's original
 and estimate amounts, and the number of months in the contract's life cycle.
 Once initialization is complete, you can edit forecasts as necessary in PM
 Contracts (Forecast tab).

[](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form)PM Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options)Forecast Options
