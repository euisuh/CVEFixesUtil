import json
import pathlib
import sys

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from prompts_kat import promptD1, promptR1, promptS1  # noqa: E402
from utils import calculate_metrics  # noqa: E402


def test_prompts_render():
    p = promptS1("int f(){}", "Out-of-bounds Write")
    assert "int f(){}" in p and "Out-of-bounds Write" in p
    assert promptD1("x", "Use After Free", "desc").count("desc") == 1
    assert "Out-of-bounds Write" in promptR1("int f(){}", "Out-of-bounds Write")


def test_paired_scoring():
    df = pd.DataFrame({"pred_before": [1, 0, -1], "pred_after": [1, 0, -1]})
    assert calculate_metrics(df, "pred_before", "pred_after") == (1, 1, 1, 1, 1, 1)


def test_notebooks_are_valid_json():
    for f in ROOT.glob("*.ipynb"):
        json.loads(f.read_text())
