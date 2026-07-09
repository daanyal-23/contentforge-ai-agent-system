# src/agents/validator_agent.py

import logging
from src.state import PipelineState

logger = logging.getLogger("ValidatorAgent")


def validate_outputs(state: PipelineState) -> PipelineState:
    """
    Validation agent.

    Responsibilities:
    1. Validate generated artifacts
    2. Identify failed agent
    3. Provide feedback for LangGraph retry routing
    """

    errors = []

    # Reset previous failure
    state.failed_agent = None


    # -------------------------
    # Product Page validation
    # -------------------------
    if not state.product_page:

        errors.append(
            "Missing product_page"
        )

        state.failed_agent = "product_page"


    # -------------------------
    # FAQ validation
    # -------------------------
    if not state.faq or len(state.faq) < 15:

        errors.append(
            "FAQ missing or fewer than 15 items"
        )

        state.failed_agent = "faq"


    # -------------------------
    # Comparison validation
    # -------------------------
    if not state.comparison:

        errors.append(
            "Missing comparison"
        )

        state.failed_agent = "comparison"


    # -------------------------
    # Validation result
    # -------------------------
    if errors:

        state.is_valid = False

        state.error = "; ".join(errors)

        state.errors = errors

        logger.error(
            "Validation failed: %s | Failed Agent: %s",
            state.error,
            state.failed_agent,
        )

    else:

        state.is_valid = True

        state.error = None

        state.errors = []

        state.failed_agent = None

        logger.info(
            "Validation passed"
        )


    return state