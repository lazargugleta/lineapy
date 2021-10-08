import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""
ls = [1,2,3,4]
ls[0] = 1
a = 4
ls[1] = a
ls[2:3] = [30]
ls[3:a] = [40]
""",
    location=PosixPath("[source file path]"),
)
call_1 = CallNode(
    source_location=SourceLocation(
        lineno=2,
        col_offset=5,
        end_lineno=2,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="__build_list__",
    ).id,
    positional_args=[
        LiteralNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=6,
                end_lineno=2,
                end_col_offset=7,
                source_code=source_1.id,
            ),
            value=1,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=8,
                end_lineno=2,
                end_col_offset=9,
                source_code=source_1.id,
            ),
            value=2,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=10,
                end_lineno=2,
                end_col_offset=11,
                source_code=source_1.id,
            ),
            value=3,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=12,
                end_lineno=2,
                end_col_offset=13,
                source_code=source_1.id,
            ),
            value=4,
        ).id,
    ],
    keyword_args={},
)
call_2 = CallNode(
    source_location=SourceLocation(
        lineno=3,
        col_offset=0,
        end_lineno=3,
        end_col_offset=9,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="setitem",
    ).id,
    positional_args=[
        call_1.id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=3,
                col_offset=3,
                end_lineno=3,
                end_col_offset=4,
                source_code=source_1.id,
            ),
            value=0,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=3,
                col_offset=8,
                end_lineno=3,
                end_col_offset=9,
                source_code=source_1.id,
            ),
            value=1,
        ).id,
    ],
    keyword_args={},
)
literal_7 = LiteralNode(
    source_location=SourceLocation(
        lineno=4,
        col_offset=4,
        end_lineno=4,
        end_col_offset=5,
        source_code=source_1.id,
    ),
    value=4,
)
call_3 = CallNode(
    source_location=SourceLocation(
        lineno=5,
        col_offset=0,
        end_lineno=5,
        end_col_offset=9,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="setitem",
    ).id,
    positional_args=[
        call_1.id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=5,
                col_offset=3,
                end_lineno=5,
                end_col_offset=4,
                source_code=source_1.id,
            ),
            value=1,
        ).id,
        literal_7.id,
    ],
    keyword_args={},
)
call_6 = CallNode(
    source_location=SourceLocation(
        lineno=6,
        col_offset=0,
        end_lineno=6,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="setitem",
    ).id,
    positional_args=[
        call_1.id,
        CallNode(
            source_location=SourceLocation(
                lineno=6,
                col_offset=3,
                end_lineno=6,
                end_col_offset=6,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="slice",
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=6,
                        col_offset=3,
                        end_lineno=6,
                        end_col_offset=4,
                        source_code=source_1.id,
                    ),
                    value=2,
                ).id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=6,
                        col_offset=5,
                        end_lineno=6,
                        end_col_offset=6,
                        source_code=source_1.id,
                    ),
                    value=3,
                ).id,
            ],
            keyword_args={},
        ).id,
        CallNode(
            source_location=SourceLocation(
                lineno=6,
                col_offset=10,
                end_lineno=6,
                end_col_offset=14,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="__build_list__",
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=6,
                        col_offset=11,
                        end_lineno=6,
                        end_col_offset=13,
                        source_code=source_1.id,
                    ),
                    value=30,
                ).id
            ],
            keyword_args={},
        ).id,
    ],
    keyword_args={},
)
call_9 = CallNode(
    source_location=SourceLocation(
        lineno=7,
        col_offset=0,
        end_lineno=7,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="setitem",
    ).id,
    positional_args=[
        call_1.id,
        CallNode(
            source_location=SourceLocation(
                lineno=7,
                col_offset=3,
                end_lineno=7,
                end_col_offset=6,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="slice",
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=7,
                        col_offset=3,
                        end_lineno=7,
                        end_col_offset=4,
                        source_code=source_1.id,
                    ),
                    value=3,
                ).id,
                literal_7.id,
            ],
            keyword_args={},
        ).id,
        CallNode(
            source_location=SourceLocation(
                lineno=7,
                col_offset=10,
                end_lineno=7,
                end_col_offset=14,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="__build_list__",
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=7,
                        col_offset=11,
                        end_lineno=7,
                        end_col_offset=13,
                        source_code=source_1.id,
                    ),
                    value=40,
                ).id
            ],
            keyword_args={},
        ).id,
    ],
    keyword_args={},
)
