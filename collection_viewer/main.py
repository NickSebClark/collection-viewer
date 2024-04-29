from nicegui import ui


@ui.page("/table_display")
def table():
    ui.table(
        columns=["Name", "Age"],
        rows=[
            ["John", 42],
            ["Jane", 24],
        ],
    )


ui.label("JSON Document Collection Viewer")

ui.link("Table Display", table, new_tab=True)

# ui.set_page_icon("https://nicegui.io/assets/logo.png")

# read from the test_data json file
import json

with open("tests/test_data.json", "r") as f:
    data = json.load(f)[0]

ui.json_editor(
    {"content": {"json": data}},
    on_select=lambda e: ui.notify(f"Select: {e}"),
    on_change=lambda e: ui.notify(f"Change: {e}"),
)

ui.run(port=8081, title="Collection Viewer", favicon="📚")
