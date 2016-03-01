from os import makedirs
from os.path import basename, join, exists
import yaml
import requests
DOCS_LIST = 'docs.yaml'
DOCS_DIR = 'docs/originals'

with open(DOCS_LIST) as df:
    for dateslug, docsdict in yaml.load(df).items():
        for url in docsdict['urls']:
            dirname = join(DOCS_DIR, dateslug)
            makedirs(dirname, exist_ok=True)
            fname = join(dirname, basename(url))
            if not exists(fname):
                print("Downloading", url)
                resp = requests.get(url)
                with open(fname, 'wb') as wf:
                    print("\tSaving to", fname)
                    wf.write(resp.content)
