import customtkinter as ctk
from helpers import search_powershell_history, remove_powershell_history


class SearchScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(corner_radius=0, fg_color="transparent")

        self._recents: list[str] = []
        self._recent_labels: list[ctk.CTkLabel] = []

        self.set_variables()
        self.create_widgets()

    def set_variables(self):
        """Set the variables for the frame."""
        self.max_lines_stringvar = ctk.StringVar(self, value="10", name="max_lines")

        self.search_stringvar = ctk.StringVar(self, name="search")

    def create_widgets(self):
        """Creates the widgets for the frame."""
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", pady=10)

        lines_entry = ctk.CTkEntry(
            frame, placeholder_text="Lines", textvariable=self.max_lines_stringvar
        )
        lines_entry.pack(side="left", padx=5)

        search_entry = ctk.CTkEntry(
            frame, placeholder_text="Search", textvariable=self.search_stringvar
        )
        search_entry.pack(side="left", padx=5)

        button = ctk.CTkButton(
            frame, text="Search", command=lambda: self.search_recents()
        )
        button.pack(side="right", padx=5)

    def search_recents(self):
        """Search the recents for the search string and update the view"""
        self._recents = search_powershell_history(
            substring=self.search_stringvar.get(),
            max_lines=int(self.max_lines_stringvar.get()),
        )

        for label in self._recent_labels:
            label.destroy()

        self._recent_labels.clear()

        for recent in self._recents:
            self.add_recent(recent)

    def add_recent(self, text: str):
        """Add a recent line to the frame.

        Args:
            text (str): The text of the recent line.
        """
        recent = ctk.CTkButton(
            self,
            text=text,
            font=("Segoe UI", 20),
            command=lambda text=text: self.delete_lines(text),
        )

        recent.pack(fill="x", padx=10, pady=5)

        self._recent_labels.append(recent)

    def delete_lines(self, text: str):
        remove_powershell_history(text)

        self.search_recents()
