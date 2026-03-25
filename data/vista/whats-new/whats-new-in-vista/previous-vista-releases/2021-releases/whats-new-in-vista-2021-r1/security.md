---
title: "Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/security"
---

# Security

The Vista 2021 R1 release includes the addition of new forms and form tabs. Since these additions may affect your security setup, you should review them to determine what changes are necessary for your company.

## New Forms

New forms in Vista come without security settings applied and are therefore not immediately accessible. In order for users to take advantage of the following new forms, you must first grant access using the VA Form Security form.
Some forms appear as tabs on the parent form, but have a separate form attached to the tab. In some cases, you can access the form individually by double-clicking in the tab's grid. However, in most cases, the forms attached to the tab are not individually accessible; entry can only be done via the tab's grid.
ModuleForm TitleForm NameAccessed fromInherits security fromHas own securityCan set separate security
APAPVendorDuplicatesAP Vendor DuplicatesAP Vendor Master (Duplicate Vendors tab)AP Vendor MasterNY
APVendorMergeAP Vendor MergeN/AN/AYN/A

The table above indicates whether these forms have their own security setup in the VA Form Security form or inherit security from the parent form. If the form inherits security from the parent form, you may be able to set security separately, which is also indicated in the table. To set security separately for applicable forms, open the parent form, place focus on the tab, and select Tools > Form Properties. In the Form Properties window, click on the Security tab, select the Allow security for this form to be maintained separately checkbox, and click Close to save the change. You can then apply security as needed in VA Form Security.Note: You can also use VA Form Properties to set the Allow security for this form to be maintained separately checkbox for a form.

## New Tabs

Vista allows you to set security at the tab level for some forms. This is a list of new tabs added to Vista for the 2020 R1 release.
ModuleForm NameTab TitleInherits security fromHas own securityCan set tab security Can set separate security
APAPVendMasterDuplicate Vendors *AP Vendor MasterNNY
DMHQAttIndexSMAttachment Form (DMAttachments)NYN
IMIMTemplateImport\ExportIM TemplatesNYN

* These tabs have forms attached to them for which you can set security separately (indicated by a Y in the Can set separate security column). To set security separately for these forms, open the parent form, place focus on the tab, and select Tools > Form Properties. In the Form Properties window, click on the Security tab, select the Allow security for this form to be maintained separately checkbox, and click Close to save the change. You can then apply security as needed in the VA Form Security form.
