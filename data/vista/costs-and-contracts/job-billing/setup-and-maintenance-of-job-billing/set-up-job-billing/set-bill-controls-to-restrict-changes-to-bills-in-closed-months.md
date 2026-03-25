---
title: "Set Bill Controls to Restrict Changes to Bills in Closed Months | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-bill-controls-to-restrict-changes-to-bills-in-closed-months"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-bill-controls-to-restrict-changes-to-bills-in-closed-months"
---

# Set Bill Controls to Restrict Changes to Bills in Closed
 Months

If you want to limit which of your users have permissions to
 add, edit, or delete bills in closed months, you can set Closed Month Bill Controls on the
 JB Company Parameters form.
These
 are optional settings that you can enable per JB Company. Bill control settings apply to
 both Progress and T&M bills.You will need to set up an HQ Role
 and assign users to it. You can either do this before enabling these bill control
 settings or while you configure them. For more information about setting up roles,
 see [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form).

1. Go to Job Billing > Programs > JB Company Parameters and select the Bill Control Options
 tab.

1. To restrict which users can create, edit, or
 delete bills in a closed JB month, select the Closed Mth Bill Control
 checkbox.

1. In the Last Month Closed field,
 enter a month to stop the entry of incoming invoices and prevent further changes
 in Job Billing for that month.Tip: The month you
 enter can be the current month, as this would allow your accounting team
 time to finish tasks while the AR Subledger and General Ledger remain
 open, but without having to account for new JB invoices.This setting allows you to close the month in JB
 independent of the last month closed in GL.

1. In the Closed Mth Bill Access Role
 field, do one of the following:

- If you want to set up a new role or edit an existing
 one, press F5
 to launch the [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form). Then select the new role you create.

- If you want to choose an existing role from the list
 of active HQ Roles, press F4 to open the lookup. Select the existing role you
 want to use.

- If you want to prevent all users in your JB company
 from being able to add, edit, or delete bills in closed months, leave
 this field blank.

1. Save your changes.

For more details about each of these bill control fields, see
 [Field Definitions: JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form/field-definitions-jb-company-parameters-form#concept-hfuvp07s--en).

If you want to enable settings to limit which users can
 add, edit, or delete bills assigned to other users, see [Set Bill Controls to Restrict Changes to Bills Assigned to Other
 Users](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-bill-controls-to-restrict-changes-to-bills-assigned-to-other-users).
