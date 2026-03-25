---
title: "Field Definitions: SM Departments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form/field-definitions-sm-departments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form/field-definitions-sm-departments-form"
---

# Field Definitions: SM Departments Form

The following is a list of field descriptions for the SM
 Departments form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Department

Enter a code to identify this Service Management department. Up to 10 characters allowed.

## Description

Enter a description of this department. Up to 30 characters allowed.

## GL Co

Enter the GL company (set up in GL Company Parameters) for this department. Initially defaults the GL Co specified in SM Company Parameters.
This company's GL accounts will be updated when processing work completed on work orders that reference this department (i.e. this department is assigned to a service center specified on a work order).

## Cost: Equipment

Required.
Enter the GL account to debit with costs incurred for equipment used on an SM work order associated with this department. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account once you post a work completed equipment line or when posting miscellaneous lines or purchase order items that reference an equipment cost type.
Note: The system will only use this account when the following conditions exist:

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

## Cost: Labor

Required.
Enter the GL account to debit with costs incurred for labor on an SM work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
For work completed labor lines, the system updates this account once you process payroll (in PR Payroll Process) and run PR Ledger Update. For work completed miscellaneous or purchase lines referencing a labor cost type, updates will occur when you post the miscellaneous line or process the purchase order batch.
Note: The system will only use this account when the following conditions exist:

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

## Cost: Other

Required.
Enter the GL account to debit when miscellaneous costs (e.g. trip charges, fuel surcharges, etc.) are incurred on an SM work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
For work completed miscellaneous or purchase lines referencing a cost type with this cost type category, updates will occur you post the miscellaneous line or purchase order batch (respectively).
Note: The system will only use this account when the following conditions exist:

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

## Cost: Material

Required.
Enter the GL account to debit with costs incurred for materials (stocked or purchased) on an SM work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account once you post the work completed inventory line. For work completed purchase lines referencing a material or a material cost type, an initial update to this account occurs when you receive the purchase order via PO Receipts Entry. Then when you post an invoice for the purchase order in AP Transaction Entry, the system backs out the original entries and creates new entries for the actual cost.
For work completed miscellaneous lines referencing a material cost type, updates will occur when you post the miscellaneous work completed line.
Note: The system will only use this account when the following conditions exist:

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

## Cost: Subcontract

Required.
Enter the GL account to debit with subcontract costs incurred on an SM work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you post work completed miscellaneous or purchase lines referencing a subcontract cost type.
Note: The system will only use this account when the following conditions exist:

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

## Cost: Burden

Required.
Enter the GL account to debit with burden costs incurred on an SM work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
For the burden portion of work completed labor lines, the system updates this account once you process payroll and run PR Ledger Update. However, this account will only be used when all of the following conditions are met:

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed. For more information, see the Cost Accounts topic in the SM Departments form help.

- No override Cost GL account is found (in SM Departments, Overrides tab) for the liability type associated with the work completed line.
Note: The amount debited to this account will depend on the rate type (E-Exactly as Payroll or R-Rate) specified for the work completed line's liability type on the Burden Rates tab (in SM Departments). If you did not define a burden rate for the liability type, no GL update for burden will occur.

## Revenue: Equipment

Required.
Enter the GL account to credit when billing work completed for equipment used on a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you create and interface an invoice for equipment usage to Accounts Receivable.
Note: This account will only be used if the following conditions exist:

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

## Revenue: Labor

Required.
Enter the GL account to credit when billing work completed for labor on a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you create and interface an invoice for labor costs to Accounts Receivable.
Note: This account will only be used if the following conditions exist:

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

## Revenue: Other

Required.
Enter the GL account to credit when billing miscellaneous work completed on a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you create and interface an invoice for "other" miscellaneous costs to Accounts Receivable. Other miscellaneous costs are those where the miscellaneous work completed line references a cost type with a cost type category of Other. Miscellaneous work competed lines that reference equipment, labor, subcontract, or material cost types will update the revenue accounts for the corresponding cost category.
Note: This account will only be used if the following conditions exist:

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

## Revenue: Material

Required.
Enter the GL account to credit when billing work completed for materials (stocked or purchased) used on a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you create and interface an invoice for material usage to Accounts Receivable.
Note: This account will only be used if the following conditions exist:

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

## Revenue: Subcontract

Required.
Enter the GL account to credit when billing miscellaneous work completed lines for subcontract costs on a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you create and interface an invoice for subcontract costs to Accounts Receivable.
Note: This account will only be used if the following conditions exist:

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

## Cost WIP: Equipment

Required.
Enter the GL account for tracking work in progress costs on equipment usage for an SM work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when posting work completed equipment lines or equipment-related miscellaneous or purchase lines that are associated with a call type that is tracking WIP.
Note: The system updates this account once you enter and save a work completed equipment line (in SM Work Orders, Work Completed tab). However, this account will only be used when all of the following conditions are met:

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked for the
 call type in SM Call Types).

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Cost account will be used, regardless of whether you are tracking WIP for the call type.)

## Cost WIP: Labor

Required.
Enter the GL account for tracking work-in-progress costs on labor for an SM work order.Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
For work completed labor lines associated with a call type that is tracking WIP, the system updates this account once you process payroll (in PR Payroll Process) and run PR Ledger Update. For work completed miscellaneous or purchase lines referencing a labor cost type, updates will occur when you post the miscellaneous line or process the purchase order batch.
Note: The system updates this account once you process payroll and run PR Ledger Update for work completed labor lines in SM Work Orders (Work Completed tab). However, this account will only be used when all of the following conditions are met:

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked for the
 call type in SM Call Types).

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Cost account will be used, regardless of whether you are tracking WIP for the call type.)

## Cost WIP: Other

Required.
Enter the GL account for tracking work-in-progress costs on miscellaneous items for an SM work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
For work completed miscellaneous or purchase lines associated with a call type that is tracking WIP and that reference a cost type with a cost type category of Other, updates will occur you post the miscellaneous line or purchase order batch (respectively).
Note: The system updates this account once you enter and save a work completed miscellaneous line (in SM Work Orders, Work Completed tab). However, this account will only be used when all of the following conditions are met:

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked for the
 call type in SM Call Types).

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Cost account will be used, regardless of whether you are tracking WIP for the call type.)

## Cost WIP: Material

Required.
Enter the GL account for tracking work-in-progress costs for materials (stocked and purchased) used on an SM work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
This account is updated once you post a work completed inventory line associated with call type that is tracking WIP.
For work completed purchase lines associated with a call type that is tracking WIP and that reference a material or a material cost type, an initial update to this account occurs when you receive the purchase order via PO Receipts Entry. Then when you post an invoice for the purchase order in AP Transaction Entry, the system backs out the original entries and creates new entries for the actual cost.
For work completed miscellaneous lines associated with a call type tracking WIP and that reference a material cost type, updates will occur when you post the miscellaneous work completed line.
Note: The system updates this account once you enter and save a work completed inventory or purchase line (in SM Work Orders). However, this account will only be used when all of the following conditions are met:

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked for the
 call type in SM Call Types).

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Cost account will be used, regardless of whether you are tracking WIP for the call type.)

## Cost WIP: Subcontract

Required.
Enter the GL account for tracking work-in-progress for subcontract costs incurred on an SM work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you post work completed miscellaneous or purchase lines associated with a call type that is tracking WIP and that reference a subcontract cost type.
Note: The system updates this account for miscellaneous work completed lines referencing a subcontract cost type (i.e. an SM cost type with a Subcontract cost type category). However, this account will only be used when all of the following conditions are met:

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked for the
 call type in SM Call Types).

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Cost account will be used, regardless of whether you are tracking WIP for the call type.)

## Cost WIP: Burden

Required.
Enter the GL account for tracking work-in-progress burden costs for an SM work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
For the burden portion of work completed labor lines associated with a call type that is tracking WIP, the system updates this account once you process payroll and run PR Ledger Update. However, this account will only be used when all of the following conditions are met:

- No override Cost WIP account is found (in SM Departments, Overrides tab) for the liability type associated with the work completed line.

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Cost Burden account will be used, regardless of whether you are tracking WIP for the call type.)
Note: The amount debited to this account will depend on the rate type (E-Exactly as Payroll or R-Rate) specified for the work completed line's liability type on the Burden Rates tab (in SM Departments). If you did not define a burden rate for the liability type, no GL update for burden will occur.

## Revenue WIP: Equipment

Required.
Enter the GL account for tracking equipment revenue on work in progress for a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you create and interface an invoice for work-in-progress equipment usage to Accounts Receivable. Once you close the related work order scope, the revenue WIP amounts are transferred to the equipment revenue account.
Note: The system updates this account once you bill a work completed equipment line in SM Work Orders (Work Completed tab). However, this account will only be used when the following conditions exist:

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked in SM
 Call Types).

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Revenue account will be used, regardless of whether you are tracking WIP for the call type.)

## Revenue WIP: Labor

Required.
Enter the GL account for tracking labor revenue on work in progress for a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you create and interface an invoice for work-in-progress labor to Accounts Receivable. Once you close the related work order scope, the revenue WIP amounts are transferred to the labor revenue account.
Note: The system updates this account once you bill a work completed labor line in SM Work Orders (Work Completed tab). However, this account will only be used when the following conditions exist:

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked in SM
 Call Types).

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Revenue account will be used, regardless of whether you are tracking WIP for the call type.)

## Revenue WIP: Other

Required.
Enter the GL account for tracking miscellaneous revenue on work in progress for a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you create and interface an invoice for work-in-progress "other" miscellaneous costs to Accounts Receivable. Once you close the related work order scope, the revenue WIP amounts are transferred to the Other miscellaneous revenue account.
Note: The system updates this account once you bill a work completed miscellaneous line in SM Work Orders (Work Completed tab). However, this account will only be used when the following conditions exist:

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked in SM
 Call Types).

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Revenue account will be used, regardless of whether you are tracking WIP for the call type.)

## Revenue WIP: Material

Required.
Enter the GL account for tracking stocked or purchased material revenue on work in progress for a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you create and interface an invoice for work-in-progress material usage to Accounts Receivable. Once you close the related work order scope, the revenue WIP amounts are transferred to the material revenue account.
Note: The system updates this account once you bill a work completed inventory or purchase line in SM Work Orders (Work Completed tab). However, this account will only be used when the following conditions exist:

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked in SM
 Call Types).

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Revenue account will be used, regardless of whether you are tracking WIP for the call type.)

## Revenue WIP: Subcontract

Required.
Enter the GL account for tracking subcontract revenue on work in progress for a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system updates this account when you create and interface an invoice for work-in-progress subcontract costs to Accounts Receivable. Once you close the related work order scope, the revenue WIP amounts are transferred to the subcontract revenue account.
Note: The system updates this account once you bill a work completed purchase line in SM Work Orders (Work Completed tab). However, this account will only be used when the following conditions exist:

- No override account is found (in SM Departments, Overrides tab) for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type associated with the work completed line.

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked in SM
 Call Types).

- The work order scope specified for the work completed line has a status of "Open". (If the work order scope's status is "Completed", the Revenue account will be used, regardless of whether you are tracking WIP for the call type.)

## Agreement: Revenue

Required.
Enter the GL account to credit when processing periodic billings (invoices) for service agreements. The account must be valid (set up in GL Chart of Accounts) with a subledger code of S-Service or blank.
The system updates this account when creating and interfacing invoices for an agreement that is set up to recognize revenue when billed

## Agreement: Deferred Rev

The Agreement: Deferred Rev field in SM Departments, Info tab.
Enter the GL account to credit when
 recognizing revenue for agreements using the S-Amortize or
 C-As Cost Incurred revenue recognition methods. The account must
 be set up in GL Chart of Accounts with the Subledger Code field set
 to S-Service or blank.

## Misc Offset Account: Cost

Misc Offset Account: Cost field on the SM Departments form, Info tab.
Required.
Enter the GL account to use as the offset account when posting miscellaneous work completed transactions. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
 When you post a miscellaneous work completed batch (manually or automatically), a single entry is posted to each line's transaction account (as defined in SM Departments), and one offsetting entry is posted to this account.

## Deferred Rev

Deferred Rev field under the Work Order section on the Info tab of the SM Departments form.
Enter the GL deferred revenue account to update when recognizing revenue (via
 SM Revenue Recognition) for customer work orders using the C-As Cost
 Incurred revenue recognition method. Press F4 for
 a list of valid GL accounts.

## Overrides: Seq

Enter + to add a new override sequence; the
 system will automatically assign the next sequential number.

## Overrides: Cost Type Category

Required.
Select the cost type category for which to define Cost, Revenue, Cost WIP and Revenue WIP GL accounts for this department.

- 1 - Equip

- 2 - Labor

- 3 - Other

- 4 - Material

- 5 - Subcontracts

Note: These categories correspond to the options available
 in the SM Cost Type
 Category drop-down in SM Cost Types. If you will be specifying a cost type
 for this override sequence, the cost type category specified here controls which cost types
 will be available for selection.

## Overrides: Burden

This field is enabled when you select the
 L-Labor cost type category and is set as null (blue-filled). Once you tab off the
 Cost Type
 Category field, the system sets this field to No (clears the checkbox).
Select this checkbox to apply this override
 to labor burden. Once selected, the Liability Type field is enabled, allowing
 Cost and Cost WIP GL account overrides by liability type, cost type, and/or call type.
Leave this checkbox unselected if this
 override does not apply to labor burden. The Liability Type field is disabled,
 allowing Cost, Revenue, Cost WIP, and Revenue WIP account overrides by cost type and/or
 call type only.

## Overrides: Liability Type

This field is only enabled when you select the L-Labor cost type category.
Enter the labor burden liability type for
 which to set up Cost and Cost WIP account overrides. Press F4 for a list
 of valid liability types (as set up in HQ Liability Types).
The system will only use the override accounts defined for this sequence if all of the following conditions are met:

-  The service center or division specified on the work order is assigned the department to which this override applies,

-  The cost type category for the work completed line matches the cost type category for this sequence and,

- The liability type is assigned to the earnings code associated with the work completed line. in other words, the earnings code assigned to the pay code specified for the work competed line must have at least one liability code that is assigned this liability type).

Note: If this override sequence also specifies a cost type and/or call type, the liability type, cost type, and/or call type must match the liability type, cost type, and/or call type specified here.

## Overrides: Cost Type

Enter the cost type for which you are setting up override GL accounts.
The cost type specified here must be assigned a cost type category (in SM Cost Types) matching the cost type category specified for the override sequence. The only exception is for override sequences assigned a cost type category of O-Other; in this case, any cost type can be entered, regardless of its cost type category.
The system will only use the override accounts defined for this sequence if all of the following conditions are met:

-  The service center or division specified on the work order is assigned the department to which this override applies,

-  The cost type category for the work completed line matches the cost type category for this sequence and,

- The work completed line references this call type.

Note: If this override sequence also specifies a liability type (labor burden only) and/or call type, the liability type (labor lines only), cost type, and/or call type associated with the work completed line must match the liability type, cost type, and/or call type specified here.

## Overrides: Call Type

Enter the call type for which you are setting up override GL accounts.
The system will only use the override accounts defined for this sequence if all of the following conditions are met:

-  The service center or division specified on the work order is assigned the department to which this override applies,

-  The cost type category for the work completed line matches the cost type category for this sequence and,

- The work completed line is for a scope assigned this call type.

Note: If this override sequence also specifies a liability type (labor burden only) and/or cost type, the liability type (labor lines only), cost type, and/or call type associated with the work completed line must match the liability type, cost type, and/or call type specified here.

## Overrides: Cost GL Account

Required.
Non-Burden Overrides
Enter the override GL account to debit when costs are incurred on a work order for the specified cost type category. For the labor cost type category, this applies to non-burden costs on a work order only. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system will only use this account when the following conditions exist:

- The service center or division specified on the work order is assigned this department and the work completed line is associated with the specified cost type category/call type/cost type, cost type category/cost type, or cost type category/call type.

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

Labor Burden Overrides
Enter the override GL account to debit when burden costs are incurred on a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system will only use this account for work completed labor lines when the following conditions exist:

- The service center or division specified on the work order is assigned this department and the work completed labor line is associated with the specified liability type, cost type, and/or call type.

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.
Note: The amount debited to this account will depend on the rate type (E-Exactly as Payroll or R-Rate) specified for the work completed line's liability type on the Burden Rates tab (in SM Departments). If you did not define a burden rate for the liability type, no GL update for burden will occur.

## Overrides: Revenue GL Account

This field is disabled when the Cost Type
 Category is L-Labor and the Burden checkbox is selected.
Required.
Enter the override GL account to credit when billing work completed on a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
Note: The system will only use this account when the following conditions exist:

- The service center or division specified on the work order is assigned this department and the work completed line is associated with the specified cost type category/call type/cost type, cost type category/cost type, or cost type category/call type.

- You are not tracking WIP for call types OR you are tracking WIP for call types and the work order scope has been closed.

## Overrides: Cost WIP GL Account

Required.
Non-Burden Overrides
Enter the override GL account for tracking costs on work in progress on a work order for the specified cost type category. For the labor cost type category, this applies to non-burden costs on a work order only. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
 The system will only use this account when the following conditions exist:

- The service center or division specified on the work order is assigned this department and the work completed line is associated with the specified cost type category/call type/cost type, cost type category/cost type, or cost type category/call type.

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked in SM Call
 Types).

Labor Burden Overrides
Enter the override GL account for tracking work-in-progress burden on a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
 The system will only use this account for work completed labor lines when the following conditions exist:

- The service center or division specified on the work order is assigned this department and the work completed labor line is associated with the specified liability type, cost type, and/or call type.

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked in SM Call
 Types).

## Overrides: Revenue WIP GL Account

This field is disabled when the Cost Type
 Category is L-Labor and the Burden checkbox is selected.
Required.
Enter the override GL account for tracking revenue on work in progress on a work order. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
Note: The system updates this account once you bill a work completed in SM Work Orders (Work Completed tab). However, this account will only be used when the following conditions exist:

- The service center or division specified on the work order is assigned this department and the work completed line is associated with the specified cost type category/call type/cost type, cost type category/cost type, or cost type category/call type.

- You are tracking WIP for the call type associated
 with the work completed line (i.e. the Track WIP box is checked in SM
 Call Types).

## Burden Rates: Liability Type

Enter the liability type for which to define a
 labor burden rate. Press F4 for a list of valid liability types
 (as set up in HQ Liability Types).
Note: You must define burden rates for each liability type that you will use for tracking labor burden. If you do not set up burden rates here, no GL update will occur.

## Burden Rates: Rate Type

Select the burden rate type for this liability type.

- E-Exactly as Payroll - Select this option to charge burden to SM work orders using the exact amount calculated in Payroll.

- R-Rate - Select this option to specify the rate to use when calculating burden for timecards posted to SM work orders.

## Burden Rates: Rate

Enabled only if you selected R-Rate as the
 Rate
 Type.
Enter the rate to use when calculating burden for this liability type.

## Seq

Seq field on SM Departments form, Standard Items tab.
Enter + to add a new standard
 item override sequence; the system will automatically assign the next sequential
 number.

## Standard Item

Standard Item field on the SM Departments form, Standard Items tab.
Enter the standard item for which to define an override offset GL account.

## Misc Offset GL Acct

Misc Offset GL Acct field on the SM Departments form, Standard Items tab.
Enter the override offset GL account for this standard item. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
When posting miscellaneous work completed lines that reference this standard item, the system will post one entry to the line's cost account and one offsetting entry to this account.
Note: During the posting process, if no override account is found for the specified standard item, the system uses the override account defined for the line's SM cost type. If an override account is not found for the cost type or if you did not specify a cost type for the work completed line, the system uses the standard miscellaneous offset account defined for the department (on the Info tab).

## Seq

Seq field on SM Departments form, Cost Types tab.
Enter + to add a new cost type
 override sequence; the system will automatically assign the next sequential number.

## Cost Type

Cost Type field on the SM Departments form, Cost Types tab.
Enter the SM cost type for which to define an override offset GL account or press
 F4
 to select from a list of valid SM cost types.

## Misc Offset GL Account

Misc Offset GL Acct field on the SM Departments form, Cost Types tab.
Enter the override offset GL account for this SM cost type. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
When posting work completed miscellaneous lines or work completed inventory lines for non-stocked materials that reference this cost type, the system will post one entry to the line's cost account and one offsetting entry to this account.
Note: For work completed miscellaneous lines that reference both a standard item and an SM cost type, the standard item override account is used instead of the cost type override account. The system will only use the cost type override account if the standard item does not have an override account defined.
