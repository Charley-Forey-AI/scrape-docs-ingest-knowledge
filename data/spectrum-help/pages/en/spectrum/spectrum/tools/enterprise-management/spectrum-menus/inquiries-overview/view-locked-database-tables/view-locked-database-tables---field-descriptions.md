---
title: "View Locked Database Tables - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/inquiries-overview/view-locked-database-tables/view-locked-database-tables---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/inquiries-overview/view-locked-database-tables/view-locked-database-tables---field-descriptions"
---

# View Locked Database Tables - Field Descriptions

A reference for completing the fields on this screen.
Fields/ButtonsDescriptions
Lock durationThe amount of time the user has been holding the lock.
Object nameThe table or view where the lock occurred.
CompanyA list of company codes associated with the record locks.
Company nameA list of the company names associated with the record locks.
Operator IDA list of the operator IDs for the operators who are causing the record locks.
NameA list of the names of the operators who are causing the record locks.
EmailIf available, this column displays the email addresses of the operators who are causing the record locks. This allows you to send the operators messages directly. Operator email address information is stored in the Edit Operator window.
Time onA list of the times when the operators who are causing the record locks first logged on to the software.
Terminal IDA list of the terminal numbers for the operators who are causing the record locks.
SessionA list of operator session numbers. The session number is the unique number that SQL Server assigns to each new process on the database. This number is then used to differentiate the file activity on the database.
Lock typeThe SQL Server lock code and a short text translation of the code.
Last logged functionThe last function that the Operator Audit Log recorded the user entering.
Lock granularityThe narrowest type of lock held on that particular object (KEY, RID, PAGE, OBJECT).
Blocked userA list of the operator codes and the companies in which the locks are occurring for the operators who are currently being blocked by the lock activity. For example, if no one is trying to access the same job while an operator is locking a table (in other words, the operator is not preventing anyone from viewing the table), then this column will appear blank while the other columns will contain data.
RefreshSelect to refresh the information on this screen and view the most current lock activity.
FindSelect to conduct a search on the View Locked Database Tables list using specific criteria:

- Operator - the operator ID of the person causing the lock.

- Company code - the company code of the session causing the lock.

- Session ID - the SQL Server session ID of the session causing the lock.

- File definition - the file definition of an object that is currently locked.

- Table/view - the name of the database table or view being locked.

Block InfoChoose the appropriate record and then select this button to see who is locking this process.
Send EmailChoose the record relating to the object you are trying to access and select this button to send a message to the person causing the record lock.
