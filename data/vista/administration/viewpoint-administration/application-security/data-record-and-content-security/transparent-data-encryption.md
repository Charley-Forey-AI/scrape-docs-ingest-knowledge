---
title: "Transparent Data Encryption | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/transparent-data-encryption"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/transparent-data-encryption"
---

# Transparent Data Encryption

Transparent Data Encryption (TDE) is a means of securing data at rest in which all data that is written to disk is encrypted, including log files and database backups.
TDE has to do with the secured nature of how your Vista data is stored, but is managed by your organization outside the Vista application. Viewpoint recommends all organizations take steps to secure their ERP data.
Normally, data stored in a database file is stored in plain text. When you opt to use TDE, your data is more secure.
When you enable TDE on your SQL server, a 'key' is required to read the data, and without the correct key, data is unreadable. When you supply the correct key, your server decrypts the data. The process of encryption and decryption are transparent to the consumer/user of the data.
 Please see the more comprehensive article at the Viewpoint Customer Portal[here](https://support.viewpoint.com/s/knowledgedetail?c__urlname=190313184333256).
