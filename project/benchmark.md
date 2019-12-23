tests/test_storage_google.py::TestStorage::test_benchmark 
+----------------------------+-------+---------------------+--------+----------------------------------+----------------+--------+-------------+-------------+ 
| timer                      | time  | start               | tag    | node                             | user           | system | mac_version | win_version |
+----------------------------+-------+---------------------+--------+----------------------------------+----------------+--------+-------------+-------------+
| create source              | 0.001 | 2019-12-20 22:40:57 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| create dir                 | 0.489 | 2019-12-20 22:40:57 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| put                        | 0.355 | 2019-12-20 22:40:57 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| get                        | 0.677 | 2019-12-20 22:40:58 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| list                       | 0.152 | 2019-12-20 22:40:58 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| delete                     | 0.219 | 2019-12-20 22:40:59 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| test_blob_metadata         | 0.076 | 2019-12-20 22:41:00 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| test_rename_blob           | 0.074 | 2019-12-20 22:41:00 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| test_copy_blob_btw_buckets | 0.531 | 2019-12-20 22:41:01 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| test_create_bucket_google  | 0.54  | 2019-12-20 22:41:02 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| test_list_bucket_google    | 0.11  | 2019-12-20 22:41:02 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
| benchmark_start_stop       | 0.0   | 2019-12-20 22:41:03 | google | ('Shreyanss-MacBook-Pro.local',) | shreyansjain_2 | Darwin | 10.15.1     |             |
+----------------------------+-------+---------------------+--------+----------------------------------+----------------+--------+-------------+-------------+
