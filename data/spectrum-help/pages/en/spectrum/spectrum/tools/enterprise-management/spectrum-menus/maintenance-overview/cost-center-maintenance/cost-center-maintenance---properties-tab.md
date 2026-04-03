---
title: "Cost Center Maintenance - Properties Tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/cost-center-maintenance/cost-center-maintenance---properties-tab"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/cost-center-maintenance/cost-center-maintenance---properties-tab"
---

# Cost Center Maintenance - Properties Tab

Use this tab to set up or make changes to cost centers.
Fields
Descriptions

Cost center
If adding a new cost center, type the code you want to use as a label for the cost center here. If editing an existing cost center, no entry is allowed in this field.

Info

Description
If adding a new cost center, type the description you want to associate with this cost center. If editing an existing cost center, make any necessary changes to the description.

Address, phone
If adding a new cost center, type the primary address and phone number for the cost center here. If editing an existing cost center, make any necessary changes to the address and phone here.

Entity
This field only displays if entities are enabled. The Search
 Entities window will allow you to select a valid code.
The entity code and name will then display on the main [Cost Center Maintenance](/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/cost-center-maintenance) screen.

Status

Active/Inactive
Select the cost center status.
 If changing an Active cost center to an Inactive cost center, other users with security access to the specified cost center will no longer be able to access records or process transactions using this cost center (records will not be deleted, but they will remain inaccessible until the status is returned to Active).

Bank accounts

ePayments
Enter the bank account code used to default for electronic vendor payments.

Accounts Payable
Enter the Accounts Payable bank account that will act as the default override for the specified cost center, or double-click to select from a list of available codes. This field is only available if the Cash Management module is present and the posting checkbox in the Cash Management Installation – Bank Accounts tab is selected. Spectrum ensures that the cash G/L account associated with the bank account is valid for the specified cost center.
Tip: Any accounts used here must also be set up for use with cost centers in the Cash Management > Bank Account File Maintenance screen in the Edit window by
 clicking the Cost Center Sharing button and
 selecting the cost center validation checkbox.

Payroll
Enter the Payroll bank account that will act as the default override for the specified cost center, or double-click to select from a list of available codes. This field is only available if the Cash Management module is present and the posting checkbox in the Cash Management Installation – Bank Accounts tab is selected. Spectrum ensures that the cash G/L account associated with the bank account is valid for the specified cost center.
Tip: Any accounts used here must also be set up for use with cost centers in the Cash Management > Bank Account File Maintenance screen in the Edit window by
 clicking the Cost Center Sharing button and
 selecting the cost center validation checkbox.

Comdata
Enter the Comdata bank account number that will act as the default override
 for the specified cost center. When an AP bank account is specified on the
 cost center, the Comdata bank account is set equal to the AP bank account,
 and cannot be changed in the A/P Payment Selection
 screen.
