"""
ASADA AND CITTODVEGA: ANXIETY- AND DEPRESSION-RELATED EDUCATIONAL PROTOTYPE

Educational research demonstration only. Not a diagnostic instrument, treatment
selector, or substitute for assessment by a qualified mental-health professional.
The 0-3 symptom scores and burden bands are illustrative and not validated.
Do not enter identifying information. Do not use the score to start, stop, or
change medication or other treatment.

Terminology: Avavasada (आसाद) and Cittodvega (चित्तोद्वेग) are Ayurvedic concepts.
They are not exact equivalents of major depressive disorder or anxiety disorders.
Clinical terms below are descriptive symptom vocabulary, not diagnoses.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

QUESTIONS = [
    ("Low mood / feeling down", "Depressed mood; sadness, emptiness or irritability", "depressed_mood", "avasada"),
    ("Less interest or enjoyment", "Anhedonia; reduced interest or pleasure", "anhedonia", "avasada"),
    ("Low energy / tiring easily", "Fatigue or reduced energy", "fatigue", "avasada"),
    ("Sleep changes", "Insomnia or hypersomnia; altered sleep pattern", "sleep_change", "both"),
    ("Appetite or weight changes", "Appetite or weight change", "appetite_change", "avasada"),
    ("Poor focus or indecision", "Impaired concentration or indecisiveness", "concentration", "both"),
    ("Feeling worthless, guilty, or hopeless", "Worthlessness, excessive guilt or hopelessness", "hopelessness", "avasada"),
    ("Hard to keep up with usual tasks", "Functional impairment in study, work, self-care or relationships", "function", "both"),
    ("Hard-to-control worry", "Excessive worry, difficult to control", "worry", "cittodvega"),
    ("Feeling tense, restless, or on edge", "Psychomotor tension, restlessness or hyperarousal", "tension", "cittodvega"),
    ("Irritability", "Irritability / heightened reactivity", "irritability", "both"),
    ("Racing thoughts or expecting something bad", "Anticipatory anxiety or repetitive anxious thoughts", "racing_thoughts", "cittodvega"),
    ("Body symptoms during worry (e.g., tight muscles, fast heartbeat)", "Somatic arousal: muscle tension, palpitations or autonomic symptoms", "somatic", "cittodvega"),
    ("Avoiding situations because of fear or worry", "Anxiety-related avoidance", "avoidance", "cittodvega"),
]

LIFESTYLE = [
    ("Long or late screen use, especially near bedtime", "screen"),
    ("Long periods sitting / little physical activity", "inactive"),
    ("Irregular sleep or wake times", "sleep_routine"),
    ("Few outdoor or daylight breaks", "daylight"),
    ("Irregular meals or frequent meal skipping", "meals"),
    ("High caffeine / energy-drink intake", "caffeine"),
    ("Reduced contact with supportive people", "isolation"),
    ("Current study, work, financial, family or health stress", "stress"),
]

YOGA_ROUTINE = [
    "Keep a regular wake and sleep schedule; aim for a calm wind-down before bed.",
    "Get daylight and fresh air when practical; take short movement breaks during long sitting.",
    "Build activity gradually: a comfortable walk or gentle mobility can be a starting point.",
    "Optional gentle asanas: Tadasana, Marjaryasana-Bitilasana, Balasana, and supported Setu Bandhasana.",
    "Optional calming practice: comfortable diaphragmatic breathing or a brief body scan; stop if it increases distress.",
    "Reduce stimulating screen use before sleep; use breaks and keep devices away from the bed if helpful.",
    "Plan regular meals, hydration, and one manageable enjoyable or social activity each day.",
    "Adapt or skip poses for pain, pregnancy, dizziness, injury, or medical conditions; seek qualified guidance.",
]

RED_FLAGS = (
    "If there are thoughts of suicide or self-harm, a plan, inability to stay safe, "
    "or immediate danger: stay with a trusted person, move away from means of harm, "
    "and contact local emergency services or go to the nearest emergency department now. "
    "In India, Tele-MANAS can be reached at 14416 or 1-800-891-4416. Do not wait for this score."
)

class App:
    def __init__(self, root):
        self.root = root
        root.title("Avavasada & Cittodvega — Educational Research Assistant")
        root.geometry("1020x850")
        root.minsize(800, 650)
        self.symptom_vars = {}
        self.lifestyle_vars = {}
        self._build()

    def _build(self):
        outer = ttk.Frame(self.root, padding=14)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="AVASĀDA & CITTODVEGA — ANXIETY- AND DEPRESSION-RELATED EDUCATIONAL ASSISTANT",
                  font=("Arial", 14, "bold"), wraplength=960).pack(anchor="w")
        ttk.Label(outer, text="Academic demonstration only • Not a diagnosis or treatment recommendation",
                  foreground="#9a3d16").pack(anchor="w", pady=(4, 10))
        canvas = tk.Canvas(outer, highlightthickness=0)
        scroll = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        body = ttk.Frame(canvas)
        body.bind("<Configure>", lambda _e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=body, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.heading(body, "1. Study details (use a code, never a name)")
        row = ttk.Frame(body); row.pack(anchor="w")
        self.code = tk.StringVar(); self.age = tk.StringVar(); self.duration = tk.StringVar()
        for col, (label, var) in enumerate((("Study code", self.code), ("Age (optional)", self.age), ("Symptom duration", self.duration))):
            ttk.Label(row, text=label).grid(row=0, column=col*2, sticky="w", padx=5, pady=4)
            ttk.Entry(row, textvariable=var, width=22).grid(row=0, column=col*2+1, sticky="w", padx=5, pady=4)

        self.heading(body, "2. Recent symptom check-in")
        ttk.Label(body, text="For an academic demonstration, rate recent impact: 0 none, 1 mild, 2 moderate, 3 severe. "
                  "These ratings and totals are not a validated scale or diagnosis.", wraplength=930).pack(anchor="w")
        grid = ttk.Frame(body); grid.pack(anchor="w", pady=5)
        ttk.Label(grid, text="Everyday wording", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", padx=5)
        ttk.Label(grid, text="Clinical wording (descriptive)", font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w", padx=5)
        ttk.Label(grid, text="0–3", font=("Arial", 10, "bold")).grid(row=0, column=2, sticky="w", padx=5)
        for i, (plain, clinical, key, _group) in enumerate(QUESTIONS, 1):
            ttk.Label(grid, text=plain, wraplength=290).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            ttk.Label(grid, text=clinical, wraplength=430).grid(row=i, column=1, sticky="w", padx=5, pady=2)
            var = tk.StringVar(value="0"); self.symptom_vars[key] = var
            ttk.Combobox(grid, textvariable=var, values=["0", "1", "2", "3"], state="readonly", width=5).grid(row=i, column=2, padx=5)

        self.heading(body, "3. Current routine and context (not causes or diagnoses)")
        ttk.Label(body, text="These factors can affect wellbeing and are useful context; this prototype cannot determine causation.").pack(anchor="w")
        for label, key in LIFESTYLE:
            var = tk.BooleanVar(value=False); self.lifestyle_vars[key] = var
            ttk.Checkbutton(body, text=label, variable=var).pack(anchor="w", padx=5, pady=1)

        self.heading(body, "4. Safety and care-seeking check")
        self.duration_2w = tk.BooleanVar(value=False)
        self.impairment = tk.BooleanVar(value=False)
        self.self_harm = tk.BooleanVar(value=False)
        ttk.Checkbutton(body, text="Symptoms have been present most days for about 2 weeks or longer", variable=self.duration_2w).pack(anchor="w", padx=5)
        ttk.Checkbutton(body, text="Symptoms are making daily life, study/work, relationships, or self-care difficult", variable=self.impairment).pack(anchor="w", padx=5)
        ttk.Checkbutton(body, text="There are thoughts of self-harm / suicide, or the person may not be safe", variable=self.self_harm).pack(anchor="w", padx=5)
        ttk.Label(body, text=RED_FLAGS, foreground="#9a2020", wraplength=930).pack(anchor="w", padx=5, pady=5)

        ttk.Button(body, text="Generate educational summary", command=self.generate).pack(anchor="w", pady=10)
        self.report = tk.Text(body, height=27, width=115, wrap="word", state="disabled")
        self.report.pack(fill="both", expand=True)
        ttk.Label(body, text="Yoga and Dinacharya are optional wellbeing practices, not treatments. They must not delay professional care. "
                  "Do not stop prescribed medication or therapy based on this report.", foreground="#9a3d16", wraplength=930).pack(anchor="w", pady=8)

    def heading(self, parent, text):
        ttk.Label(parent, text=text, font=("Arial", 11, "bold")).pack(anchor="w", pady=(12, 5))

    def generate(self):
        code = self.code.get().strip()
        if not code:
            messagebox.showerror("Study code needed", "Enter a non-identifying study code."); return
        age = self.age.get().strip()
        if age:
            try:
                if not 0 <= int(age) <= 120: raise ValueError
            except ValueError:
                messagebox.showerror("Check age", "Enter a whole number from 0 to 120, or leave it blank."); return
        scores = {k: int(v.get()) for k, v in self.symptom_vars.items()}
        groups = {"avasada": 0, "cittodvega": 0}
        for _plain, _clinical, key, group in QUESTIONS:
            if group in ("avasada", "both"): groups["avasada"] += scores[key]
            if group in ("cittodvega", "both"): groups["cittodvega"] += scores[key]
        total = sum(scores.values())
        burden = "lower" if total <= 14 else "middle" if total <= 28 else "higher"
        lines = ["AVASĀDA & CITTODVEGA — EDUCATIONAL SUMMARY", "=" * 60, f"Date: {date.today().isoformat()}",
                 f"Study code: {code}", f"Age: {age or 'Not recorded'}", f"Duration: {self.duration.get().strip() or 'Not recorded'}", "",
                 "SYMPTOMS (plain language — descriptive clinical terminology)"]
        for plain, clinical, key, _group in QUESTIONS:
            lines.append(f"- {plain} / {clinical}: {scores[key]}/3")
        lines.extend(["", f"Illustrative symptom total: {total}/42 ({burden} reported burden)",
                      f"Avavasada-associated descriptive subtotal: {groups['avasada']}",
                      f"Cittodvega-associated descriptive subtotal: {groups['cittodvega']}",
                      "These project-defined totals are not validated, cannot determine a diagnosis, and must not be used to rank treatment.", "",
                      "AYURVEDIC EDUCATIONAL FRAMING",
                      "Āsāda and Cittodvega are Ayurvedic concepts used here as educational headings. Their meanings and mapping to modern clinical categories vary by source and context. This report does not claim equivalence with depressive or anxiety disorders.", "",
                      "CURRENT CONTEXT REPORTED"])
        selected = [label for label, key in LIFESTYLE if self.lifestyle_vars[key].get()]
        lines.extend(f"- {x}" for x in (selected or ["No listed factors selected"]))
        lines.extend(["These are contextual observations only. Screen use or inactivity alone does not establish a mental-health condition.", "",
                      "GENTLE YOGA AND DINCHARYA IDEAS (OPTIONAL, ADAPTABLE)"])
        lines.extend(f"- {x}" for x in YOGA_ROUTINE)
        lines.extend(["", "CARE GUIDANCE"])
        if self.self_harm.get():
            lines.extend(["PRIORITY: URGENT HUMAN SUPPORT", RED_FLAGS])
        elif self.duration_2w.get() or self.impairment.get():
            lines.append("Because symptoms are persistent or affecting daily function, arrange an assessment with a qualified mental-health professional or physician. A score cannot determine the cause or the right care.")
        else:
            lines.append("If symptoms persist, worsen, or interfere with daily life, contact a qualified mental-health professional or physician. Support and effective care are available.")
        lines.extend(["", "LIMITATIONS", "This educational prototype does not diagnose depression, anxiety, or any Ayurvedic disorder; assess suicide risk; or recommend medicines, herbs, Panchakarma, or treatment. An appropriate clinician considers duration, functioning, medical causes, current medicines, age, and individual circumstances. Do not stop prescribed care.",
                      "", "ACADEMIC NOTE", "If used in research, obtain required ethics approval, use validated instruments administered as instructed, protect participant privacy, and have terminology and references reviewed by relevant faculty and qualified mental-health professionals. The illustrative scoring bands in this demonstration must not be represented as clinically validated."])
        self.report.configure(state="normal"); self.report.delete("1.0", "end"); self.report.insert("1.0", "\n".join(lines)); self.report.configure(state="disabled")

if __name__ == "__main__":
    root = tk.Tk(); App(root); root.mainloop()

