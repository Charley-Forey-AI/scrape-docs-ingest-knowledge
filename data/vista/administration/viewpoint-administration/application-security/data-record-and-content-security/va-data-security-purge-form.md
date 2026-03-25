---
title: "VA Data Security Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-purge-form"
---

# VA Data Security Purge Form

Use this program to purge orphaned security entries; that is, entries in VA Data Security Access that no longer have existing detail in the system due to module specific purges.
To purge a security entry, enter the datatype in the Datatype
 field and press Enter. The form cycles through all tables in the system and locates
 secured datatype instances where no detail exists. Depending on the number of security
 entries and the number of tables the system checks for detail, this process may take
 some time.
Once the cycle process is complete, the system populates the grid with all eligible
 qualifiers (for example, Co#/Job#, Co#/Employee#, and so on). Click
 Purge to purge the orphan entries.
