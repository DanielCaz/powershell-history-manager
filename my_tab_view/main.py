import customtkinter as ctk
from recents_scroll_view import RecentsScrollFrame
from search_scroll_view import SearchScrollFrame


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._tab_names = ["Recent", "Remove"]

        for tab_name in self._tab_names:
            self.add(tab_name)

        self.create_tabs()

    def create_tabs(self):
        """Create the tabs and add the scrollable frames to them."""
        self.recents_frame = RecentsScrollFrame(self.tab("Recent"))
        self.recents_frame.pack(fill="both", expand=True)

        self.remove_frame = SearchScrollFrame(self.tab("Remove"))
        self.remove_frame.pack(fill="both", expand=True)
