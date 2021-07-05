# ds-dvc-demo

Clone the repo and create the conda environment:

```
conda env create -f environment.yaml
```

This will install `dvc` using pip and including the s3 backend.

## Initialise dvc

Initialise dvc on a new branch in the repository root:

```
git checkout -b dvc_init
dvc init
git commit -m 'dvc init'
```

This will initialize dvc in the repo. It will throw an error if you are not in repo tracked by git or simlar verscion control system. 

- `.dvc` directory contains the config files and local cache. There is a .gitignore created also.
- `.dvcignore` equivilent to .gitignore, to specify files/folders that dvc should not track.

These will need to be commited to git. 

## Add some data

Use `dvc add` to add raw data for dvc to track. This creates a .dvc for our dataset which needs to be added and commited to git. The data itself will be git ignored. 

```
dvc add data/raw_ais.csv
git add data/raw_ais.csv.dvc data/.gitignore
git commit -m 'add raw data'
```

## Add a remote storage and push

Add s3 remote storage location and push our data to it. 

```
dvc remote add -d s3remote s3://davids-scratch/dvc-demo
git commit -a -m 'add remote'
dvc push
```

## Pull data to new machine

```
git clone git@github.com:UKHO/ds-dvc-demo.git
git checkout dvc_init
dvc pull
```

## Modify data and checkout between versions

Switching between versions of raw data. On a new branch modify our raw data to simulate reciving some new data. 

```
git checkout -b raw_data_v2
head -n -1000 raw_ais.csv > raw_ais_modified.csv
mv raw_ais_modified.csv raw_ais.csv
```

Running `dvc status` should tell us that dvc has detected the data changed. We want to commit the new data to the cache and then commit the updated .dvc file to git.  

```
dvc status
dvc commit data/raw_ais.csv
git status
git commit -a -m 'raw data modified'

```

Switching between versions of the data is then a case of checking out the old branch and then doing `dvc checkout` to pull the old version from the dvc cache. 

```
git checkout dvc_init
dvc checkout
```


## Gotchas
- Forgetting to dvc push when you git push
- Forgetting to dvc checkout when you git checkout different branch
- Size of the cache can grow is worth keep an eye on
