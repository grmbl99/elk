# Info

## Docker ELK

```bash
docker-compose pull
docker-compose up
```

## Python Conda environment

```bash
conda create -n haystack python=3.10
conda activate haystack
conda install jupyter
```

## Haystack installation

```bash
pip install farm-haystack -f https://download.pytorch.org/whl/torch_stable.html
```

## Use corporate proxy certificate

```python
os.environ['REQUESTS_CA_BUNDLE'] = 'cisco_umbrella_root_ca.cer'
```

## Save roberta model locally

```python
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")
reader.save("roberta_model")
reader_local = FARMReader(model_name_or_path="roberta_model")
```
