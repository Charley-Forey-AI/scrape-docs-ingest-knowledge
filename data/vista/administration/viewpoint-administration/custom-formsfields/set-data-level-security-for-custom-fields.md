---
title: "Set Data Level Security for Custom Fields | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-data-level-security-for-custom-fields"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-data-level-security-for-custom-fields"
---

# Set Data Level Security for Custom
 Fields

You can set data level security for custom fields added via VA Custom Fields Wizard.
In order to secure a custom field, you must
 associate the field with a securable datatype. For example, if you are creating an
 Employee field that requires security, assign it to the bEmployee datatype.
When creating a custom field, the Wizard provides the option to use a pre-defined datatype. If you do not use a pre-defined type, you must format the field manually. However, if you elect to use a pre-defined type, make sure it is a securable datatype. The following list displays all available securable datatypes:
bAPCo
bHQCo
bLoc

bARCo
bHRCo
bMSCo

bCMAcct
bINCo
bPOCo

bCMCo
bHRRef
bPMCo

bContract
bJBCo
bPRCo

bEMCo
bJob
bRMCo
bEmployee
bJCCo
bSLCo

bGLCo

Since data level security requires a qualifier (i.e.
 company), make sure that the table you are adding the field to contains the
 appropriate company column. For example, if you are adding a custom field that
 references the bEmployee datatype, the table must contain the PRCo column. If it
 does not, you will need to add it before adding any custom field referencing the
 bEmployee datatype. Adding the Co column to the table makes the table available for
 selection in VA Data Security Setup.
Once you have set up the user-defined field, access
 VA Data Security Setup, locate the desired table (Secured Tables tab), check the
 In
 Use box, and regenerate the view to incorporate the change. For more
 information, see [VA Data Security Setup](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form).

Related information

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)

- [VA Data Security Access Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-data-security-access-form)

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)
