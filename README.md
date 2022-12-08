# Info

## Docker ELK

The `docker-compose.yml` file contains everything to run a local elasticserach + kibana instance.

Make sure there is a `data` folder in the root of this project. This folder will be mapped to the folder inside the elastic container.

Other than that, just do:

```bash
docker-compose pull
docker-compose up
```

## Python Conda environment

As best practice, install all Python stuff in a dedicated conda environment:

```bash
conda create -n haystack python=3.10
conda activate haystack
conda install jupyter
```

## Haystack installation

Also install the haystack stuff in the conda environment:

```bash
pip install farm-haystack -f https://download.pytorch.org/whl/torch_stable.html
```

## Use corporate proxy certificate

Some corporate environments use internal certificates, to be able to scan outgoing https traffic.

```python
os.environ['REQUESTS_CA_BUNDLE'] = 'cisco_umbrella_root_ca.cer'
```

## Save roberta model locally

```python
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")
reader.save("roberta_model")
reader_local = FARMReader(model_name_or_path="roberta_model")
```
