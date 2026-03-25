---
title: "Field Definitions: VA Data Security Setup | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form/field-definitions-va-data-security-setup"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form/field-definitions-va-data-security-setup"
---

# Field Definitions: VA Data Security Setup

The following is a list of field descriptions for the VA Data
 Security Setup form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Apply Security

The Apply Security checkbox on the VA Data Security Setup form, Secure Tables tab.
Select this checkbox for each table in which to secure this datatype.
CAUTION: If you are securing the bEmployee datatype, it is recommended that you do not select this checkbox for the bEMEM table (instance Operator). Doing so prevents the Show Basis field in EM Process Cost Allocations from displaying the basis if the equipment attached to the allocation has an Operator to which the user (running allocations) does not have access. This results in the user being unable to create the allocation batch.

Once you have selected the tables to secure, select Regenerate Views to update all
 tables with the security changes.

Related information

- [Securing Datatypes](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes)

- [Disabling Datatype Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/disabling-datatype-security)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)

## Datatype

The Datatype field on the VA Data Security Setup form.
Enter a valid datatype to secure or press F4 to select from a list of valid datatypes.

Related information

- [Securing Datatypes](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes)

- [Disabling Datatype Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/disabling-datatype-security)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)

## Default Security Group

Default Security Group field on the VA Data Security Setup form
 Enter the default security group for this
 datatype. The system automatically grants this security group access to any new occurrence
 of this datatype, based on which tables are in use (Apply Security checkbox selected on the
 Secure Tables tab). To assign access to this datatype for any other security group, use VA
 Data Security Access.
Note: If you leave this field blank, upon saving the record (or moving to the grid), a message displays indicating that the default security group is missing. You can save the record, but it is suggested that you assign a default security group to prevent having to assign them manually (via VA Data Security Access).
Changing the Security Group
If you change the default security group for a datatype, a message displays indicating that
 the default security group has changed and asks if you want to update all instances with
 the new default security group. If you select Yes, all instances where the existing
 security group matches the previous default security group (that is, the one you changed),
 or is blank, update with the new security group. The system leaves all other instances
 intact.
Note:Changing the security group here does not affect additional security
 set up on the JC Jobs (Security Group field), JC Contracts (Security Grp field), and PR
 Group Master (Group Security tab) forms.

## Secure Datatype

Secure Datatype checkbox on the VA Data Security Setup form
 Select this checkbox to secure this datatype.
Note: After selecting this checkbox, you can set up security for this datatype (by company and instance or security group) in VA Data Security Access.

Related information

- [Securing Datatypes](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes)

- [Disabling Datatype Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/disabling-datatype-security)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)
