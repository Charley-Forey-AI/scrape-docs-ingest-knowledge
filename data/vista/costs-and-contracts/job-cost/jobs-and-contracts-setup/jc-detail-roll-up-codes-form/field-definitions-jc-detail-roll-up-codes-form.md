---
title: "Field Definitions: JC Detail Roll-up Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form/field-definitions-jc-detail-roll-up-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form/field-definitions-jc-detail-roll-up-codes-form"
---

# Field Definitions: JC Detail Roll-up Codes Form

The following is a list of field descriptions for the JC
 Detail Roll-up Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Roll-up Code

Enter a code, up to 4 characters, to identify this roll-up.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form)JC Detail Roll-up Codes

## Roll-up Description

Enter a description for this roll-up, up to 25 characters.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form)JC Detail Roll-up Codes

## Summary Level

By Month
Leaves one record per month, per phase/cost type.
By Month/Source
Leaves one record per month, per phase/cost type, per source.
By Month/Source/Detail
For cost detail roll-ups only, summarizes detail as follows:

- AP = One record per vendor

- EM = One record per equipment

- MS = One record per material

- IN = One record per material

- PR = One record per payroll date

- JC = Compress only those transactions with nothing but units (e.g. transactions created in JC Progress Entry). All other JC transactions will not be compressed.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form)JC Detail Roll-up Codes

## Type

Specify the roll-up type.

- Cost – Select this option to roll-up cost detail.

- Revenue – Select this option to roll-up revenue detail.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form)JC Detail Roll-up Codes

## Jobs/Contracts

- All – Select this option to roll-up all jobs (cost detail roll-up) or contracts (revenue detail roll-up).

- Selected – Select this option to specify a job or range of jobs (cost detail) to roll up, or to specify a contract or range of contracts (revenue detail) to roll up. Job(s) or contract(s) are specified at the time you run JC Detail Rollup.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form)JC Detail Roll-up Codes

## Source

Specify from which source(s) to pull cost or revenue detail for roll-up. Valid sources are as follows:
Cost Detail

- AP (Transaction Entry)

- MS (Tickets)

- IN (Material Orders)

- PR (Timecards)

- AR (Misc Receipts)

- JC (Cost Adjustments, Progress Entry)

- EM (Revenue Adjustments)

Note: If summary level is month, all sources are disabled. If summary level is month/source, all sources are available. If summary level is month/source/detail, all sources except AR and JC are available.Revenue Detail

- AR (Receipts)

- JC (Revenue Adjustments)

Note: If summary level is month, all sources are disabled. If summary level is month/source, only AR and JC sources are available—all others are disabled. The month/source/detail summary level is not available for revenue roll-ups, therefore, all sources are disabled. except AR and JC are available. Select All
Click this button to set all sources to Y (checked). Boxes checked will depend on type of roll-up and available sources.
Clear All
Click this button to set all sources to N (unchecked).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form)JC Detail Roll-up Codes

## Closed Month Offset

Specify the number of months prior to the last month closed in subledgers through which to roll up cost or revenue detail.
For example, if you specify '12', and the last month closed in subledgers is 04/03, detail will be rolled up through 04/02.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form)JC Detail Roll-up Codes
