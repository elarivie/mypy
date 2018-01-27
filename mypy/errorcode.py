from typing import Optional
from typing import Tuple


class ErrorCode():

    def __init__(self, code: int, severity: str, message: str) -> None:
        # A positive numeric code
        self.code = code
        # Either 'error', 'note', or 'warning'.
        self.severity = severity
        self.message = message

    def toTuple(self,
                path: Optional[str],
                line: int,
                column: int) -> Tuple[Optional[str], int, int, str, str, int]:
        """Translate the messages data into a tuple.

        Each tuple is of form (path, line, col, severity, message, code).
        The path item may be None.
        If the line item is negative, the line number is not defined for the tuple.
        """
        return (path, line, column, self.severity, self.message, self.code)


def UNUSED_TYPE_IGNORE_COMMENT() -> ErrorCode:
    return ErrorCode(1, "note", "unused 'type: ignore' comment")


def MSG_SHOW_ERROR_CONTEXT(message: str) -> ErrorCode:
    return ErrorCode(2, "note", message)
