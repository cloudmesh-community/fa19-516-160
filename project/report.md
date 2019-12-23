
# Cloudmesh Google Storage Service
Contributors:
Shreyans Jain, [fa19-516-160](https://github.com/cloudmesh-community/fa19-516-160/blob/master/project/report.md)  
Gregor von Laszewski


Code: https://github.com/cloudmesh/cloudmesh-google/tree/master/cloudmesh/google

* command code:https://github.com/cloudmesh/cloudmesh-google/blob/master/cloudmesh/google/command/google.py

* Provider code:https://github.com/cloudmesh/cloudmesh-google/blob/master/cloudmesh/google/storage/Provider.py

Manual: https://github.com/cloudmesh/cloudmesh-manual/blob/master/docs-source/source/accounts/google/account.md


Open Issues:

https://github.com/cloudmesh/cloudmesh-oracle/issues
https://github.com/cloudmesh/cloudmesh-storage/issues


Special note: With the class progression my project was changed to
"google storage provider" part of new CMS module cloudmesh-google, initial proposal was cloudmesh transfer.

## Abstract
* Cloudmesh is a multicloud platform. With inclusion of storage
service, a highly optimized and simple to use methos will be made
available to cloudmesh users. Introduction of cloudmesh-goole will  
enable users to perform various storage commands for google cloud storage.

* Local cloud to Google cloud storage and vise versa Cloudmesh Storage
  Provider for Virtual Directories: see cloudmesh-storage to start.
  develop OpenAPI REST services.
  
 
 
# Cloudmesh Google cloud Storage Service	
## Objective

Provide cloudmesh users an API and REST service to transfer files,
directories from data storage of one cloud service provider to other
cloud service provider. This packge will consider  google cloud storage 
implementation.


## Motivation

Cloud technology evolves at a very fast rate. Due to which, policies and
facilities provided by cloud service providers change as well. There
could be various practical scenarios in which users want to use local storage with 
data currently stored in Google storage. Such scenarios could be
get to download file, put to upload file, list or delete blob or object at google location.


## Architecture

![Architecture](images/gregor-cloud-storage.png)

![Architecture](images/Architecture_v2.png)

## Technology
* Python
* cloudmesh storage
* OpenAPI 3.0.2
* REST
* Google Cloud Storage

## Usage storage command
```
Usage:
     storage [--storage=SERVICE] create dir DIRECTORY
     storage [--storage=SERVICE] get SOURCE DESTINATION [--recursive]
     storage [--storage=SERVICE] put SOURCE DESTINATION [--recursive]
     storage [--storage=SERVICE] list [SOURCE] [--recursive] [--output=OUTPUT]
     storage [--storage=SERVICE] delete SOURCE

```
## Usage transfer command
Following transfer command is not implemented and is option for future development:
 
```
  Usage:
        transfer config [--file=ip_file]
        transfer --id=<transfer_id> --data=<file_name> [--copy=True|False]
        transfer status --id=<transfer_id>
        transfer statistic

  This command is part of CloudMesh's multicloud storage service. Command allows users to transfer
  files/directories from storage of one Cloud Service Provider (CSP) to storage of other CSP.
  Current implementation is to transfer data between Azure blob storage and AWS S3 bucket.

  Arguments:
      transfer_id   A unique id/name assigned by user to each transfer instance
      file_name     Name of the file/directory to be transferred
      Boolean       True/False argument for --copy option. When False, data will be removed from source location
      ip_file       Input file used to configure 'transfer' command

  Options:
      --id=transfer_id        Specify a unique i/name to the transfer instance
      --data=file_name        Specify the file/directory name to be transferred
      --copy=True|False       Specify is the data should be kept in source location after the transfer
      --file=ip_file          Specify the file to be used for configuration of the transfer instance
      -h                      Help function

  Description:
      transfer config [options..]
            Configures source/destination and authentication details to be used by transfer command

      transfer [options..]
            Transfers file/directory from storage of one CSP to storage of another CSP

      transfer status [options..]
            Returns status of given transfer instance

      transfer statistic
            Returns statistics of all transfer processes

  Examples:
      transfer --id="Dummy transfer" --data=dummy_file.txt --copy=True
```


## Benchmarks

Benchmark results can be found at folling link:

https://github.com/cloudmesh-community/fa19-516-160/blob/master/project/benchmark.md

## Testing

Py tests can be found at following link:
https://github.com/cloudmesh/cloudmesh-google/tree/master/tests

## Acknowledgements

A sincere thanks to Professor Gregor von Laszewski for his direction and contributions throughout the project. He helped correcting code bugs, providing solution to complex problems with code logic, as well as better documentation. During the couse of this project professor patiently guided and encouraged for improvements. Thanks to Mr. Niranda Perera for reviewing my project. Special thanks to my fellow project members.


## References 

* https://github.com/cloudmesh/cloudmesh-google
* https://cloud.google.com/products/storage/
* https://myaccount.google.com/
* https://support.google.com/accounts/answer/27441
* https://cloud.google.com/docs/authentication
* https://cloudmesh.github.io/cloudmesh-manual/accounts/google.html


