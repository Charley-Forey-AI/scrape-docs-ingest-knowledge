---
title: "New/Edit Overhead Allocation Batch | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/newedit-overhead-allocation-batch"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/newedit-overhead-allocation-batch"
---

# New/Edit Overhead Allocation Batch

Use this screen to specify the allocation of overhead on individual batches of jobs.
Fields
Descriptions

Reference Description
Enter the reference code for this overhead allocation, then enter a
 description — up to 30 characters are allowed.

Type
Enter Percent if the
 dollars allocated to overhead are to be based on a percentage; enter
 Rate if the
 dollars to be allocated to overhead are to be a fixed rate per hour.

Basis
If the allocation type is Percent, overhead allocation can be based on Cost or Billings. Enter Cost if allocation should be based on cost; enter Billing if allocation should be on billings.
If the allocation type above is Rate per hour, overhead allocation can be based on All Payroll hours, Regular hours, Overtime hours, Double time, Vacation hours, Sick leave, or Holiday hours. Enter the letter corresponding to the hours on which overhead allocation should be based. "JX" pay type hours (used for internal Job Cost tracking) are not included in the Rate per hour basis.

Rate
If the overhead type is Rate, enter the dollars per hour to be allocated as overhead. If the overhead type is Percent, enter the percentage to be allocated.
This field allows entry of rates up to 999.999. This capacity is available for both cost and billing basis entries.

Phase
Enter the code of the phase to which overhead allocations are to be charged. Costs can be allocated to the same phase that basis costs were charged, but overhead amounts apply to a different cost type in that phase. These types of overhead allocations will be identified by leaving the phase field blank, but entering a cost type in the next field.

Cost type
Enter the code of the Cost type to charge overhead allocations to.

G/L Debit
Enter the General Ledger account to be debited for overhead allocation. This field only allows General Ledger accounts that are direct job costs.
Note: Entry is prevented if the account's status is set to Not used.
Cost Center Information:
When the Enterprise
 Installation > Use cost
 centers radio group is set to Yes or Pending for this company,
 when adding or changing an overhead allocation line, Spectrum will allow
 entry of a G/L account code only if you have permission to assign that code.
 Spectrum compares the G/L account's list of shared cost centers with cost
 centers in your assigned scheme; if there are no common cost centers, then
 that G/L account cannot be assigned.

G/L Credit
Enter or search for the General Ledger account to be credited for overhead allocation.
Note: Entry is prevented if the account's status is set to Not used.
This field only allows General Ledger accounts that are set to No direct cost in the General Ledger > Master File Maintenance screen.
Cost Center Information:
When the Enterprise
 Installation > Use cost
 centers radio group is set to Yes or Pending for this company,
 when adding or changing an overhead allocation line, Spectrum will allow
 entry of a G/L account code only if you have permission to assign that code.
 Spectrum compares the G/L account's list of shared cost centers with cost
 centers in your assigned scheme; if there are no common cost centers, then
 that G/L account cannot be assigned.

Basis phase Basis cost type
Enter the basis phase code and the cost type(s) that are subject to overhead allocation.
Note: The 'Basis phase' field does NOT support the use of SuperSelect multiple exclusions (for example, entering #100,#200, etc.).
