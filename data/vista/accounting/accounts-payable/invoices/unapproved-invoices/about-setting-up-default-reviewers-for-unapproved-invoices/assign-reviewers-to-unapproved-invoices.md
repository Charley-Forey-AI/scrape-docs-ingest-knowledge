---
title: "Assign Reviewers to Unapproved Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-setting-up-default-reviewers-for-unapproved-invoices/assign-reviewers-to-unapproved-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-setting-up-default-reviewers-for-unapproved-invoices/assign-reviewers-to-unapproved-invoices"
---

# Assign Reviewers to Unapproved
 Invoices

You can assign reviewers to unapproved invoices so that they can review and approve
 invoices before the invoices are posted.
 Creating and assigning reviewers is the central required
 element in the AP unapproved invoice process. In order for the process to work, you must
 assign at least one reviewer to each line on the invoice that is being reviewed. See [About Reviewers for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewers-for-unapproved-invoices) for more
 information.Use the Reviewer tabs in AP
 Unapproved Invoice Entry to assign active reviewers to the header or line levels of the
 invoice. Assignment of reviewers at the header level is not required, but if you do, the
 same reviewers default on to every invoice line. Once you assign reviewers, the
 Date
 Assigned field (Reviewers tab) for the line defaults the current date.
 You can also delete reviewers from an unapproved invoice as necessary.
At the line level, you may assign or
 override reviewer groups on the info tab or individual reviewers on the Reviewers tab.
 Using reviewer groups allows for increased functionality; see [About Reviewer Groups for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewer-groups-for-unapproved-invoices) for more
 information.

1. From the main menu, select Accounts Payable > Programs > AP Unapproved Invoices.

1. Use the Month and Seq # fields to
 select the appropriate invoice.

1. To assign reviewers by group at the header level, enter the reviewer group in the
 Reviewer Group field of the invoice header. All reviewers without an assigned threshold amount display on the Reviewers
 tab in the invoice header. In addition, those same reviewers default to the Reviewers
 tab at the invoice line level. For more information on setting threshold amounts, see
 [About Thresholds for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-thresholds-for-unapproved-invoices).Note: The
 Reviewer group in the header does not default to the Reviewer
 Group field on the line(s).

1. To assign reviewers by group at the line level, enter the reviewer group in the
 Reviewer Group field of each applicable invoice line.The system adds reviewers associated with this group to the line Reviewers
 tab, along with any existing reviewers from the header level and any reviewers
 assigned by any other means.

1. To assign individual
 reviewers to an invoice:

1. If the reviewer should be assigned to every invoice line (existing and
 future), select the Reviewers tab in the invoice header.

1. In the Reviewer field, enter the reviewer's
 name.

1. If you are using a sequence-based approval process, use the
 Approval Seq field to enter the approval sequence
 number.Note: The sequence number determines the order in which reviewers are able to
 view and approve invoice lines. For more information on sequences, see [About Assigning Approval Sequences for
 Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-assigning-approval-sequences-for-unapproved-invoices).

1. If applicable, enter additional reviewers to invoices lines using the
 Reviewers tab for each applicable invoice line. Specify a sequence number as
 applicable in the Approval Seq field and then
 use the Optional Reviewer checkbox to indicate whether
 the the reviewer is optional.

Note: If you enter a job, equipment, location (item), or GL account that has a
 default reviewer group assigned, that reviewer group defaults for the line and
 places the reviewers of the group on the Reviewers tab. While you cannot specify
 an additional group, you can either replace the default group or add the
 individual reviewers to the Reviewers tab. If you replace the default group, the
 system removes the reviewers associated with the old group and adds the reviewers
 associated with the new group.

1. Save the record.Note: If you pre-assigned reviewers to the job, equipment department, inventory
 location (items), GL account, additional reviewers may default at the line level.
 If a reviewer is already assigned to the line for one reason, the system will not
 add it again. If you change the record in a way that prompts the system to remove
 a reviewer, the system will check whether it should remain for any other reason
 before removing. Note that the system always assigns a sequence number 1 to each
 reviewer that doesn't already have one from a group assignment. Reviewers
 associated with groups that default for any other reason will have an approval
 sequence of 1.

Once the invoice is ready for review, the
 reviewers assigned to the invoice can approve or reject the invoice/lines in AP Unapproved
 Invoice Review.Note: You can delete or change reviewers as needed. However, you must have at least one
 reviewer assigned to each invoice line. If you delete all reviewers from a line, you
 must add at least one reviewer before you can flag the invoice as ready for review
 (using the Status button in the invoice header).If you assigned a reviewer group
 to the invoice, but a reviewer in the group is not required to review the invoice,
 you can delete the reviewer from the line without affecting the group. If you delete or change a
 reviewer or group at the header level, the system also removes the group and/or
 reviewers from the invoice lines and replaces them if applicable. However, if you
 delete or change a reviewer on a line, the system does not update that change to
 the header level or any other lines.

Related information

- [About Setting Up Default Reviewers for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-setting-up-default-reviewers-for-unapproved-invoices)

- [About Assigning Approval Sequences for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-assigning-approval-sequences-for-unapproved-invoices)
