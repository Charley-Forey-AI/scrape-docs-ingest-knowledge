---
title: "About Reviewer Groups for Unapproved Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewer-groups-for-unapproved-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewer-groups-for-unapproved-invoices"
---

# About Reviewer Groups for Unapproved Invoices

You can use reviewer groups to assign multiple reviewers to unapproved invoices.
Reviewer groups allow you to assign multiple reviewers to unapproved invoices/lines by adding the group to the header or the line (whether manually or automatically/by default). Reviewer groups also offer a number of functions that are not relevant to individual reviewers. More information about these options and instructions for setting up reviewer groups are available in [Creating Reviewer Groups for AP Unapproved Invoices](/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-ap-unapproved-invoices).
When creating and using reviewer groups, you should be aware of the following information:

- You can only assign active reviewer groups to invoices/lines.

- Reviewers can be assigned to more than one group.

- You can cause reviewer groups to default to the line from multiple sources. See [Setting Up Default Reviewers for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-setting-up-default-reviewers-for-unapproved-invoices) for more information.

- When you add a reviewer group to an invoice header, all associated reviewers will be added to the Reviewer tab in AP Unapproved Invoices, with the exception of reviewers assigned a threshold amount.

- If you make changes to the Reviewer
 Group field in either the header or the line in the AP Unapproved
 Invoice Entry form, the system updates the respective Reviewers tab accordingly.

- Since all reviewers listed in the header Reviewers tab also appear on each line, you should only add groups to the header if you want the group's reviewers to be assigned to every line.

- If you update the assigned reviewers for the group in HQ Reviewer Group, you can choose to have the system update all relevant invoice lines when saving the changes by responding accordingly to the prompt after making the change.

-

With the exception of adding reviewers to a reviewer group, changes to the reviewers of the group do not update automatically to existing lines. In order for changes applied to group's reviewers to take effect (such as up-level approvals, actions on changed data, email settings), you can either edit the line as needed or remove the group, save the record, and re-add the group. When deciding your best option, you must weigh the number of needed changes against the risk of any approvals that will need to be redone.

- Any changes you make to the fields in the Reviewers tab are not applied to existing invoices.

-  Any changes you make to the fields in the Info tab get applied by the system to existing invoices, with the exception of threshold reviewers.

- When there is a reviewer group on both the header and the line, and a reviewer belongs to both groups, the system takes the following actions:



-

On the Action on changed data dropdown, any one group’s setting of Clear prior approval on data change will be enforced; likewise, a setting of Clear prior approval on amount change will be honored over a setting of Nothing.



-

If the Allow up level approval dropdown is set to Approve for self and lower levels for only one group, the reviewer can view invoices as if the setting was on both groups.

-

If any of the email options on rejection are selected, the system will refer to the setting of the group in the header.

Note: There are a few things you should be aware of about how reviewers that are members of a group act in tandem with reviewers assigned to the same invoice/line that are not part of the group. See [About Reviewer Groups' Interaction with Individual Reviewers](/db/organizations/viewpoint/repositories/vista-production/content/documents/Vista/Viewpoint/AP/Overview/Transactions/Unapproved_Invoices/Unapproved_Invoices_Features/c_ap_unapproved_invoice_reviewer_groups_and_ind_reviewers.dita) for more information
