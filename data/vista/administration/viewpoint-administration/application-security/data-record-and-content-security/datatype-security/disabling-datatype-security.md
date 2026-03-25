---
title: "Disabling Datatype Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/disabling-datatype-security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/disabling-datatype-security"
---

# Disabling Datatype Security

Disable datatype security.
Use the [VA Data Security Setup](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form) form to disable datatype security that [has previously been set up](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes).
Note: The Secure Tables tab displays all tables that contain an occurrence of the specified datatype, the field name (Instance Column), and the Qualifier Column (the qualifier is generally the company). Field names may differ between forms. For example, if the datatype is ‘bEmployee’, the instance column might be called 'Employee’ on one form and ‘Contact Name’ on another.

1. In the VA Data Security
 Setup form, enter the datatype in the Datatype field.

1. Uncheck the Secure
 Datatype box.

1. Save the record. The system displays a dialog box asking if you want to clear the security group setting for all datatype instances.

1. Click Yes
 to have the system clear the security group for each instance in all companies.


1. Click the Regenerate Views button. The VA View Generator form displays.

1. Use the VA View Generator form to regenerate views. For more information, see [VA View Generator](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-view-generator-form).

1. Close VA View
 Generator. Focus returns to VA Data Security Setup. The system clears the
 Secured box for each table that was secured. Note: The Apply Security checkbox
 remains checked for any specified tables.

Related information

- [Securing Datatypes](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)
