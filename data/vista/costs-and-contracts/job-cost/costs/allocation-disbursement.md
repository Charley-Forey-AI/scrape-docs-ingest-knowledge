---
title: "Allocation Disbursement | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/allocation-disbursement"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/allocation-disbursement"
---

# Allocation Disbursement

When processing cost allocations (in JC Process Cost Allocations), the system uses one of several formulas to calculate the disbursement to each specified job.
Disbursements are calculated using one of the following formulas:
Using Amount to AllocateBasis
Calculation

Cost
Job Cost ÷ Total Job Cost ´ Allocation Amount

Hours
Job Hours ÷ Total Job Hours ´ Allocation Amount

Revenue
Contract Revenue ´ Allocation Amount

Using Job Amount ColumnAllocation will be the flat amount designated for each job in the specified custom (user-defined) field. The 'Job Amount Column' in JC Allocation Codes is used to identify from which custom field in JC Jobs the allocation amount is pulled for each job.
Note: Custom fields are created via VA Custom Fields Wizard.
Using Allocation RateBasisCalculation
CostCost for Job x Allocation Rate
HoursHours for Job x Allocation Rate
RevenueContract Revenue ÷ Total Revenue ´ Allocation
 Amount

Using Job Rate ColumnAllocation will be a calculation of Cost for Job x the Allocation rate designated for each job in the specified custom memo field. The 'Job Rate Column' in JC Allocation Codes is used to identify from which custom field in JC Jobs the allocation rate is pulled for each job.
Example:
Type: Allocation Amount with Cost Basis
Month: 06/98
Allocation Code: 1 (applies to all jobs/departments)
Date: 06/31/98
Amount To Allocate: 15,000
The allocated amount of $15,000 is disbursed to all open jobs, based on the allocation setup. If there are three jobs with labor costs for the month of June--$20,000, $30,000, and $40,000, respectively--for a total of $90,000, the system will calculate the allocation for each job as follows:
Job #1
20,000

(20,000 / 90,000) x 15,000 = 3,333.33

Job #2
30,000

(30,000 / 90,000) x 15,000 = 5,000.00

Job #3
40,000

(40,000 / 90,000) x 15,000 = 6,666.67 *

Total Amount Allocated:
 $15,000.00

*  When necessary, the system rounds up the last calculation (in this
 case 6,666.666 to 6,666.67) to balance with the amount to allocate.
Note: If the basis is Revenue and
 multiple jobs point to the same contract, allocations will be
 charged to the phase/cost type specified, but only to the first job.
