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

ui.run(port=8081, title="Collection Viewer", favicon="📚")
