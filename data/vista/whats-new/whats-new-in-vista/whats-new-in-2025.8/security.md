---
title: "Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.8/security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.8/security"
---

# Security

The Vista 2025.8 release includes the addition of new forms and form tabs. Since these additions may affect your security setup, you should review them to determine what changes are necessary for your company.

## New Forms

New forms in Vista come without security settings applied and are therefore not immediately accessible. In order for users to take advantage of the following new forms, you must first grant access using the VA Form Security form.
Some forms appear as tabs on the parent form, but have a separate form attached to the tab. In some cases, you can access the form individually by double-clicking in the tab's grid. However, in most cases, the forms attached to the tab are not individually accessible; entry can only be done via the tab's grid.
ModuleForm
 TitleForm
 NameAccessed
 FromInherits
 Security FromHas Own
 SecurityCan Set
 Separate Security
HQHQ State ComplianceHQStateComplianceMain Menu and HQ StatesN/AYesNo
PRPR Pay Pd Control CompliancePRPayPdControl Compliance
PR Pay Period ControlN/AYesNo
PR Timecard CompliancePRTimeCards CompliancePR Timecard EntryN/AYesNo
PR Timecard Validation RulesPRTimecardValidation RulesN/AYesNo
PR Timecard Validation Rules ParamPRTimecardValidation RulesParamPR Timecard Validation RulesPR Timecard Validation RulesNoYes

The table above indicates whether these forms have their own security setup in the VA Form Security form or inherit security from the parent form. If a form which inherits security from the parent form also offers the option to set security separately, take these steps to do so:

1. Open the parent form and place the focus on the pertinent tab.

1. Select Tools > Form Properties.

1. In the Form Properties window, select the Security tab.

1. Select the Allow security for this form to be maintained separately checkbox.

1. Select Close.You can then apply security as needed in the VA Form Security form.

Tip: If you want to apply this setting to multiple/many/all forms, use the grid in the VA Form Properties form to quickly select the Allow security for this form to be maintained separately checkbox for the pertinent forms.

## New Tabs

Vista allows you to set security at the
 tab level for some forms. This is a list of new tabs added to Vista for the 20YY R# release.
ModuleForm NameTab TitleInherits Security FromHas Own SecurityCan Set Tab SecurityCan Set Separate Security
HQHQ StatesComplianceN/AYesNoN/A
HQ State ComplianceGridHQ State ComplianceNoNoNo
InfoHQ State ComplianceNoYesNo
NotesHQ State ComplianceNoYesNo
PRPR Company ParametersTimecard RulesN/AYesNoN/A
PR Pay Period ControlComplianceN/AYesNoN/A
PR Timecard ComplianceGridPR Timecard ComplianceNoNoNo
InfoPR Timecard ComplianceNoYesNo
PR Timecard Validation RulesGridPR Timecard Validation RuleNoNoNo
InfoPR Timecard Validation RulesNoYesNo
ParametersN/AYesNoN/A

* These
 tabs have forms attached to them for which you can set security separately
 (indicated by a Yes in the Can set
 separate security column). To set security separately for these
 forms, open the parent form, place focus on the tab, and select Tools > Form Properties. In the Form Properties window, choose the Security tab, select the
 Allow security for this form to be
 maintained separately checkbox, and select Close to save the change. You can
 then apply security as needed in the VA Form Security form.
Note: In some cases, you can only access the Form Properties for the tab's attached form using the VA Form Properties form. Once you locate the form, double-click to open the Form Properties window. Then choose the Security tab, select the Allow security for this form to be maintained separately checkbox, and select Close to save the change. You can then apply security as needed in the VA Form Security form.
