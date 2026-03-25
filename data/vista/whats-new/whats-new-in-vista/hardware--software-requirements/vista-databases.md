---
title: "Vista Databases | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/hardware--software-requirements/vista-databases"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/hardware--software-requirements/vista-databases"
---

# Vista Databases

Depending on your setup, you may have two databases: a
 transactional database and a replica read-only reporting database (Vista Enterprise
 Database).
Note: The Vista Enterprise Database is a
 secondary reporting database only available to cloud-hosted customers who have
 purchased the setup. To learn more about this offering, contact your account
 representative.

Each database has unique benefits:

- Transactional
 database: The transactional database is the primary Vista
 database, which updates in real time. It allows you to do real-time reporting on
 the most up-to-date data. To run Crystal Reports against this database, you must
 select the Transactional
 Report checkbox on the RP Report Titles form.

- Vista
 Enterprise Database: This reporting database is a read-only
 replica of the transactional database. Executing reports off the reporting
 database frees up the transactional database, allowing you to continue to use
 Vista for other functions. This is the default database for running reports that
 do not require a lot of processing power.

For more information about configuring reporting with the Vista
 Enterprise Database, see [Choose a Database to Run Crystal Reports](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/choose-a-database-to-run-crystal-reports).
