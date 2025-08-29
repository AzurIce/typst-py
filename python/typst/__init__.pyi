import pathlib
from typing import List, Optional, TypeVar, overload, Dict, Union, Literal, Tuple

Input = TypeVar("Input", str, pathlib.Path, bytes)
OutputFormat = Literal["pdf", "svg", "png", "html"]


class TypstError(RuntimeError):
    """A structured error raised during Typst compilation or querying.

    This exception provides structured access to Typst diagnostics including
    error messages, hints, and stack traces.

    Attributes:
        message (str): The main error message
        hints (list[str]): List of helpful hints for resolving the error
        trace (list[str]): Stack trace information showing error location context
    """
    message: str
    hints: List[str]
    trace: List[str]

    def __init__(self, message: str, hints: Optional[List[str]] = None, trace: Optional[List[str]] = None) -> None: ...


class TypstWarning(UserWarning):
    """A structured warning raised during Typst compilation.

    This warning provides structured access to Typst warning diagnostics including
    warning messages, hints, and stack traces.

    Attributes:
        message (str): The main warning message
        hints (list[str]): List of helpful hints related to the warning
        trace (list[str]): Stack trace information showing warning location context
    """
    message: str
    hints: List[str]
    trace: List[str]

    def __init__(self, message: str, hints: Optional[List[str]] = None, trace: Optional[List[str]] = None) -> None: ...

class CompilerBuilder:
    def __init__(
        self,
        font_paths: List[Input] = [],
        ignore_system_fonts: bool = False,
        sys_inputs: Dict[str, str] = {},
    ) -> None:
        """Initialize a Typst compiler builder.
        Args:
            font_paths (List[PathLike]): Folders with fonts.
            ignore_system_fonts (bool): Ignore system fonts.
            sys_inputs (Dict[str, str]): string key-value pairs to be passed to the document via sys.inputs
        """
    
    def build_path(self, path: Input) -> "Compiler":
        """Build a Typst compiler.
        Args:
            input: .typ file bytes or path to project's main .typ file.
        Returns:
            Compiler: A Typst compiler.
        """

    def build_bytes(self, data: bytes, root: Input = None) -> "Compiler":
        """Build a Typst compiler.
        Args:
            data: .typ file bytes.
            root: Root path for the Typst project.
        Returns:
            Compiler: A Typst compiler.
        """

class Compiler:
    def compile(
        self,
        output: Optional[Input] = None,
        format: Optional[OutputFormat] = None,
        ppi: Optional[float] = None,
    ) -> Optional[Union[bytes, List[bytes]]]:
        """Compile a Typst project.
        Args:
            output (Optional[PathLike], optional): Path to save the compiled file.
            Allowed extensions are `.pdf`, `.svg` and `.png`
            format (Optional[str]): Output format.
            Allowed values are `pdf`, `svg` and `png`.
            ppi (Optional[float]): Pixels per inch for PNG output, defaults to 144.
        Returns:
            Optional[Union[bytes, List[bytes]]]: Return the compiled file as `bytes` if output is `None`.
        """

    def compile_with_warnings(
        self,
        output: Optional[Input] = None,
        format: Optional[OutputFormat] = None,
        ppi: Optional[float] = None,
    ) -> Tuple[Optional[Union[bytes, List[bytes]]], List[TypstWarning]]:
        """Compile a Typst project and return both result and warnings.
        Args:
            output (Optional[PathLike], optional): Path to save the compiled file.
            Allowed extensions are `.pdf`, `.svg` and `.png`
            format (Optional[str]): Output format.
            Allowed values are `pdf`, `svg` and `png`.
            ppi (Optional[float]): Pixels per inch for PNG output, defaults to 144.
        Returns:
            Tuple[Optional[Union[bytes, List[bytes]]], List[TypstWarning]]: Return a tuple of (compiled_data, warnings).
            The first element is the compiled file as `bytes` if output is `None`, otherwise `None`.
            The second element is a list of structured warnings that occurred during compilation.
        """

    def query(
        self,
        selector: str,
        field: Optional[str] = None,
        one: bool = False,
        format: Optional[Literal["json", "yaml"]] = None,
    ) -> str:
        """Query a Typst document.
        Args:
            selector (str): Typst selector like `<label>`.
            field (Optional[str], optional): Field to query.
            one (bool, optional): Query only one element.
            format (Optional[str]): Output format, `json` or `yaml`.
        Returns:
            str: Return the query result.
        """
