---
title: "Create a Validation Procedure | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/custom-validation-procedures/create-a-validation-procedure"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/custom-validation-procedures/create-a-validation-procedure"
---

# Create a Validation Procedure

Create a new validation procedure that can be attached to any
 non-validated field, standard or custom (user-defined).

1. From the Info tab on the
 UD User Validation form, click the New Record icon ().

1. Enter a name and
 description of the validation procedure.

1. Use the Tables tab to
 specify the validating table(s). For example, a job validation procedure would
 use the JCJM table.

1. For each table specified
 on the Tables tab, enter the Error
 Message that displays when an invalid input is entered. This
 message should be brief and appropriately informative. For example, if an
 invalid job is entered, the error message might say, “Not a valid Job” or “Job
 not set up in JC Jobs (JCJM).”

1. In the
 Description
 field, enter the column from the validating table that displays as
 a label when a valid entry is accepted. Using the job validation example, the
 JCJM Description field would be specified to display next to the job number for
 a valid entry. Pressing F4 shows all available columns from the table specified
 in step 2. Note: If an invalid job is entered, and the
 validation level is set to blank (no validation) or “Warning, allow save,”
 the error message displays in the Description field. For more information on
 setting the validation level, see the “Assigning a Validation Procedure”
 section below.

1. Configure the validation
 parameters on the Parameters tab.

1. On the SQL tab, click
 Initialize to generate and display the SQL view. Procedures can
 be changed after initialization, but clicking Initialize again removes any changes.Note: For security reasons, certain commands
 cannot be used in custom (user-defined) validation procedures. If any of
 these words are found, the Compile process displays the following error
 message (where XXX equals the disallowed word): “Illegal command: XXX. For
 security reasons, you may not use this command in your validation
 procedure.” All disallowed words must be removed before a successful compile
 can occur. The following is a list of disallowed words:

- alter

- execute

- sys.


- create

- grant

- truncate

- dbcc


- insert

- update

- delete

- kill


- use


- deny


- revoke

- xp


- drop


- shutdown

- exec


- sp_


1. Click
 Compile
 to generate the validation procedure. This creates a new SQL
 procedure within the database.

1. Click Save () to save the validation
 procedure.

1. Assign the validation
 procedure to the field using the F3 window (System Overrides tab, Validation
 section). See [Customizing Validation using the System Overrides
 tab](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form).
