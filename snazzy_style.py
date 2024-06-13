from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Token,
)

GREEN = "#88f398"
YELLOW = "#f4f8a7"
WHITE = "#f0f1f0"
DARK_GRAY = "#282935"
PINK = "#ed73bd"
GRAY = "#686767"


class SnazzyStyle(Style):
    styles = {
        Token: WHITE,
        Comment: f"{GRAY} italic",
        Keyword: f"{YELLOW} bold",
        Keyword.Type: f"{YELLOW} nobold",
        Keyword.Constant: f"{PINK} bold",
        Name: WHITE,
        Name.Builtin: f"{PINK} bold",
        Name.Constant: f"{PINK} bold",
        Name.Function: GREEN,
        Name.Quoted: f"{WHITE} bold",
        Name.Variable: f"{WHITE}",
        String: PINK,
        String.Symbol: f"{WHITE} bold",
        String.Name: f"{WHITE} bold",
        Operator: GREEN,
        Punctuation: GREEN,
        Number: f"{PINK} bold",
        Literal: PINK,
        Error: PINK,
    }
    background_color = DARK_GRAY
    highlight_color = PINK
