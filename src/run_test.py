"""
Testing of applying jobfile to test dataset

"""


from pyhdx.batch_processing import JobParser
from pathlib import Path
import yaml

root_dir = Path(__file__).parent.parent
print(root_dir)

cwd = root_dir / 'datasets' / '_test_SecA'

job_spec = yaml.safe_load((cwd / 'jobfile.yaml').read_text())

parser = JobParser(job_spec, cwd=cwd)
parser.execute()