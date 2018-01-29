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


def MSG_SHOW(message: str) -> ErrorCode:
    return ErrorCode(1, "note", message)


def INTERNAL_ERROR() -> ErrorCode:
    return ErrorCode(2, "error", "INTERNAL ERROR --")


def UNUSED_TYPE_IGNORE_COMMENT() -> ErrorCode:
    return ErrorCode(3, "note", "unused 'type: ignore' comment")


def PLUGIN_CANT_FIND(plugin_path: str) -> ErrorCode:
    return ErrorCode(4, "error", "Can't find plugin '{}'".format(plugin_path))


def PLUGIN_DOES_NOT_HAVE_PY_EXTENSION(fnam: str) -> ErrorCode:
    return ErrorCode(5, "error", "Plugin '{}' does not have a .py extension".format(fnam))


def PLUGIN_DOES_NOT_DEFINE_ENTRY_POINT(plugin_path: str) -> ErrorCode:
    return ErrorCode(6,
        "error",
        'Plugin \'{}\' does not define entry point function "plugin"'.format(plugin_path))


def PLUGIN_TYPE_OBJECT_EXPECTED(plugin_type: str, plugin_path: str) -> ErrorCode:
    return ErrorCode(7, "error",
        'Type object expected as the return value of "plugin"; got {!r} (in {})'.format(
            plugin_type, plugin_path))


def PLUGIN_RETURN_VALUE_MUST_SUBCLASS_PLUGIN(plugin_path: str) -> ErrorCode:
    return ErrorCode(8, "error",
        'Return value of "plugin" must be a subclass of "mypy.plugin.Plugin" '
        '(in {})'.format(plugin_path))


def MSG_SHOW_ERROR_CONTEXT(message: str) -> ErrorCode:
    return ErrorCode(9, "note", message)


def MSG_STUB_FILES_ARE_FROM() -> ErrorCode:
    return ErrorCode(10, "note", "(Stub files are from https://github.com/python/typeshed)")


def NO_LIBRARY_STUB_FILE_FOR_STANDARD_LIBRARY_MODULE(moduleName: str) -> ErrorCode:
    return ErrorCode(
        11,
        "error",
        "No library stub file for standard library module '{}'".format(moduleName))


def NO_LIBRARY_STUB_FILE_FOR_MODULE(moduleName: str) -> ErrorCode:
    return ErrorCode(12, "error", "No library stub file for module '{}'".format(moduleName))


def CANNOT_FIND_BUILTINS_MODULE() -> ErrorCode:
    return ErrorCode(13, "error", "Cannot find 'builtins' module. Typeshed appears broken!")


def CANNOT_FIND_MODULE(moduleName: str) -> ErrorCode:
    return ErrorCode(14, "error", "Cannot find module named '{}'".format(moduleName))


def MSG_SHOW_ANCESTOR_PACKAGE_IGNORED(id: str) -> ErrorCode:
    return ErrorCode(15, "note", "Ancestor package '%s' ignored" % (id,))


def MSG_SHOW_IMPORT_IGNORED(id: str) -> ErrorCode:
    return ErrorCode(16, "note", "Import of '%s' ignored" % (id,))


def NO_PARENT_MODULE_CANNOT_PERFORM_RELATIVE_IMPORT() -> ErrorCode:
    return ErrorCode(17, "error", "No parent module -- cannot perform relative import")


def DUPLICATE_MODULE_NAME(name: str) -> ErrorCode:
    return ErrorCode(18, "error", ("Duplicate module named '%s'" % name))
