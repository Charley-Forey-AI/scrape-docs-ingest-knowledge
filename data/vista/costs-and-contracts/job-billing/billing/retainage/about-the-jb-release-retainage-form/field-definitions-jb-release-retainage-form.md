---
title: "Field Definitions: JB Release Retainage Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/retainage/about-the-jb-release-retainage-form/field-definitions-jb-release-retainage-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/retainage/about-the-jb-release-retainage-form/field-definitions-jb-release-retainage-form"
---

# Field Definitions: JB Release Retainage Form

The following is a list of field descriptions for the JB
 Release Retainage form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Bill Month

 Specify the bill month to release retainage for.
Note: If you specify a month that is closed in subledgers,
 a blue warning displays next to the Bill Number field and all
 remaining fields are disabled.

##  Bill Number

 Specify the bill number to release retainage for. The Release by Contract section displays the invoiced and open retainage amounts for all previous billings, as well as for the current billing.
Note: If you specify a billing in a closed month, a blue warning displays next to the Bill Number field, and all remaining fields are disabled.

##  Reverse Previously Released Retainage

 This field is enabled for “Active” billings only.
 Check this box to reverse previously released retainage for this contract.
Note: You cannot reverse released retainage on closed-month billings or interfaced billings. However, you can reverse released retainage related to a closed-month or interfaced billing by creating a new billing (in an open month), then using the new billing to reverse the desired released retainage amount.
 Leave this box unchecked if you are not reversing previously released retainage.

##  Release by Contract or Item

- Contract – Select this radio button to release retainage at the contract level. This enables the % Released, Amount Released, and Net Retg - This Bill fields in the Release By Contract section.

- Item – Select this radio button to release retainage at the contract item level. This enables the % Released and Amount Released columns in the items grid.

##  % Released This Bill

 Indicate the percentage of total open retainage to release on this billing. The amount released for this billing is calculated and displayed in the Amt Released field.
Note: If you are reversing previously released retainage (i.e. the Reverse Previously Released Retainage checkbox is selected), enter this as a positive value.

## Amount Released This Bill

If you enter a percentage in the % Released This
 Bill field, the amount to release is automatically calculated and displayed
 in this field. Override this value as necessary, but the percentage entered in the previous
 field will recalculate.
If you did not enter a percentage in the
 % Released This
 Bill field, enter the amount of retainage to release. The system
 automatically calculates the percentage and displays it in the % Released This
 Bill field.
Note: If you are reversing previously released retainage
 (i.e. the Reverse
 Previously Released Retainage box is checked), enter this as a negative
 value.

##  Net Retainage This Bill

 This field defaults the total remaining retainage available for release. If you override this amount, the system will recalculate the percentage and amount released.

##  % Released

 For release by contract item only, specify the percent of this item’s retainage to release. The amount to release will be calculated and displayed in the Amt Released field.
Note: If you are reversing previously released retainage (i.e. the Reverse Previously Released Retainage checkbox is selected), enter this as a positive value.

##  Amount Released

 For release by contract item only, specify the fixed amount of this item’s retainage to release. The system calculates the released percentage and displays it in the % Released field.
Note: If you are reversing previously released retainage (i.e. the Reverse Previously Released Retainage checkbox is selected), enter this as a negative value.
