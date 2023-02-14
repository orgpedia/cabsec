# Data-package: orgpedia_cabsec

Posting data of Ministers of India. The data is obtained by processing posting orders from [Cabinet Secretariat's website](https://cabsec.gov.in/).

To get a quick peek check out the [tenures-sample.csv](flow/buildTenure_/output/tenures-sample.csv) it contains a snapshot of the tenure information of Cabinet Secretariat officers.

The tenures information is built by processing orders found on the Cabinet Secretariat's webpage ([import/documents](import/documents)). The orders are processed to build higher level concepts of Tenure and an Org chart. To undersand the processing logic please check out the [Data Processing](#Data_Processiong) section.

## Accessing the data

All the data is available in the [flow/buildTenure_/output](flow/buildTenure_/output) folder and it contains the following files

1. [tenures.json](flow/buildTenure_/output/tenures.json), [tenures.csv](flow/buildTenure_/output/tenures.csv): Tenure information in json and csv format

2. [orders.json](flow/buildTenure_/output/orders.json): Order information in json format.

3. [officer_infos.json](flow/buildTenure_/output/officer_infos.json): Officer ID to name mapping and additional information if available.

4. [post_infos.json](flow/buildTenure_/output/officer_infos.json): Contains hierarchis of different components making up the post `dept`, `role`, `juri`, `loca` and `stat`, which map to Department, Rank, Jurisdiction, Location and Status.

5. [orders/*.order.json](flow/buildTenure_/output/orders/*.order.json): Individual orders in json format.

6. [schema/*.schema.json](flow/buildTenure_/output/schema/*.schema.json): Schema information for all these json files can be found in the [data/schema](flow/buildTenure_/output/schema) directory. check out the [README.md](flow/buildTenure_/output/schema) for an introduction.

You can also Install the orgpedia_cabsec package, the package contains all the data created by this repository.

```
python -m pip install orgpedia_cabsec

```

Once you install the package, all the data is available in `data.zip`. Use this command to get the path of the `data.zip` installed on your computer.

```

python -c "import pkg_resources;pkg_resources.resource_filename('orgpedia_cabsec', 'data.zip')"

<path/to/data.zip>
```

## Data Stats

These are high level statistics, please check [flow](flow) directory for more information.

 - Number of Documents: 904
 - Documents Processed: 817
 - Number of Pages: 2,145

 - Total Edits: 3,885
 - Edits per Page:  *1.8112* (3,885/2,145)

## Data Processing
This is a data package repository - it contains documents, configuration and code for processing the documents and creating data. In a sense it is different from code repositories that only contain code and not the artifacts the code generates.

The data processing is broken down in series of Tasks, where each task processes the data created in the upstream task (links in the `input` folder) and generages new data stored in the `output` folder. The directory layout of this repository follows the ideas mentioned in this video: [Principled Data Processing by Patrick Ball](https://www.youtube.com/watch?v=ZSunU9GQdcI). There are 3 main top-level directories `import`, `flow` and `export`. A *simple* `makefile`  orchestrates the document flow across these folders, run `make help` to find out more about the commands.

You can check out the template repository [template.datapackage](https://github.com/orgpedia/template.datapackage) where each directory and sub-directory is explained. To understand how the data (`/flow/buildTenure_/output`) is generated from documents (`/import/documents/`) explore the [flow](flow) directory.

## Deverloper Notes

If you want to make changes and regenerate data you have two choices

1. Use GitHub codespaces (WIP).
2. Build locally, for this you will need at least 20 GB of space, as we store documents, intermediate data and final data locally. To minimize the space requirement it is recommended that you work only on the buildOrder/* and downstream tasks.


## Local Development
### Prerequisites
- Git with Git LFS
- Python 3.7+
- Poetry
- make


### Installation

#### Git & Git LFS
To install Git, visit the [Git website](https://git-scm.com/) and follow the installation instructions for your operating system. For make sure Git-LFS stays enabled (default option). For othe platforms follow these [instructions](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) on Github.

#### Python
To install Python, visit the [Python website](https://www.python.org/downloads/) and download the  version of Python 3.x for your operating system. Follow the installation instructions for your operating system.

#### Poetry
To install Poetry, visit the [Poetry website](https://python-poetry.org/docs/#installation) and follow installation instructions for your operating system:

#### Make
On Unix based `make` should come pre-installed, on Windows use `winget` to install `make`, follow instructions [here](https://winget.run/pkg/GnuWin32/Make).



### Setup
Orgpedia repository makes heavy use of soft-links, soft-links are stored in the GitHub repository. On non-windows platforms this is not a problem for Windows you need to do two things 1) enable soft-links and 2) tell git about it.

#### Symlinks Setup On Windows
On Windows 11, make sure you have enabled deverloper mode this will automatically enable soft-links on your machine. On windows 10 soft-links were added in Build 14972 and only works on Administrator cmd prompt. More info at this [link](https://blogs.windows.com/windowsdeveloper/2016/12/02/symlinks-windows-10/).

Next you need to tell git it should create soft-links when it sees them in the respository, check the Stack Overflow [answer](https://stackoverflow.com/questions/5917249/git-symbolic-links-in-windows/59761201#59761201) to know more about this. Execute the following command.

```
git config --global core.symlinks true
```


To setup the project, clone the repository using git (this is a large repository, will take several minutes):

```
git clone https://github.com/orgpedia/cabsec.git
```

Navigate to the project directory:

```
cd cabsec
```
Use poetry to install software dependencies(one time only):
```
make install
```

Import models and other data-packages required for the document flow (one time only), these will be downloaded in the `import` folders and it takes a long time.
```
make import
```
### Generate Data

After this you should have all the files needed to generate the data. Make whatever changes you need to make and then execute

```
make flow
```
This will generate the data based on your changes. Currently, make does not track dependencies as a result the entire document flow is re-executed !!
