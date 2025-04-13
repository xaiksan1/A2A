import mesop as me


SIDENAV_MIN_WIDTH=68
SIDENAV_MAX_WIDTH=200

DEFAULT_MENU_STYLE = me.Style(align_content="left")

_FANCY_TEXT_GRADIENT = me.Style(
    color="transparent",
    background=(
        "linear-gradient(72.83deg,#4285f4 11.63%,#9b72cb 40.43%,#d96570 68.07%)"
        " text"
    ),
)

MAIN_COLUMN_STYLE = me.Style(
    display="flex",
    flex_direction="column",
    height="100%",
    background="black",
    color="lime",
    font_family="Courier New",
    font_size="16px",
)

PAGE_BACKGROUND_STYLE = me.Style(
    background=me.theme_var("background"),
    height="100%",
    overflow_y="scroll",
    margin=me.Margin(bottom=20),
)

PAGE_BACKGROUND_PADDING_STYLE = me.Style(
    background=me.theme_var("background"),
    padding=me.Padding(top=24, left=24, right=24, bottom=24),
    display="flex",
    flex_direction="column",
)

CYBERPUNK_HACKER_STYLE = me.Style(
    background="black",
    color="lime",
    font_family="Courier New",
    font_size="16px",
    box_shadow="0 0 10px lime",
    border="1px solid lime",
    border_radius="5px",
    padding="10px",
    margin="10px",
    transition="all 0.3s ease",
    ":hover": {
        "box_shadow": "0 0 20px lime",
        "transform": "scale(1.05)",
    },
)
