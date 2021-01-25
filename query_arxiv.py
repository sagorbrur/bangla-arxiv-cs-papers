import json
import arxiv
from tqdm import tqdm

def query_arxiv_by_keywords(query_texts_list, output_json_name="output_papers.json", max_results=100):
  total_papers = []
  for query_text in tqdm(query_texts_list):
      result = arxiv.query(
        query=query_text,
        max_chunk_results=10,
        max_results=max_results,
        iterative=True
      )
      for paper in result():
        total_papers.append(paper)

  with open(output_json_name, 'w') as fp:
    for paper in total_papers:
      json.dump(paper, fp, ensure_ascii=False)
      fp.write("\n")

if __name__=="__main__":
  query_keyword_list = ['bangla', 'bengali', 'bn']
  query_arxiv_by_keywords(query_keyword_list, output_json_name='bangla_arxiv_papers.json', max_results=100000)

