import mesop as me

SIDENAV_MIN_WIDTH = 68
SIDENAV_MAX_WIDTH = 200

DEFAULT_MENU_STYLE = me.Style(align_content="left")

# Define the cyberpunk-hacker theme colors
CYBERPUNK_HACKER_THEME = {
    "background": "#000000",  # Black background
    "text": "#FFFFFF",  # White text for contrast
    "shadow": "#FFFFFF",  # White shadows
    "neon_green": "#00FF00",  # Neon green
    "neon_blue": "#0000FF",  # Neon blue
    "neon_purple": "#800080",  # Neon purple
    "neon_pink": "#FF00FF",  # Neon pink
    "neon_yellow": "#FFFF00",  # Neon yellow
    "accent_green": "#00AA00",  # Accent green
}

# Global text gradient
_FANCY_TEXT_GRADIENT = me.Style(
    color="transparent",
    background=(
        f"linear-gradient(72.83deg,{CYBERPUNK_HACKER_THEME['neon_green']} 11.63%,{CYBERPUNK_HACKER_THEME['neon_blue']} 40.43%,{CYBERPUNK_HACKER_THEME['neon_purple']} 68.07%)"
        " text"
    ),
    background_clip="text"
)

MAIN_COLUMN_STYLE = me.Style(
    display="flex",
    flex_direction="column",
    height="100%",
)

PAGE_BACKGROUND_STYLE = me.Style(
    background=CYBERPUNK_HACKER_THEME["background"],
    height="100%",
    overflow_y="scroll",
    margin=me.Margin(bottom=20),
)

PAGE_BACKGROUND_PADDING_STYLE = me.Style(
    background=CYBERPUNK_HACKER_THEME["background"],
    padding=me.Padding(top=24, left=24, right=24, bottom=24),
    display="flex",
    flex_direction="column",
)

# Box styles related to roles and states
# Example: Agent box style
AGENT_BOX_STYLE = me.Style(
    background=CYBERPUNK_HACKER_THEME["neon_green"],
    border=f"2px solid {CYBERPUNK_HACKER_THEME['accent_green']}",
    box_shadow=f"0px 0px 10px {CYBERPUNK_HACKER_THEME['shadow']}",
    padding=me.Padding(top=10, left=10, right=10, bottom=10),
    margin=me.Margin(top=5, left=5, right=5, bottom=5),
)

# Example: Task box style
TASK_BOX_STYLE = me.Style(
    background=CYBERPUNK_HACKER_THEME["neon_blue"],
    border=f"2px solid {CYBERPUNK_HACKER_THEME['neon_green']}",
    box_shadow=f"0px 0px 10px {CYBERPUNK_HACKER_THEME['shadow']}",
    padding=me.Padding(top=10, left=10, right=10, bottom=10),
    margin=me.Margin(top=5, left=5, right=5, bottom=5),
)

# Example: Active State box style
ACTIVE_BOX_STYLE = me.Style(
    background=CYBERPUNK_HACKER_THEME["neon_yellow"],
    border=f"2px solid {CYBERPUNK_HACKER_THEME['neon_green']}",
    box_shadow=f"0px 0px 10px {CYBERPUNK_HACKER_THEME['shadow']}",
    padding=me.Padding(top=10, left=10, right=10, bottom=10),
    margin=me.Margin(top=5, left=5, right=5, bottom=5),
)
