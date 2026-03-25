---
title: "Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/security"
---

# Security

The Vista 2022 R1 release includes the addition of new forms and form tabs. Since these additions may affect your security setup, you should review them to determine what changes are necessary for your company.

## New Forms

New forms in Vista come without security settings applied and are therefore not immediately accessible. In order for users to take advantage of the following new forms, you must first grant access using the VA Form Security form.
Some forms appear as tabs on the parent form, but have a separate form attached to the tab. In some cases, you can access the form individually by double-clicking in the tab's grid. However, in most cases, the forms attached to the tab are not individually accessible; entry can only be done via the tab's grid.
Note: The Job Billing and Payroll forms listed in the table below were put in place for an upcoming release. They are not currently in use.

ModuleForm TitleForm NameAccessed FromInherits Security FromHas Own SecurityCan Set Separate Security
JBJB Prog Bill Delivery HistoryJBProgressBillDeliveryHistoryJB Progress BillingJB Progress BillingNY
JB Progress Bill RecipientsJBProgressBillRecipientsJB Progress BillingJB Progress BillingNY
JB T&M Bill Delivery HistoryJBTMBillDeliveryHistoryJB T&M Bill EditJB T&M Bill EditNY
JB T&M Bill RecipientsJBTMBillRecipientsJB T&M Bill EditJB T&M Bill EditNY
PRPR Employee Accums Detail (Australia)PRAUEmployeeAccumsDtlGridPR Employee AccumulationsPR Employee AccumulationsNY
PR Employee Accums Detail (Australia)PRAUEmployeeAccumsDtlHdrPR Employee AccumulationsPR Employee AccumulationsNY
PR STP 2 Amt Primary (Australia)PRAUSTP2AmtPrimaryPR STP ProcessPR STP ProcessNY
PR STP Employee Amounts (Australia)PRAUSTPEmployeeAmountsPR STP ProcessPR STP ProcessNY
RPSync SSRS SecurityRPSYNCSSRSRP RS ServerN/AYN/A

The table above indicates whether these forms have their own security setup in the VA Form Security form or inherit security from the parent form. If the form inherits security from the parent form, you may be able to set security separately, which is also indicated in the table. To set security separately for applicable forms, open the parent form, place focus on the tab, and select Tools > Form Properties. In the Form Properties window, click on the Security tab, select the Allow security for this form to be maintained separately checkbox, and click Close to save the change. You can then apply security as needed in VA Form Security.Note: You can also use VA Form Properties to set the Allow security for this form to be maintained separately checkbox for a form.

## New Tabs

Vista allows you to set security at the tab level for some forms. This is a list of new tabs added to Vista for the 2022 R1 release.
Note: The Job Billing and Payroll tabs listed in the table below were put in place for an upcoming release. They are not currently in use.

ModuleForm NameTab TitleInherits Security FromHas Own SecurityCan Set Tab SecurityCan Set Separate Security
JBJB Company ParametersEmail SettingsJB Company ParametersNYN
JBProgressBillRecipientsGridJB Progress BillingNNN
JBProgressBillRecipientsInfoJB Progress BillingNYN
JBTMBillRecipientsGrid JB T&M Bill EditNNN
JB T&M Bill EditRecipients*JB T&M Bill EditNNY
JB T&M Bill EditDelivery*JB T&M Bill EditNNY
PRPRAUSTPEmployeeAmountsTemp TabPR STP ProcessNNN

* These tabs have forms attached to them for which you can set security separately (indicated by a Y in the Can set separate security column). To set security separately for these forms, open the parent form, place focus on the tab, and select Tools > Form Properties. In the Form Properties window, click on the Security tab, select the Allow security for this form to be maintained separately checkbox, and click Close to save the change. You can then apply security as needed in the VA Form Security form.
