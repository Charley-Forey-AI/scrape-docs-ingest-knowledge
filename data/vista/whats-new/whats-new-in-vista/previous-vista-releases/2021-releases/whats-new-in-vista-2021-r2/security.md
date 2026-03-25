---
title: "Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/security"
---

# Security

The Vista 2021 R2 release includes the addition of new forms and form tabs. Since these additions may affect your security setup, you should review them to determine what changes are necessary for your company.

## New Forms

New forms in Vista come without security settings applied and are therefore not immediately accessible. In order for users to take advantage of the following new forms, you must first grant access using the VA Form Security form.
Some forms appear as tabs on the parent form, but have a separate form attached to the tab. In some cases, you can access the form individually by double-clicking in the tab's grid. However, in most cases, the forms attached to the tab are not individually accessible; entry can only be done via the tab's grid.
ModuleForm TitleForm NameAccessed FromInherits Security FromHas Own SecurityCan Set Separate Security
APAP Check ReviewAPCheckReviewVWMain MenuN/AYN/A
AP HR Expense PostingAPExpensePostingVWMain MenuN/AYN/A
AP Invoice ReviewAPInvoiceReviewVWMain MenuN/AYN/A
HRHR Applicant SearchHRApplicantSearchVWMain MenuN/AYN/A
HR Benefits DashboardHRBenefitsDashboardVWMain MenuN/AYN/A
HR Job RequisitionsHRJobRequisitionsVWMain MenuN/AYN/A
HR Manage TrainingHRManageTrainingVWMain MenuN/AYN/A
HR Onboarding DashboardHROnboardingDashboardVWMain MenuN/AYN/A
HR Training DashboardHRTrainingClassDashboardVWMain MenuN/AYN/A
JBJB Billing CompilerJBBillingCompilerVWMain MenuN/AYN/A
JB DashboardJBDashboardVWMain MenuN/AYN/A
JB Open Billing ReviewJBOpenBillingReviewVWMain MenuN/AYN/A
JCJC Field Ticket DashboardJCFieldTicketDashboardVWMain MenuN/AYN/A
POPO DashboardPMDashboardVWMain MenuN/AYN/A
PMPM FieldTicket DashboardPMFieldTicketDashboardVWMain MenuN/AYN/A
PM Manage TrainingPMManageTrainingVWMain MenuN/AYN/A
PM Open Billing ReviewPMOpenBillingReviewVWMain MenuN/AYN/A
PM Timecard DashboardPMTimecardDashboardVWMain MenuN/AYN/A
PM Training DashboardPMTrainingClassDashboardVWMain MenuN/AYN/A
POPO DashboardPODashboardVWMain MenuN/AYN/A
PO Purchasing AgentPOPurchasingAgentVWMain MenuN/AYN/A
PRPR HR Expense PostingPRExpensePostingVWMain MenuN/AYN/A
PR Paystub ToolsPRPaystubToolsVWMain MenuN/AYN/A
PR Timecard Batch MovePRTimecardBatchMoveVWMain MenuN/AYN/A
PR Timecard DashboardPRTimecardDashboardVWMain MenuN/AYN/A
SMSM Agreement NotesSMAgreementNotesSM Agreements, Agreement Notes
 tabSM AgreementsNY
SM Agreement TermSMAgreementTermSM Agreements, Term Notes tabSM AgrementsNY
VAVA Portal User AccessVAUserAccessVWMain MenuN/AYN/A
VA Web FormsVAWebFormsMain MenuN/AYN/A

The table above indicates whether these forms have their own security setup in the VA Form Security form or inherit security from the parent form. If the form inherits security from the parent form, you may be able to set security separately, which is also indicated in the table. To set security separately for applicable forms, open the parent form, place focus on the tab, and select Tools > Form Properties. In the Form Properties window, click on the Security tab, select the Allow security for this form to be maintained separately checkbox, and click Close to save the change. You can then apply security as needed in VA Form Security.Note: You can also use VA Form Properties to set the Allow security for this form to be maintained separately checkbox for a form.

## New Tabs

Vista allows you to set security at the tab level for some forms.
 This is a list of new tabs added to Vista for the 2021 R2 release.
ModuleForm NameTab TitleInherits Security FromHas Own SecurityCan Set Tab SecurityCan Set Separate Security
APAPCheckReviewVWAPCheckReviewVWAPCheckReviewVWNNN
SMSMAgreement *Term NotesSM AgreementsNNY
SMAgreement *Agreement NotesSM AgreementsNNY
SMAgreementNotesGridSM Agreement NotesNNN
SMAgreementNotesInfoSM Agreement NotesNYN
SMAgreementNotesNotesSM Agreement NotesNYN
SMAgreementTermGridSM Agreement TermNNN
SMAgreementTermInfoSM Agreement TermNYN
SMAgreementTermNotesSM Agreement TermNYN
SMCustomerBillingSM CustomersNYN
VAVAWebFormsGridVA Web FormsNNN
VAWebFormsInfoVA Web FormsNYN
VAWebFormsNotesVA Web FormsNYN

* These
 tabs have forms attached to them for which you can set security separately
 (indicated by a Y in the Can set
 separate security column). To set security separately for these
 forms, open the parent form, place focus on the tab, and select Tools > Form Properties. In the Form Properties window, click on the Security tab, select the
 Allow security for this form to be
 maintained separately checkbox, and click Close to save the change. You can
 then apply security as needed in the VA Form Security form.
