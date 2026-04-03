---
title: "Enterprise Installation - Properties tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/enterprise-management/enterprise-installation/enterprise-installation---properties-tab"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/tools/enterprise-management/enterprise-installation/enterprise-installation---properties-tab"
---

# Enterprise Installation - Properties tab

Use the Properties tab to set up a default security scheme and password requirements.
The scheme you enter here acts as the default for any operators who are not assigned a scheme elsewhere in the software, so this scheme should be set up with the lowest level security options.
FieldsDescriptions
Default schemeEnter the security scheme that you want to use as the default scheme, or click the drop-down arrow to select from a list of available schemes.The default entered here is for operators who do not have a scheme assignment in the Operator Maintenance screen.

Next operator codeEnter the first operator code for the software default.This number will be the next number to default in the Operator Maintenance > New Operator window.
Press Enter to accept this code or enter a new code if you want to overwrite the one displayed.Note: After 999 codes have been assigned, the next code will default to a combination of letters and numbers.

Use password encryption?Encrypted passwords are not readable from the database.
Require strong passwords?Select this checkbox if you want all operators to use strong passwords. These must be 6-24 characters long and they need to include at least three of the following:

- uppercase letters

- lowercase letters

- symbols (any keyboard symbols except for quotation marks)

- numbers

Minimum password lengthMust be six or more if you're using strong passwords.
Password expiration daysThe number of days between an operator setting a new password and having to set a new one.The number you enter here applies to all operators, but you can override it in the Operator Maintenance screen.

Track unsuccessful logon attempts in event log?Select this checkbox if you want to keep a record of the number of unsuccessful logon attempts for security purposes.
