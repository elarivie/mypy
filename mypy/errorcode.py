from typing import Optional
from typing import Tuple

from mypy.nodes import nongen_builtins


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


def SYNTAX_ERROR(message: str) -> ErrorCode:
    return ErrorCode(19, "error", message)


def SYNTAX_ERROR_TYPE_COMMENT() -> ErrorCode:
    return ErrorCode(20, "error", 'syntax error in type comment')


def DUPLICATE_TYPE_SIGNATURES() -> ErrorCode:
    return ErrorCode(21, "error", "Function has duplicate type signatures")


def TYPE_COMMENT_OR_ANNOTATION_AST_ERROR() -> ErrorCode:
    return ErrorCode(22, "error", "invalid type comment or annotation")


def TYPE_COMMENT_AST_ERROR() -> ErrorCode:
    return ErrorCode(23, "error", "invalid type comment")


def ELLIPSES_CANNOT_ACC_OTHER_ARG_TYPES_IN_FUNCTION_TYPE_SIGNATURE() -> ErrorCode:
    return ErrorCode(24, "error", "Ellipses cannot accompany other argument types "
              "in function type signature.")


def TYPE_SIGNATURE_HAS_TOO_MANY_ARGUMENTS() -> ErrorCode:
    return ErrorCode(25, "error", 'Type signature has too many arguments')


def TYPE_SIGNATURE_HAS_TOO_FEW_ARGUMENTS() -> ErrorCode:
    return ErrorCode(25, "error", 'Type signature has too few arguments')


def DUPLICATE_ARGUMENT(name: str, description: str) -> ErrorCode:
    return ErrorCode(26, "error", "Duplicate argument '{}' in {}".format(name, description))


def INTERNAL_ERROR_NODE_IS_NONE(kind: int) -> ErrorCode:
    return ErrorCode(27, "error", 'Internal error (node is None, kind={})'.format(kind))


def NO_SUBSCRIPT_BUILTIN_ALIAS(name: str, propose_alt: bool = True) -> ErrorCode:
    msg = '"{}" is not subscriptable'.format(name.split('.')[-1])
    replacement = nongen_builtins[name]
    if replacement and propose_alt:
        msg += ', use "{}" instead'.format(replacement)
    return ErrorCode(28, "error", msg)


def METHOD_MUST_HAVE_AT_LEAST_ONE_ARGUMENT() -> ErrorCode:
    return ErrorCode(29, "error", 'Method must have at least one argument')


def IMPLEMENTATION_FOR_AN_OVERLOADED_FUNCTION_IS_NOT_ALLOWED_IN_STUB() -> ErrorCode:
    return ErrorCode(30, "error", "An implementation for an overloaded function "
                     "is not allowed in a stub file")


def IMPLEMENTATION_FOR_AN_OVERLOADED_FUNCTION_MUST_COME_LAST() -> ErrorCode:
    return ErrorCode(31, "error", "The implementation for an overloaded function "
                    "must come last")


def OVERLOADED_FUNCTION_OUTSIDE_STUB_MUST_HAVE_AN_IMPLEMENTATION() -> ErrorCode:
    return ErrorCode(32, "error", "An overloaded function outside a stub file "
                     "must have an implementation")


def DECORATED_PROPERTY_NOT_SUPPORTED() -> ErrorCode:
    return ErrorCode(33, "error", "Decorated property not supported")


def CANNOT_OVERWRITE_NAMEDTUPLE_ATTRIBUTE(prohibited: str) -> ErrorCode:
    return ErrorCode(34, "error", 'Cannot overwrite NamedTuple attribute "{}"'.format(prohibited))


def ATRUNTIME_CAN_ONLY_BE_USED_WITH_PROTOCOL_CLASS() -> ErrorCode:
    return ErrorCode(35, "error", '@runtime can only be used with protocol classes')


def ONLY_SINGLE_OR_GENERIC_CAN_BE_IN_BASES() -> ErrorCode:
    return ErrorCode(36, "error", 'Only single Generic[...] or Protocol[...] can be in bases')


def DUPLICATE_TYPE_VARIABLES_IN_GENERIC_OR_PROTOCOL() -> ErrorCode:
    return ErrorCode(37, "error", "Duplicate type variables in Generic[...] or Protocol[...]")


def SHOULD_LIST_ALL_TYPE_VARIABLE_WITH_GENERIC_OR_PROTOCOL() -> ErrorCode:
    return ErrorCode(38, "error", "If Generic[...] or Protocol[...] is present"
              " it should list all type variables")


def FREE_TYPE_VARIABLE_EXPECTED(name: str) -> ErrorCode:
    return ErrorCode(39, "error", 'Free type variable expected in %s[...]' % name)


def NAMEDTUP_CLASS_ERROR() -> ErrorCode:
    return ErrorCode(40, "error", 'Invalid statement in NamedTuple definition; '
                     'expected "field_name: field_type [= default]"')


def NAMEDTUP_FIELD_NAME_CANNOT_START_WITH_AN_UNDERSCORE(name: str) -> ErrorCode:
    return ErrorCode(41, "error", 'NamedTuple field name cannot start with an underscore: {}'
              .format(name))


def NAMEDTUP_DEFAULT_FIELD_CANNOT_FOLLOW_NONDEFAULT_FIELD() -> ErrorCode:
    return ErrorCode(42, "error", 'Non-default NamedTuple fields cannot follow default fields')


def NAMEDTUP_ONLY_PYTHON36() -> ErrorCode:
    return ErrorCode(43, "error", 'NamedTuple class syntax is only supported in Python 3.6')


def NAMEDTUP_SHOULD_BE_SINGLE_BASE() -> ErrorCode:
    return ErrorCode(44, "error", 'NamedTuple should be a single base')


def INVALID_BASE_CLASS() -> ErrorCode:
    return ErrorCode(45, "error", "Invalid base class")


def X_IS_NOT_A_VALID_BASE_CLASS(name: str) -> ErrorCode:
    return ErrorCode(46, "error", "'%s' is not a valid base class" %
              name)


def CLASS_HAS_TWO_INCOMPATIBLE_BASES_DERIVED_FROM_TUPLE() -> ErrorCode:
    return ErrorCode(47, "error", "Class has two incompatible bases derived from tuple")


def CANNOT_SUBCLASS_NEWTYPE() -> ErrorCode:
    return ErrorCode(48, "error", "Cannot subclass NewType")


def CANNOT_SUBCLASS_VALUE_OF_TYPE_ANY() -> ErrorCode:
    return ErrorCode(49, "error", "Class cannot subclass value of type 'Any'")


def CANNOT_SUBCLASS_X_HAS_TYPE_ANY(name: str) -> ErrorCode:
    return ErrorCode(50, "error", "Class cannot subclass '{}' (has type 'Any')".format(name))


def ENUM_CLASS_CANNOT_BE_GENERIC() -> ErrorCode:
    return ErrorCode(51, "error", "Enum class cannot be generic")


def CANNOT_DETERMINE_CONSISTENT_MRO(name: str) -> ErrorCode:
    return ErrorCode(52, "error", "Cannot determine consistent method resolution order "
         '(MRO) for "%s"' % name)


def METACLASS_DEFINED_AS_INNER_CLASS_NOT_SUPPORTED() -> ErrorCode:
    return ErrorCode(53, "error", "Metaclasses defined as inner classes are not supported")


def MULTIPLE_METACLASS_DEFINITION() -> ErrorCode:
    return ErrorCode(54, "error", "Multiple metaclass definitions")


def CYCLE_IN_INHERITANCE_HIERARCHY() -> ErrorCode:
    return ErrorCode(55, "error", 'Cycle in inheritance hierarchy')


def DUPLICATE_BASE_CLASS(name: str) -> ErrorCode:
    return ErrorCode(56, "error", 'Duplicate base class "%s"' % name)


def DYNAMIC_METACLASS_NOT_SUPPORTED(name: str) -> ErrorCode:
    return ErrorCode(57, "error", "Dynamic metaclass not supported for '%s'" % name)


def INVALID_METACLASS(metaclass_name: str) -> ErrorCode:
    return ErrorCode(58, "error", "Invalid metaclass '%s'" % metaclass_name)


def METACLASS_NOT_INHERITING_FROM_TYPE_NOT_SUPPORTED() -> ErrorCode:
    return ErrorCode(59, "error", "Metaclasses not inheriting from 'type' are not supported")


def INCONSISTENT_METACLASS_STRUCTURE(name: str) -> ErrorCode:
    return ErrorCode(60, "error", "Inconsistent metaclass structure for '%s'" % name)


def ALL_BASE_OF_NEW_TYPED_DICT_MUST_BE_TYPED_DICT_TYPE() -> ErrorCode:
    return ErrorCode(61, "error", "All bases of a new TypedDict must be TypedDict types")


def CANNOT_OVERWRITE_TYPEDDICT_FIELD_WHIlE_MERGING(key: str) -> ErrorCode:
    return ErrorCode(62, "error", 'Cannot overwrite TypedDict field "{}" while merging'
              .format(key))


def CANNOT_OVERWRITE_TYPEDDICT_FIELD_WHIlE_EXTENDING(key: str) -> ErrorCode:
    return ErrorCode(62, "error", 'Cannot overwrite TypedDict field "{}" while extending'
              .format(key))


def TYPEDDICT_CLASS_SYNTAX_IS_ONLY_SUPPORTED_IN_PYTHON36() -> ErrorCode:
    return ErrorCode(63, "error", 'TypedDict class syntax is only supported in Python 3.6')


def TPDICT_CLASS_ERROR() -> ErrorCode:
    return ErrorCode(64, "error", 'Invalid statement in TypedDict definition; '
        'expected "field_name: field_type"')


def NAME_ALREADY_DEFINED(name: str, extra_msg: str) -> ErrorCode:
    return ErrorCode(65, "error", "Name '{}' already defined{}".format(name, extra_msg))


def DUPLICATE_TYPEDDICT(name: str) -> ErrorCode:
    return ErrorCode(66, "error", 'Duplicate TypedDict field "{}"'.format(name))


def RIGHT_HAND_SIDE_VALUES_ARE_NOT_SUPPORTED_IN_TYPEDDICT() -> ErrorCode:
    return ErrorCode(67, "error", 'Right hand side values are not supported in TypedDict')


def VALUE_TOTAL_MUST_BE_TRUE_OR_FALSE() -> ErrorCode:
    return ErrorCode(68, "error", 'Value of "total" must be True or False')


def CANNOT_ASSIGN_MULTIPLE_TYPES_WIHTOUT_EXPLICIT_EPSILON(name: str) -> ErrorCode:
    return ErrorCode(69, "error", 'Cannot assign multiple types to name "{}"'
              ' without an explicit "Type[...]" annotation'
              .format(name))


def TYPE_CANNOT_BE_DECLARED_IN_ASSIGNMENT_TO_NON_SELF_ATTRIBUTE() -> ErrorCode:
    return ErrorCode(70, "error", 'Type cannot be declared in assignment to non-self '
              'attribute')


def UNEXPECTED_TYPE_DECLARATION() -> ErrorCode:
    return ErrorCode(71, "error", 'Unexpected type declaration')


def REQUIRED_POS_ARGS_MAY_NOT_APPEAR_AFTER_DEFAULT_NAMED_VARARGS() -> ErrorCode:
    return ErrorCode(72, "error", "Required positional args may not appear "
         "after default, named or var args")


def POS_DEFAULT_ARGS_NOT_AFTER_NAMED_VARARGS() -> ErrorCode:
    return ErrorCode(73, "error",
        "Positional default args may not appear after named or var args")


def VAR_ARGS_NOT_AFTER_NAMED_VARARGS() -> ErrorCode:
    return ErrorCode(74, "error", "Var args may not appear after named or var args")


def A_KWARGS_MUST_BE_LAST_ARGUMENT() -> ErrorCode:
    return ErrorCode(75, "error", "A **kwargs argument must be the last argument")


def ONLY_ONE_KWARGS_ARGUMENT() -> ErrorCode:
    return ErrorCode(76, "error", "You may only have one **kwargs argument")


def ARGS_CONSTRUCTOR_SUGGESTION(constructor: str) -> ErrorCode:
    return ErrorCode(77, "note", "Suggestion: use {}[...] instead of {}(...)".format(
        constructor, constructor))


def TOO_MANY_ARGUMENTS_FOR_ARGUMENT_CONSTRUCTOR() -> ErrorCode:
    return ErrorCode(78, "error", "Too many arguments for argument constructor")


def EXPECTED_ARGS_CONSTRUCTOR_NAME() -> ErrorCode:
    return ErrorCode(79, "error", "Expected arg constructor name")


def GETS_MULTIPLE_VALUES_FOR_KEYWORD_ARG_NAME(constructor: str) -> ErrorCode:
    return ErrorCode(80, "error", '"{}" gets multiple values for keyword argument "name"'.format(
        constructor))


def GETS_MULTIPLE_VALUES_FOR_KEYWORD_ARG_TYPE(constructor: Optional[str]) -> ErrorCode:
    return ErrorCode(80, "error", '"{}" gets multiple values for keyword argument "type"'.format(
        constructor))


def UNEXPECTED_ARGUMENT_FOR_CONSTRUCTOR_ARG(arg: Optional[str]) -> ErrorCode:
    return ErrorCode(81, "error", 'Unexpected argument "{}" for argument constructor'.format(arg))


def EXPECTED_STRING_LITERAL_FOR_ARG_NAME(name: str) -> ErrorCode:
    return ErrorCode(82, "error", 'Expected string literal for argument name, got {}'.format(name))


def TYPE_VAR_IS_INVALID_AS_TARGET_FOR_TYPE_ALIAS(name: Optional[str]) -> ErrorCode:
    return ErrorCode(83, "error", 'Type variable "{}" is invalid as target for type alias'.format(
        name))


def INVALID_TYPE_ALIAS() -> ErrorCode:
    return ErrorCode(84, "error", 'Invalid type alias')


def CANNOT_USE_BOUND_TYPE_VAR_TO_DEFINE_GENERIC_ALIAS(name: str) -> ErrorCode:
    return ErrorCode(85, "error", 'Can\'t use bound type variable "{}"'
              ' to define generic alias'.format(name))


def TYPE_VAR_USED_WITH_ARG(name: str) -> ErrorCode:
    return ErrorCode(86, "error", 'Type variable "{}" used with arguments'.format(
        name))


def BARE_GENERIC() -> ErrorCode:
    return ErrorCode(87, "error", 'Missing type parameters for generic type')


def SUGGESTION_IS_THERE_SPURIOUS_TRAILING_COMMA() -> ErrorCode:
    return ErrorCode(89, "note", 'Suggestion: Is there a spurious trailing comma?')


def TYPE_MUST_HAVE_EXACTLY_ONE_TYPE() -> ErrorCode:
    return ErrorCode(90, "error", 'Type[...] must have exactly one type argument')


def INVALID_TYPE_CLASSVAR_NESTED_INSIDE_TYPE() -> ErrorCode:
    return ErrorCode(91, "error", 'Invalid type: ClassVar nested inside other type')


def CLASS_VAR_MUST_HAVE_AT_MOST_ONE_TYPE_ARG() -> ErrorCode:
    return ErrorCode(92, "error", 'ClassVar[...] must have at most one type argument')


def FORWARD_REERENCES_TO_TYPE_VAR_PROHIBITED() -> ErrorCode:
    return ErrorCode(93, "note", "Forward references to type variables are prohibited")


def INVALID_TYPE() -> ErrorCode:
    return ErrorCode(88, "error", 'Invalid type')


def INVALID_TYPE_X(name: str) -> ErrorCode:
    return ErrorCode(94, "error", 'Invalid type "{}"'.format(name))


def GENERIC_TUPLE_TYPES_NOT_SUPPORTED() -> ErrorCode:
    return ErrorCode(95, "error", 'Generic tuple types not supported')


def GENERIC_TYPEDDICT_TYPES_NOT_SUPPORTED() -> ErrorCode:
    return ErrorCode(96, "error", 'Generic TypedDict types not supported')


def TEST_FIXTURE_DOES_NOT_DEFINE_X(fullname: str) -> ErrorCode:
    return ErrorCode(97, "note", 'Maybe your test fixture does not define "{}"?'.format(fullname))


def RELATIVE_IMPORT_CLIMBS_TOO_MANY_NAMESPACES() -> ErrorCode:
    return ErrorCode(98, "error", "Relative import climbs too many namespaces")


def PROTOCOL_MEMBERS_MUT_HAVE_DECLARED_TYPE() -> ErrorCode:
    return ErrorCode(99, "error", 'All protocol members must have explicitly declared types')


def TWO_STARRED_EXPRESSIONS_IN_ASSIGNMENT() -> ErrorCode:
    return ErrorCode(100, "error", 'Two starred expressions in assignment')


def CANNOT_ASSIGN_TO_TUPLE() -> ErrorCode:
    return ErrorCode(101, "error", "can't assign to ()")


def INVALID_ASSIGNMENT_TARGET() -> ErrorCode:
    return ErrorCode(102, "error", 'Invalid assignment target')


def STARRED_ASSIGNMENT_TARGET_MUST_BE_IN_LIST_OR_TUPLE() -> ErrorCode:
    return ErrorCode(103, "error", 'Starred assignment target must be in a list or tuple')


def STAR_TYPE_ONLY_ALLOWED_FOR_STARRED_EXPRESSIONS() -> ErrorCode:
    return ErrorCode(104, "error", 'Star type only allowed for starred expressions')


def INCOMPATIBLE_NUMBER_OF_TUPLE_ITEMS() -> ErrorCode:
    return ErrorCode(105, "error", 'Incompatible number of tuple items')


def TUPLE_TYPE_EXPECTED_FOR_MULTIPLE_VARIABLES() -> ErrorCode:
    return ErrorCode(106, "error", 'Tuple type expected for multiple variables')


def NEW_TYPE_CANNOT_BE_USED_WITH_PROTOCOL_CLASSES() -> ErrorCode:
    return ErrorCode(107, "error", "NewType cannot be used with protocol classes")


def COULD_NOT_FIND_X_IN_CURRENT_NAMESPACE(name: str) -> ErrorCode:
    return ErrorCode(108, "error", "Could not find {} in current namespace".format(name))


def CANNOT_DECLARE_THE_TYPE_OF_A_NEWTYPE_DECLARATION() -> ErrorCode:
    return ErrorCode(109, "error", "Cannot declare the type of a NewType declaration")


def CANNOT_REDEFINE_X_AS_A_NEWTYPE(name: str) -> ErrorCode:
    return ErrorCode(110, "error", "Cannot redefine '%s' as a NewType" % name)


def SUGGESTED_ADD_TEST_FIXTURES(suggested_test_fixtures: str) -> ErrorCode:
    return ErrorCode(111,
                     "note",
                     'Consider adding [builtins fixtures/{}] to your test description'.format(
                         suggested_test_fixtures))


def CANNOT_ASSIGN_TO_TYPE() -> ErrorCode:
    return ErrorCode(112, "error", 'Cannot assign to a type')


def PROTOCOL_MEMBERS_CANNOT_BE_DEFINED_VIA_ASSIGNMENT_TO_SELF() -> ErrorCode:
    return ErrorCode(113, "error", "Protocol members cannot be defined via assignment to self")


def TYPEVAR_EXPECTS_STRING_LITERAL_AS_FIRST_ARG() -> ErrorCode:
    return ErrorCode(114, "error", "TypeVar() expects a string literal as first argument")


def FIRST_ARGUMENT_OF_NEWTYPE_MUST_BE_STRING_LITERAL() -> ErrorCode:
    return ErrorCode(115, "error", "Argument 1 to NewType(...) must be a string literal")


def SECOND_ARGUMENT_OF_NEWTYPE_MUST_BE_VALID_TYPE() -> ErrorCode:
    return ErrorCode(116, "error", "Argument 2 to NewType(...) must be a valid type")


def CANNOT_DECLARE_TYPE_OF_TYPE_VARIABLE() -> ErrorCode:
    return ErrorCode(117, "error", "Cannot declare the type of a type variable")


def CANNOT_REDEFINE_X_AS_TYPE_VARIABLE(name: str) -> ErrorCode:
    return ErrorCode(118, "error", "Cannot redefine '%s' as a type variable" % name)


def TOO_FEW_ARGUMENTS_FOR_TYPEVAR() -> ErrorCode:
    return ErrorCode(119, "error", "Too few arguments for TypeVar()")


def UNEXPECTED_ARGUMENT_TO_TYPEVAR() -> ErrorCode:
    return ErrorCode(120, "error", "Unexpected argument to TypeVar()")


def UNEXPECTED_ARGUMENT_TO_TYPEVAR_X(param_name: Optional[str]) -> ErrorCode:
    return ErrorCode(127, "error", "Unexpected argument to TypeVar(): {}".format(param_name))


def TYPEVAR_COVARIANT_MAY_ONLY_BE_TRUE() -> ErrorCode:
    return ErrorCode(121, "error", "TypeVar 'covariant' may only be 'True'")


def TYPEVAR_CONTRAVARIANT_MAY_ONLY_BE_TRUE() -> ErrorCode:
    return ErrorCode(122, "error", "TypeVar 'contravariant' may only be 'True'")


def TYPEVAR_CANNOT_HAVE_BOTH_VALUES_AND_UPPER_BOUND() -> ErrorCode:
    return ErrorCode(123, "error", "TypeVar cannot have both values and an upper bound")


def TYPEVAR_BOUND_MUST_BE_A_TYPE() -> ErrorCode:
    return ErrorCode(124, "error", "TypeVar 'bound' must be a type")


def TYPE_VAR_VALUES_NOT_SUPPORTED() -> ErrorCode:
    return ErrorCode(125, "error", "TypeVar 'values' argument not supported")


def USE_TYPEVAR_WITHOUTVALUES() -> ErrorCode:
    return ErrorCode(126, "error",
        "Use TypeVar('T', t, ...) instead of TypeVar('T', values=(t, ...))")


def NEWTYPE_EXPECTS_TWO_POSITIONAL_ARGUMENTS() -> ErrorCode:
    return ErrorCode(127, "error", "NewType(...) expects exactly two positional arguments")


def STRING_FIRST_ARGUMENT_TO_NEWTYPE_DOES_NOT_MATCH_VAR_NAME(
        argvalue: str, name: str) -> ErrorCode:
    return ErrorCode(128, "error",
        "String argument 1 '{}' to NewType(...) does not match variable name '{}'".format(
            argvalue, name))


def TYPEVAR_CANNOT_BE_BOTH_COVARIANT_AND_CONTRAVARIANT() -> ErrorCode:
    return ErrorCode(129, "error", "TypeVar cannot be both covariant and contravariant")


def TYPEVAR_CANOT_HAVE_ONLY_A_SINGLE_CONSTRAINT() -> ErrorCode:
    return ErrorCode(130, "error", "TypeVar cannot have only a single constraint")


def TYPE_EXPECTED() -> ErrorCode:
    return ErrorCode(131, "error", 'Type expected')


def CLASSVAR_CAN_ONLY_BE_USED_FOR_ASSIGNMENTS_IN_CLASS_BODY() -> ErrorCode:
    return ErrorCode(132, "error", 'ClassVar can only be used for assignments in class body')


def CANT_ASSIGN_MULTI_MOD_TO_X_WITHOUT_MODTYPE_ANNOTATION(name: str) -> ErrorCode:
    return ErrorCode(133, "error", "Cannot assign multiple modules to name '{}' "
    "without explicit 'types.ModuleType' annotation".format(name))


def STRING_FIRST_ARGUMENT_X_TOTYPEVAR_DOESNOT_MATCH_VARIABLE_Y(value: str, name: str) -> ErrorCode:
    return ErrorCode(134, "error",
        "String argument 1 '{}' to TypeVar(...) does not match variable name '{}'".format(
            value, name))


def FIRST_ARG_X_TO_TYPEDDICT_DOES_NOT_MATCH_VAR_Y(name: str, var_name: str) -> ErrorCode:
    return ErrorCode(135, "error",
        "First argument '{}' to TypedDict() does not match variable name '{}'".format(
            name, var_name))


def INVALID_FIELD_TYPE() -> ErrorCode:
    return ErrorCode(136, "error", 'Invalid field type')


def TUPLE_EXPECTED_AS_NAMEDTUPLE_FIELD() -> ErrorCode:
    return ErrorCode(137, "error", "Tuple expected as NamedTuple() field")


def TOO_FEW_ARGUMENTS_FOR_NAMEDTUPLE() -> ErrorCode:
    return ErrorCode(138, "error", "Too few arguments for namedtuple()")


def TOO_MANY_ARGUMENTS_FOR_NAMEDTUPLE() -> ErrorCode:
    return ErrorCode(139, "error", "Too many arguments for namedtuple()")


def UNEXPECTED_ARGUMENT_TO_NAMEDTUPLE() -> ErrorCode:
    return ErrorCode(140, "error", "Unexpected arguments to namedtuple()")


def NAMEDTUPLE_EXPECTS_STRING_LITERAL_AS_FIRST_ARGUMENT() -> ErrorCode:
    return ErrorCode(141, "error", "namedtuple() expects a string literal as the first argument")


def LIST_OR_TUPLE_LITERAL_EXPECTE_AS_SECOND_ARGUMENT_TO_NAMEDTUPLE() -> ErrorCode:
    return ErrorCode(142, "error",
        "List or tuple literal expected as the second argument to namedtuple()")


def STRING_LITERAL_EXPECTED_AS_NAMEDTUPLE_ITEM() -> ErrorCode:
    return ErrorCode(143, "error", "String literal expected as namedtuple() item")


def INVALID_NAMEDTUPLE_FIELD_DEFINITION() -> ErrorCode:
    return ErrorCode(144, "error", "Invalid NamedTuple field definition")


def TOO_MANY_ARGUMENTS() -> ErrorCode:
    return ErrorCode(145, "error", 'Too many arguments')


def INVALID_NAMEDTUPLE_FIELD_NAME() -> ErrorCode:
    return ErrorCode(146, "error", "Invalid NamedTuple() field name")


def CAN_USE_STARRED_EXPRESSION_ONLY_AS_ASSIGNMENT_TARGET() -> ErrorCode:
    return ErrorCode(147, "error", 'Can use starred expression only as assignment target')


def YIELD_FORM_OUTSIDE_FUNCTION() -> ErrorCode:
    return ErrorCode(148, "error", "'yield from' outside function")


def YIELD_FORM_ASYNC_FUNCTION() -> ErrorCode:
    return ErrorCode(149, "error", "'yield from' async function")


def CAST_TARGET_IS_NOT_A_TYPE() -> ErrorCode:
    return ErrorCode(150, "error", 'Cast target is not a type')


def ANY_EPSILON_IS_NOT_SUPPORTED() -> ErrorCode:
    return ErrorCode(151, "error", 'Any(...) is no longer supported. Use cast(Any, ...) instead')


def FIRST_AGUMENT_TO_PROMITE_IS_NOT_A_TYPE() -> ErrorCode:
    return ErrorCode(152, "error", 'Argument 1 to _promote is not a type')


def DEFINITION_OF_X_MISSING_OVERLOAD(name: str) -> ErrorCode:
    return ErrorCode(153, "error", "Definition of '{}' missing 'overload'".format(name))


def NONCONSECUTIVE_OVERLOAD_X_FOUND(name: str) -> ErrorCode:
    return ErrorCode(154, "error", "Nonconsecutive overload {} found".format(name))


def NAME_NOT_DEFINED(name: str, extra: Optional[str]) -> ErrorCode:
    message = "Name '{}' is not defined".format(name)
    if extra:
        message += ' {}'.format(extra)
    return ErrorCode(155, "error", message)


def MODULE_X_HAS_NO_ATTRIBUTE_Y(
        module_name: str, attribute_name: str, extra: Optional[str]) -> ErrorCode:
    message = "Module '{}' has no attribute '{}'".format(module_name, attribute_name)
    if extra:
        message += ' {}'.format(extra)
    return ErrorCode(156, "error", message)


def INVALID_TYPE_COMMENT() -> ErrorCode:
    return ErrorCode(157, "error", 'Invalid type comment')


def INCOMPATIBLE_NUMBER_OF_TYPES_FOR_WITH_TARGETS() -> ErrorCode:
    return ErrorCode(158, "error", 'Incompatible number of types for `with` targets')


def MULTIPLE_TYPES_EXPECTED_FOR_MULTIPLE_WITH_TARGETS() -> ErrorCode:
    return ErrorCode(159, "error", 'Multiple types expected for multiple `with` targets')


def TOO_FEW_ARGUMENTS_FOR_TYPEDDICT() -> ErrorCode:
    return ErrorCode(160, "error", "Too few arguments for TypedDict()")


def TOO_MANY_ARGUMENTS_FOR_TYPEDDICT() -> ErrorCode:
    return ErrorCode(161, "error", "Too many arguments for TypedDict()")


def UNEXPECTED_ARGUMENT_TO_TYPEDDICT() -> ErrorCode:
    return ErrorCode(162, "error", "Unexpected arguments to TypedDict()")
