---
title: "Introduction to Info-Link | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/introduction-to-info-link"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/introduction-to-info-link"
---

# Introduction to Info-Link

Info-Link provides an easy-to-use interface to the database security features.
All Spectrum data is stored in the Microsoft SQL Server database. The database has built-in security features that can be used to define user access.
Info-Link provides two main functions:

- It makes security setup and maintenance accessible to administrators without requiring special database training.

- It provides a way to look at the structure of the Spectrum database in order to find which tables store which information.

For security reasons, limited access should be given to the Info-Link security setup programs. These programs control which users have access to which tables, based on passwords and security clearance levels. Normally, the same person who administers the security for the Spectrum application should administer the Info-Link security.

## Access Levels

It's important to control who receives access, what information they get access to, and what they can do to the database.
With Info-Link, you can set up the following types of security:

- Allow one or more users to have read-only access to one or more specific database tables.

- Allow one or more users to have full access (read and write permissions) to one or more specific database tables.

- Create a group with either read-only access or full access to one or more tables and then assign users to this group, which causes the users to inherit the access granted at the group level.

Info-Link provides the Systems Administrator with reports and inquiries that show exactly who has access to which tables in the database. With Info-Link security set up, you can be confident that users will have access only to specific parts of the database and they're ability to affect the database is well defined.

## Granting Access

Before users can access the Info-Link menu, the Systems Administrator needs to add the Info-Link security category to operator security. If needed, see [User Security Maintenance](/en/spectrum/spectrum/tools/info-link/info-link-screens-overview/user-security-maintenance).
It's recommended that the Systems Administrator be the only one granted access to the Info-Link security setup menu choices. It may be helpful for other users to have access to the Table Directory Inquiry (which displays which information is stored in which tables) and the Function / Table Cross-Reference feature.

##  Locating Information in the Spectrum Database

 Info-Link provides two ways to find where information is stored in the database: by module, or by screen function ID.

- Use the [Table Directory Inquiry](/en/spectrum/spectrum/tools/info-link/info-link-screens-overview/table-directory-inquiry) screen to view and print database table names and column documentation, by module.

- Use the [Function/Table Cross Reference Report](/en/spectrum/spectrum/tools/info-link/info-link-screens-overview/functiontable-cross-reference-report) to generate a listing of all files used by the specified function.
