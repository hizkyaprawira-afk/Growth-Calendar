# Here is your re-sequenced, logical roadmap for **Growth-Calendar**:

---

## 🛠️ Phase 1: Data Preparation (The Foundation)

Before the math starts, we ensure the data is "clean" and "honest."

1.  **Checking Data:** Open your `.xlsx` files from the `data/` folder. Check for data types, column names, and unexpected values (e.g., negative weights).
2.  **Imputing Data:** Fill the gaps. For growth curves, use interpolation to ensure the "smoothness" of the Z-score lines.
3.  **Splitting:** Divide your data into **Training** (to teach the model) and **Testing** (to grade the model).
4.  **Preprocessing:** Scale your features and handle any remaining outliers using `src/preprocessor/`.

---

## 🧠 Phase 2: The Model Lab (Local Env)

This is where `train-algorithm.py` does its work on your `D:` drive.

5.  **Clas/Clus/Reg Logic:** Define your three architectures:
    - **Clustering:** To group children by growth "profiles."
    - **Classification:** To identify stunting risk levels.
    - **Regression:** To predict the actual future Z-score.
6.  **Training:** Let the RandomForest "learn" from your training split.
7.  **Train Log:** Record your training accuracy and parameters into `logs.json`.
8.  **Testing:** Run the trained models against your "Testing" split (the data the model hasn't seen yet).
9.  **Testing Log:** Document the final performance (F1-score for class, MAE for reg).

---

## 📦 Phase 3: The Hand-off (Deployment)

Moving from your local machine to the live link.

10. **Pickling:** Use `model-pickler.py` to freeze your models into `.pkl` files.
    - _Action:_ **Commit & Push** these pickles to GitHub.
11. **St main.py running:** The live Streamlit link detects the push, installs `requirements.txt`, and executes `main.py`.
12. **Output:** The user sees the dashboard, inputs child data, and gets the triple-prediction results.
13. **Debug:** Use `st.error` or Streamlit's log console to fix any pathing issues or secret-key mismatches.
14. **Done:** The Growth-Calendar is live and helping parents!

---

### The Workflow Visualization

### 💡 Pro-Tip for your `logs.json`

Since you are doing **Clustering**, **Classification**, and **Regression** all at once, make sure your `logs.json` separates them like this:

```json
{
  "timestamp": "2026-03-19",
  "classification": { "f1_score": 0.92 },
  "regression": { "mae": 0.15 },
  "clustering": { "silhouette_score": 0.74 }
}
```
