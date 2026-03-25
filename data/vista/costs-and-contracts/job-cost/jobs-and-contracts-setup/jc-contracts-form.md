---
title: "JC Contracts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form"
---

# JC Contracts Form

Use the JC Contracts form to set up contracts.
A contract is a way to designate how one or more jobs may be billed. Contracts are set up in Job Cost to provide the opportunity to link revenue that is posted to contracts to costs that are posted to jobs. Each job you set up in Job Cost must be given a contract number so that:

- you can create meaningful cost reports showing profitability on your jobs.

- the system can suggest amounts to bill in the Job Billing (JB) module based on work complete.

Information entered in the JC Contracts form automatically updates the PM Contracts form, as both forms share the same table/view (JCCM).

## Departments

Each contract must be assigned a department to identify the set of default GL accounts (from the Departments form) to which revenue and related job costs will be posted. Departments are initially assigned at the contract header level, and then defaulted for each item on the contract. You can override the default for each item as necessary.

## Contract Items

 A contract item is a breakdown of the contract for billing purposes. Any piece of a contract that will be billed separately should be made a separate item. If the contract type is P (Progress), the items come from the schedule of values or bid items. If the contract type is T (Time & Materials), you may only need to set up one item.You can set up contract items using the Items tab or directly in the [JC Contract Items](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form) form, accessed by double-clicking in the Items tab.

## Resync Total Contract Amount

The Resync Total Contract Amount option (accessed from the File menu), allows you to resync a contract's amounts if for some reason they do not match the sum of the contract's item amounts. You should typically not need to use this feature, as these amounts are generally updated by the system automatically when adding estimates or posting costs.When you select this option, the system runs a process to sync the Total Orig. Contract and Total Curr Contract amounts (shown in the upper right corner of the form) with the sum of contract item original and current amounts (respectively).
If no adjustment was needed, the system displays a message stating, "Contract Amount is already in sync." If the totals are not in sync, the system updates the contract's totals accordingly and displays a message stating, "Contract amount has been synced. The values for Original Contract Amount and Contract Amount have adjusted to be the sum of the items."

## JB Info

This tab is used to set up additional information about a contract for billing purposes, including specifying invoice formats and delivery methods for recipients. It is identical to the [JB Contract Info](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form) form, with both updating the JCCM table; therefore, data entered here will be updated to JB Contract Info and vice versa.

## JB Delivery History

The JB Delivery History tab allows you to track the delivery history for Progress and T&M invoices associated with the contract. This tab is display only, and shows you the delivery ID, bill month, bill number, the date the invoice was sent (delivered), delivery method, delivery status (Delivered or Failed), and the recipient, as well as the recipient's email and/or address information (depending on the delivery method).

## Forecasts

The Forecast tab allows you to manually set up forecasts for a job, defining by month, the expected revenue, cost, and profit over the life of the contract. You can also initialize forecasts (via File > Forcast Initialize), in which case the system uses the forecast options defined in JC Company Parameters to generate forecast data for the contract. To learn more, see [About Contract Forecasts](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-contract-forecasts) and [Revenue/Cost Forecast Options](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options).

## Field Tickets

Use the Field Tickets tab to create field tickets for contracts that will enable linking labor, material, and equipment costs related to specific work activity on a job, and facilitate owner billing. Once you create a field ticket, you can then reference that field ticket when entering timecards, equipment usage, AP invoices / unapproved invoices, material usage, and purchase orders for a job so that project costs can be linked and pre-approved for billing by the customer. For more information, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Customer POs

Use the Customer POs tab to enter customer purchase orders associated with the contract. If you are using the Field Tickets feature, any customer PO that you reference on a field ticket must first be set up here. If you are not using the Field Tickets feature, entries on this tab are informational only.

For more information about contracts, select the links below.
[Setting Maximum Retention Amounts for Contracts](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/setting-maximum-retention-amounts-for-contracts)
[JC Forecast Initialize Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-forecast-initialize-form)
[Close a Contract](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract)
[About Security Groups](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-security-groups)
