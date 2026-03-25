---
title: "About Changing Interfaced or Closed-Month Billings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-changing-interfaced-or-closed-month-billings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-changing-interfaced-or-closed-month-billings"
---

# About Changing Interfaced or Closed-Month Billings

## Changes to Interfaced Billings

If you need to make changes to a billing that has already been interfaced to AR, be
 aware that changes will only update AR if the Status of the
 billing is Change.
Changes made to the header information,
 billing items, or change order detail will automatically set the status to
 Change in the bill header. If changes are made to a
 billing item, the item's Change flag will automatically be
 set to Y in the JBIT (JB Bill Items) table. When the
 interface is run, any billing or billing items flagged as changed will update AR.

Regardless of whether you are changing
 interfaced or closed-month billings, you will typically want to update the previous
 amounts for all future billings to ensure accuracy. For information on updating
 previous amounts, see [About Updating Previous Billed Amounts on
 Future Bills](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-updating-previous-billed-amounts-on-future-bills).

## Changes to Closed-Month Billings

For both Progress and T&M billings, the ability to add,
 change, or delete billings in a closed month depends on the Closed Month Bill Control options
 in JB Company Parameters.
If the Closed Month Bill Control options
 are enabled, *only* users assigned to the role
 entered in Closed Mth Bill Access
 Role have the ability to add, change, or delete closed-month
 billings. Anyone with permissions to interface a bill can do so, however, not just
 those assigned to the Closed Mth Bill Access Role.
When accessing a closed-month billing, a
 message displays (in blue) at the top of the form warning you that the subledger
 month is closed, however, changes are allowed.
Changing the amount of retainage on a
 closed-month billing is also allowed, as long as the new retainage value is not less
 than what has previously been released. However, you cannot change released
 retainage. For more details, see [About the JB Release Retainage Form](/en/vista/vista/costs-and-contracts/job-billing/billing/retainage/about-the-jb-release-retainage-form).
Once you have changed a closed-month
 bill, it can be re-interfaced as long as you re-interface it to a month that is open
 in JC and AR. You can still re-interface a closed-month bill even if the JB bill
 month (entered in the Last Month
 Closed field on the JB Company Parameters form) is closed.
Since the JB Interface Batch Selection
 form will automatically default the closed month, you will need to change the month
 to an open month before you can proceed with the interface. Once you have changed
 and re-interfaced a closed-month billing, additional changes can only be made to
 billings in months equal to or later (greater) than the closed-month bill.
Regardless of whether you are changing
 interfaced or closed-month billings, you will typically want to update the previous
 amounts for all future billings to ensure accuracy. For information on updating
 previous amounts, see [About Updating Previous Billed Amounts on
 Future Bills](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-updating-previous-billed-amounts-on-future-bills).
