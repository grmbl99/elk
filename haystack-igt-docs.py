import os
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.utils import convert_files_to_docs
from haystack.utils import print_answers
from haystack.nodes import BM25Retriever
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline

# required for corporate SSL proxy
os.environ['REQUESTS_CA_BUNDLE'] = 'cisco_umbrella_root_ca.cer'

document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="igt-docs")

doc_dir = "haystackdata/docxtest"
docs = convert_files_to_docs(dir_path=doc_dir, split_paragraphs=True)
#print(docs[:3])
document_store.write_documents(docs)

retriever = BM25Retriever(document_store=document_store)
# this can be used to save a model locally; for later offline use
# reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)
# reader.save("roberta_model")
reader = FARMReader(model_name_or_path="roberta_model", use_gpu=True)
pipe = ExtractiveQAPipeline(reader, retriever)

prediction = pipe.run(
    query="what is the blue color in APC full system", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
)
print_answers(prediction, details="medium")
