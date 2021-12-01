"""
Run this script to create a new entry in the database
"""

from pathlib import Path
import datetime
import uuid
import shutil

human_readable_tag = 'test'


cwd = Path(__file__).parent
root = cwd.parent

ts = datetime.datetime.now()
dirname = ts.strftime(f'%Y%m%d_{human_readable_tag}_{uuid.uuid4()}')

src_dir = root / 'datasets' / '_template'

target_dir = (root / 'datasets' / dirname)
target_dir.mkdir(exist_ok=True)

for src_pth in src_dir.iterdir():
    target_pth = target_dir / src_pth.name
    shutil.copy(src_pth, target_pth)
