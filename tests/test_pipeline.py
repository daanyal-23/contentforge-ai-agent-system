from pathlib import Path
from src.graph import run_graph

def test_full_pipeline(tmp_path):
    input_path = "examples/product_glowboost.json"
    outdir = tmp_path / "out"

    state = run_graph(
        input_path=str(input_path),
        outdir=str(outdir)
    )

    assert (outdir / "product_page.json").exists()
    assert (outdir / "faq.json").exists()
    assert (outdir / "comparison_page.json").exists()

    assert state["product_page"] is not None
    assert state["faq"] is not None
    assert state["comparison"] is not None

    assert "execution_trace" in state
    assert len(state["execution_trace"]) > 0

    agents = [
        event["agent"]
        for event in state["execution_trace"]
    ]

    assert "ValidatorAgent" in agents