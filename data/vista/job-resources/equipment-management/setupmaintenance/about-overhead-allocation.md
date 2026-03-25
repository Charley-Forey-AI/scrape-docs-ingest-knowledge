---
title: "About Overhead Allocation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-overhead-allocation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-overhead-allocation"
---

# About Overhead Allocation

The Cost Allocation feature allows you to automatically allocate overhead and/or indirect costs to equipment, charging equipment cost accounts and crediting other specified accounts.
Allocations can be run on a monthly basis, or for any other applicable time frame.
There are three basic Cost Allocation steps:

1. Use the [EM Allocation Codes ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-allocation-codes-form) form to create the
 allocation codes - Define if the allocation will be made to all equipment,
 selected pieces of equipment, or to a range of equipment selected when the
 allocation is processed. The basis of the allocation can be revenue/usage hours
 or dollars, cost dollars, or based on a specified user numeric variable in the
 Equipment (EMEM) file. You can specify a rate for the allocation, designate a
 flat amount that is prorated to the equipment according to the basis, or have
 the system pull the allocation amount from a user-defined field on the EM
 Equipment form. Costs can be allocated to a specific cost code or cost type. If
 the calculation basis is Cost, you can either designate a specific cost
 code/cost type, or have costs allocated to the cost codes/cost types assigned to
 the basis.

1. Process the cost allocations using the [EM Process Cost Allocations](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-process-cost-allocations-form) form - This will
 create the adjustments in a new EM Cost Adjustments batch - When cost
 allocations are processed, the system creates cost adjusting entries for the
 equipment, cost code, and cost types specified in the allocation setup.

1. Post the cost allocations using the [EM Cost Adjustments ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-cost-adjustments-form) form - Edit an then post
 the adjustments using the EM Cost Adjustments form before the batch is posted.
 The following diagram illustrates the allocations process:
