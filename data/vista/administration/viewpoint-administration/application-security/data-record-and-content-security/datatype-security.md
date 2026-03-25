---
title: "Datatype Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security"
---

# Datatype Security

Datatypes identify the format for fields (for example,
 Company, CM Accounts, Job, Employee, etc.).
The system uses tables to store the information
 entered on forms. For example, the system uses the JCJM table to store information
 entered in JC Jobs, the CMAC tables stores information entered in CM Accounts, and so
 forth. Data entered in other associated or related forms may also update the information
 in these tables. By setting up datatype security, you can identify secured fields in
 each of the related tables. Because datatype/table security can affect the performance
 of your system, it is important to consider how to enable datatype security before you
 decide to implement it.
 When you enable field level (datatype) security, the system performs a variety of additional checks to ensure that the user can enter data. This can slow down data entry or informational displays. Additionally, users may find that reports do not contain necessary information when you enable security for a datatype. For example, if you enable datatype security for Jobs, and you run a job cost report for all jobs, the report prints only jobs that you have access to. In addition, the grand total on the report will display the grand total only for the jobs you have access to.
 The system arrives with the following predefined, securable datatypes:

- Company (bARCo, bAPCo, bCMCo, bGLCo, etc.)

- Contract (bContract)

- Job (bJob)

- CM Account (bCMAcct)

- Employee (bEmployee)

- Reference (bHRRef)

- Location (bLoc)

 Additionally, datatype are automatically secured for selected tables. You may change this setting as necessary. For more information, see [Setting Datatype Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes).

Related information

- [Securing Datatypes](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)
