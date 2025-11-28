import tkinter as tk
from tkinter import ttk
import threading
import time

class VulnerabilityDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mobile Penetration Testing Dashboard")
        self.geometry("800x600")
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Real-Time Vulnerability Scanner", font=("Arial", 18)).pack(pady=15)
        self.scan_btn = ttk.Button(self, text="Start Scan", command=self.start_scan)
        self.scan_btn.pack(pady=10)
        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=15)
        self.report_frame = ttk.LabelFrame(self, text="Detailed Report", width=750, height=400)
        self.report_frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.report_tree = ttk.Treeview(self.report_frame, columns=("Vuln", "Severity", "Details"), show="headings")
        self.report_tree.heading("Vuln", text="Vulnerability")
        self.report_tree.heading("Severity", text="Severity")
        self.report_tree.heading("Details", text="Details")
        self.report_tree.pack(fill="both", expand=True)

    def start_scan(self):
        scan_thread = threading.Thread(target=self.scan)
        scan_thread.start()

    def scan(self):
        vulns = [
            ("SQL Injection", "High", "Found in login endpoint."),
            ("Insecure Storage", "Medium", "Sensitive info in plaintext."),
            ("Weak Encryption", "Medium", "AES ECB mode detected."),
            ("Broken Authentication", "High", "Session tokens are predictable."),
            ("Unvalidated Redirects", "Low", "Found in redirect logic."),
        ]
        for i, vuln in enumerate(vulns):
            self.progress['value'] = (i+1) * (100//len(vulns))
            self.report_tree.insert("", "end", values=vuln)
            self.update_idletasks()
            time.sleep(1)
        self.progress['value'] = 100

if __name__ == "__main__":
    dashboard = VulnerabilityDashboard()
    dashboard.mainloop()
