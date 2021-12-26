from pathlib import Path

src: Path = Path(__file__).absolute().parent.parent
project: Path = src.parent
data: Path = project / 'data'
scripts: Path = project / 'scripts'
tests: Path = project / 'tests'
 
for i in list(vars().values()):
    if isinstance(i, Path):
        i.mkdir(parents=True, exist_ok=True)
