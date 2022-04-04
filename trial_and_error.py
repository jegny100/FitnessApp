from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable


class Example(MDApp):
    def build(self):
        layout = AnchorLayout()
        data_tables = MDDataTable(
            check=True,
            size_hint=(0.9, 0.6),
            column_data=[
                ("ID", dp(20)),
                ("Column 2", dp(30)),
                ("Column 3", dp(50), self.sort_on_col_3)
            ],
            row_data=[
                # The number of elements must match the length
                # of the `column_data` list.
                (
                    "1",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                    "Astrid: NE shared managed"
                ),
                (
                    "2",
                    ("alert-circle", [1, 0, 0, 1], "Offline"),
                    "Cosmo: prod shared ares"
                )
            ],
        )
        data_tables.bind(on_check_press=self.on_check_press)
        layout.add_widget(data_tables)
        return layout

    def on_check_press(self, instance_table, current_row):
        print("CHECKED ROW!")
        '''Called when the check box in the table row is checked.'''

    def sort_on_col_3(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][3]
            )
        )

    def sort_on_col_2(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][-1]
            )
        )

Example().run()
