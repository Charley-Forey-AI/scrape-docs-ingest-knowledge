---
title: "About the VA View Generator Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-view-generator-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-view-generator-form"
---

# About the VA View Generator Form

Use this form to regenerate views after you have adjusted
 datatype security settings in VA Data Security Setup.
The system uses views, in conjunction with VA Data Security Access settings, to implement security on underlying database tables. Views screen out all data that a user does not have permission to access. Use this form to generate views after activating or updating datatype security.
You can access this form by:

- Clicking the Regenerate Views button in [VA Data Security Setup](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form). With this method, the form
 displays only those views related to the datatypes you selected in the VA Data
 Security Setup form.

- Opening it in the Viewpoint Administration > Programs folder. With this
 method, the form displays all securable views.

This form allows you to refresh views that allow custom fields (that you added
 previously via the VA Custom Fields Wizard form). This option is useful when a custom
 field is not working properly and you want to troubleshoot the cause. To refresh views
 that allow custom fields, select Tools > Refresh all
 views from the VA View Generator form. The system will display a confirmation
 dialog box. Click Yes to refresh views.

[Regenerating Views](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/regenerating-views)

Related information

- [Regenerating Views](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/regenerating-views)

- [Securing Datatypes](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes)

- [VA Data Security Access Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-data-security-access-form)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)
