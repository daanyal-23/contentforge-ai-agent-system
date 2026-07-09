# run.py
import argparse
import logging

from src.graph import run_graph

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")


def main():
    parser = argparse.ArgumentParser(description="Run agentic content pipeline (LangGraph)")
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to product JSON input file",
    )
    parser.add_argument(
        "--outdir",
        "-o",
        default="out",
        help="Output directory",
    )

    args = parser.parse_args()

    result = run_graph(
        input_path=args.input,
        outdir=args.outdir,
    )

    print("\nPipeline finished.")
    print("Output Directory:", args.outdir)
    print("Product Title:", result["product_page"].get("title"))
    print("FAQ Count:", len(result["faq"]))
    print("Comparison Verdict:", result["comparison"].get("verdict"))


    print("\n===== AGENT EXECUTION TRACE =====")

    for index, event in enumerate(result["execution_trace"], start=1):
        print(
            f"{index}. "
            f"[{event['agent']}] "
            f"{event['status']} -> "
            f"{event['message']}"
        )

        if event.get("metadata"):
            print(
                f"   metadata: {event['metadata']}"
            )

if __name__ == "__main__":
    main()
