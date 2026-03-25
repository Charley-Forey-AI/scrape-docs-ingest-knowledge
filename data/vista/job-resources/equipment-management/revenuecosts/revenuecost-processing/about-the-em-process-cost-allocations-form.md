---
title: "About the EM Process Cost Allocations Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-process-cost-allocations-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-process-cost-allocations-form"
---

# About the EM Process Cost Allocations Form

Use this form to perform cost allocations based on allocation parameters set up in EM Allocation Codes.
This is not a required part of Equipment
 Management processing — you should use this form only if you need to post additional
 overhead costs to equipment.
Once you have entered the allocation number,
 the screen displays information about the allocation based on the specified allocation
 setup (in EM Allocation Codes). This includes the equipment, departments, and categories
 to which the allocation applies, as well as the cost types on which you specified to
 base the allocation, the allocation amount or rate, and the cost code to which the
 allocation will be posted.
Because the parameters set up in EM
 Allocation Codes may differ, screen prompts in this program may also differ. For
 example, if you selected an individual piece of equipment, category, and/or department
 when you set up the allocation in EM Allocation Codes, this screen will prompt you to
 indicate the equipment, category, and/or department to process for the selected batch.
 Additionally, you can override the allocation amount or rate (depending on how you
 specified the allocation to be calculated).

- Cost Allocation Overview - Processing cost allocations is
 the part of the Cost Allocation feature. For more information, see the diagram
 in [Overhead Allocation](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-overhead-allocation).

- Before Running Allocations - Before you run this program,
 make sure you have interfaced all costs on which you are basing the allocation.
 If you perform an allocation and later discover you did not interface costs from
 other modules or the costs are not correct, it is suggested that you:

- Delete the cost adjusting entries created for the
 allocation using the EM Cost Adjustments program.

- Make sure you interface or enter all costs needed
 for the allocation in EM.

- Run the allocation again.

Each time you process an allocation, costs are calculated and posted.
 Re-running an allocation in the same month will not back out the previously
 allocated costs.

- Reversal - This option allows you to flag cost allocation
 transactions for reversal. If checked, the system will automatically flag all
 transactions generated during the allocation process as ‘1-Auto Reverse’. You
 can change the reversal status for transactions, if necessary, in EM Cost
 Adjustments. Allocations flagged for reversal will be included when initializing
 reversals in EM Initialize Reversals.

- Process Allocations - Read about processing allocations
 [here](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-processing-allocations#concept-1871--en__concept-1871).

Related information

- [About the EM Allocation Codes Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-allocation-codes-form)
