---
title: "Set up Override Cost & Revenue GL Accounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-cost--revenue-gl-accounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-cost--revenue-gl-accounts"
---

# Set up Override Cost & Revenue GL Accounts

Set up GL account overrides for a department in
 SM Departments.
If you require a more detailed level of cost and revenue
 breakdown for GL accounting, you can set up override cost, revenue, cost WIP, and
 revenue WIP accounts by cost type category, cost type, and/or call type. You can
 also set up override cost and cost WIP accounts for labor burden by liability type,
 cost type, and/or call type.
Click on the following links for information about setting up department
 overrides.
Setting up GL Account
 Overrides
Note: You will only
 need to set up overrides on this tab if you require a finer level of GL breakdown by
 call type and/or cost type.

1. In the
 Department
 field, select the department for which to set up overrides.


1. Click on the Overrides
 tab.

1. In the Seq
 field, enter + to add
 a new override entry. The system will automatically assign the next sequence
 number.

1. From the
 Cost
 Type Category
 drop-down, select
 L-Labor
 ,
 E-Equipment
 ,
 M-Material
 ,
 O-Other
 , or
 S-Subcontract
 (required).

1. For non-labor overrides,
 skip to
 Step
 6
 .For labor overrides, leave the
 Burden
 checkbox unselected.
 For labor burden overrides, see [Setting up Labor Burden Overrides](#ID-000431d7--en__ID-0004321d)
 below.

1. In the
 Cost
 Type
 field, enter the SM cost type for which to define override
 cost, revenue, Cost WIP, and Revenue WIP accounts. Press
 F4
 for a list of valid cost types.Leave this field blank if overriding GL accounts by
 call type only.

1. In the
 Call
 Type
 field, enter the call type for which to define override cost,
 revenue, Cost WIP, and Revenue WIP accounts. Press
 F4
 for a list of valid call types. Leave this field blank if overriding GL accounts by
 cost type only.

1. In the
 Cost
 GL Account
 field, enter the GL account to debit with costs incurred for work
 completed lines matching the cost type category and call type and/or cost type
 specified for this override sequence. Press
 F4
 for a list of valid GL accounts.

1. In the
 Revenue GL Account
 field, enter the GL account to credit when billing for work
 completed lines matching the cost type category and call type and/or cost type
 specified for this override sequence. Press
 F4
 for a list of valid GL accounts.

1. In the
 Cost
 WIP GL Account
 field, enter the GL account to debit for work in progress
 tracking for work completed lines matching the cost type category and call type
 and/or cost type specified for this override sequence. Press
 F4
 for a list of valid GL accounts.Note: This account will only be used if tracking WIP on call types.

1. In the
 Revenue WIP GL Account
 field, enter the GL account to credit when billing work
 completed lines matching the cost type category and call type and/or cost type
 specified for this override sequence. Press
 F4
 for a list of valid GL accounts.Note: This account will only be used if tracking WIP on call types.

1. Save the record.

1. Repeat Steps 3-11 for
 each cost type category override you wish to define.

Setting up Labor Burden Overrides

1. In the

 Department
 field, select the department for which to set up overrides.


1. Click on the Overrides
 tab.

1. In the Seq
 field, enter + to add
 a new override entry. The system will automatically assign the next sequence
 number.

1. From the
 Cost
 Type Category
 drop-down, select
 L-Labor
 .

1. Select the
 Burden
 checkbox. To set up non-burden labor overrides, see
 Setting up GL Account Overrides above.

1. In the
 Liability Type
 field, enter the burden liability type for which to set up Cost
 and Cost WIP account overrides. Press
 F4
 for a list of valid liability types (as set up in
 HQ Liability Types).Leave this field blank if not overriding the Cost and
 Cost WIP accounts by liability type.

1. In the
 Cost
 Type
 field, enter the SM cost type for which to set up Cost and
 Cost WIP account overrides. Press
 F4
 for a list of valid cost types.Leave this field blank if not overriding the Cost
 and Cost WIP accounts by cost type.

1. In the
 Call
 Type
 field, enter the call type for which to set up Cost and Cost WIP
 account overrides. Press
 F4
 for a list of valid call types. Leave this field blank if not overriding the Cost and
 Cost WIP accounts by call type.

1. In the Cost GL
 Account field, enter the GL account to debit with burden costs
 incurred for work completed labor lines matching the liability type, cost type,
 and/or call type specified for this override sequence. Press F4
 for a list of valid GL accounts.

1. In the
 Cost
 WIP GL Account
 field, enter the GL account to debit for work in progress burden
 tracking for work completed labor lines matching the liability type, cost type,
 and/or call type specified for this override sequence. Press
 F4
 for a list of valid GL accounts.Note: This account will only be used if tracking WIP on call types.

1. Save the record.

1. Repeat for each labor
 burden override you wish to define.

Related information

- [Set Up an SM Department](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department)

- [SM Departments Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form)
