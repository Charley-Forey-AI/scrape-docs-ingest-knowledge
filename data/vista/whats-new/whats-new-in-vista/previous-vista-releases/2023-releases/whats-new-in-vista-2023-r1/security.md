---
title: "Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/security"
---

# Security

The Vista 2023 R1 release includes the addition of new forms and form tabs. Since these additions may affect your security setup, you should review them to determine what changes are necessary for your company.

## New Forms

New forms in Vista come without security settings applied and are therefore not immediately accessible. In order for users to take advantage of the following new forms, you must first grant access using the VA Form Security form.
Some forms appear as tabs on the parent form, but have a separate form attached to the tab. In some cases, you can access the form individually by double-clicking in the tab's grid. However, in most cases, the forms attached to the tab are not individually accessible; entry can only be done via the tab's grid.
ModuleForm TitleForm NameAccessed FromInherits Security FromHas Own SecurityCan Set Separate Security
HQHQ Project Structure TypesHQProjectStructureTypesMain MenuN/AYN/A
JBJB Invoice DeliveryJBEmailMain MenuN/AYN/A
JB Email DeliveryJBEmailDeliveryJB Invoice DeliveryJB Invoice Delivery (JBEmail)NY
JB Email RecipientsJBEmailDeliveryRecipientsJB Email DeliveryJB Invoice Delivery (JBEmail)NY
JCJC Contract RecipientsJCContractRecipientsJC Contracts (JB Info tab)
 JB Contract Info formN/AYN/A
JC Contract Recipients DetailJCContractRecipientsDetailJC Contracts (JB Info tab)
 JB Contract Info formN/AYN/A
PMPM SL Work Flow ReviewersPMSLItemReviewersPM Subcontracts (Workflow button)N/AYN/A
PM SL Work Flow Item ReviewersPMSLItemReviewersGridPM Subcontract (Workflow button)PM SL Work Flow Reviewers (PMSLItemReviewers)NY
PRPR Employee Aatrix ID ValuesPREmplAatrixIDsPR Employees (Aatrix ID Values tab)PR Employees (PREmpl)NY

The table above indicates whether these forms have their own security setup in the VA Form Security form or inherit security from the parent form. If a form which inherits security from the parent form also offers the option to set security separately, take these steps to do so:

1. Open the parent form and place the focus on the pertinent tab.

1. Select Tools > Form Properties.

1. In the Form Properties window, select the Security tab.

1. Select the Allow security for this form to be maintained separately checkbox.

1. Click Close.You can then apply security as needed in the VA Form Security form.

Tip: If you want to apply this setting to multiple/many/all forms, use the grid in the VA Form Properties form to quickly select the Allow security for this form to be maintained separately checkbox for the pertinent forms.

## New Tabs

Vista allows you to set security at the tab level for some forms. This is a list of new tabs added to Vista for the 2022 R1 release.
ModuleForm NameTab TitleInherits Security FromHas Own SecurityCan Set Tab SecurityCan Set Separate Security
HQHQProjectStructureTypes(HQ Project Structure Types)
GridHQProjectStructureTypesNNN
InfoHQProjectStructureTypesNYN
NotesHQProjectStructureTypesNYN
JBJBEmailDelivery(JB Email Delivery)
GridJBEmailNNN
InfoJBEmailNYN
RecipientsJBEmailNNN
JBProgressBillHeader(JB Progress Billing)
DeliveryJBProgressBillHeaderNNN
NotesJBProgressBillHeaderNNN
JBTMBills(JB T&M Bill Edit)
Recipients*JBProgressBillHeaderNNN
DeliveryJBProgressBillHeaderNNN
PMPMSLHeader(PM Subcontracts)
Workflow HistoryPMSLHeaderNYN
PRPREmpl(PR Employees)
Aatrix ID* ValuesPREmplNNN
PREmplAatrixIDs(PR Employee Aatrix ID Values)
GridPREmplNNN
NotesPREmplNYN

* These tabs have forms attached to them for which you can set security separately (indicated by a Y in the Can set separate security column). To set security separately for these forms, open the parent form, place focus on the tab, and select Tools > Form Properties. In the Form Properties window, click on the Security tab, select the Allow security for this form to be maintained separately checkbox, and click Close to save the change. You can then apply security as needed in the VA Form Security form.
