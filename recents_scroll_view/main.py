import customtkinter as ctk
from helpers import read_powershell_history


class RecentsScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(corner_radius=0, fg_color="transparent")

        self._recents: list[str] = []
        self._recent_labels: list[ctk.CTkLabel] = []

        self.bind("<Visibility>", lambda _: self.refresh_recents())

        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets for the frame."""
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", pady=10)

        self.max_lines_stringvar = ctk.StringVar(frame, value="10", name="max_lines")

        entry = ctk.CTkEntry(
            frame, placeholder_text="Lines", textvariable=self.max_lines_stringvar
        )
        entry.pack(side="left", padx=5)

        button = ctk.CTkButton(
            frame, text="Refresh", command=lambda: self.refresh_recents()
        )
        button.pack(side="right", padx=5)

    def refresh_recents(self):
        """Refresh the recents by reading the PowerShell history file."""
        self._recents = read_powershell_history(
            max_lines=int(self.max_lines_stringvar.get())
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
        recent = ctk.CTkLabel(self, text=text, font=("Segoe UI", 20))

        recent.pack(fill="x", padx=10, pady=5)

        self._recent_labels.append(recent)
